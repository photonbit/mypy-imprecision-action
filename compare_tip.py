import io
import os
import sys

import requests
import zipfile
from github import Github

from extract_tip import extract_tip


def fetch_artifact(download_url: str) -> str:
    response = requests.get(
        download_url, headers={"Authorization": f'token {os.getenv("GITHUB_TOKEN")}'}
    )
    if response.status_code == 200:
        file_like_object = io.BytesIO(response.content)

        with zipfile.ZipFile(file_like_object) as z:
            with z.open("index.txt") as f:
                return f.read().decode("utf-8")
    return ""


def fetch_tip_from_base_branch(owner: str, repo_name: str, base_branch_name: str) -> float:
    g = Github(os.getenv("GITHUB_TOKEN"))
    repo = g.get_repo(f"{owner}/{repo_name}")
    base_tip = 100.0  # default value

    workflow_runs = repo.get_workflow_runs(branch=base_branch_name)  # type: ignore
    if workflow_runs.totalCount == 0:
        return base_tip

    for artifact in workflow_runs[0].get_artifacts():
        if artifact.name == "mypy-report":
            with open("base_mypy_report.txt", "w") as f:
                base_artifact = fetch_artifact(artifact.archive_download_url)
                f.write(base_artifact)
                base_tip = extract_tip("base_mypy_report.txt")
            break

    return base_tip


def main() -> None:
    pr_tip = float(sys.argv[1])
    threshold = float(sys.argv[2])
    enable_threshold_check = sys.argv[3] == "true"
    enable_base_tip_check = sys.argv[4] == "true"

    github_repo = os.getenv("GITHUB_REPOSITORY") or sys.exit(1)
    owner, repo_name = github_repo.split("/")
    base_branch_name = os.getenv("GITHUB_BASE_REF") or sys.exit(1)

    if enable_threshold_check and pr_tip > threshold:
        print(f"::error::PR TIP {pr_tip}% is greater than the maximum allowed TIP {threshold}%")
        sys.exit(1)
    if enable_base_tip_check:
        base_tip = fetch_tip_from_base_branch(owner, repo_name, base_branch_name)
        if pr_tip > base_tip:
            print(f"::error::PR TIP {pr_tip}% is greater than the base branch TIP {base_tip}%")
            sys.exit(1)


if __name__ == "__main__":
    main()
