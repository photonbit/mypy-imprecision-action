import os
import sys
import re


def extract_tip(report_file: str) -> float:
    with open(report_file, "r") as file:
        for line in file.readlines():
            match = re.search(r"^.*Total.*(\d+\.\d+)% imprecise", line)
            if match:
                return float(match.group(1))
    return 100.0


def main() -> None:
    mypy_config_path = sys.argv[1]
    mypy_report_dir = "mypy_report"
    mypy_report_file = f"{mypy_report_dir}/index.txt"

    mypy_status = os.system(
        f"python -m mypy --install-types --non-interactive "
        f"--config-file {mypy_config_path} --txt-report {mypy_report_dir} ."
    )

    if mypy_status != 0:
        print("::error::Mypy failed")
        sys.exit(1)

    tip = extract_tip(mypy_report_file)
    print(f"TIP={tip}")
    with open(os.environ["GITHUB_OUTPUT"], "a") as fh:
        print(f"TIP={tip}", file=fh)


if __name__ == "__main__":
    main()
