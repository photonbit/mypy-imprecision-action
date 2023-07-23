# MyPy Check GitHub Action

The MyPy Check GitHub Action is designed to facilitate the incremental adoption of static typing in Python code. 
By providing automatic checks on the Total Imprecise Percent (TIP) against a set threshold and the base branch, 
this action ensures that any new code committed does not regress but rather enhances the type annotations, 
making the codebase more reliable and robust with each commit.

## Why was this action created?

The Python programming language's "gradual typing" approach allows developers to incrementally adopt static typing 
in their codebases. Gradual typing is beneficial because it combines the flexibility of dynamic typing and the 
robustness of static typing. By incrementally adopting static typing, teams can start reaping the benefits of 
static typing without having to refactor their entire codebase at once.

Incremental typing adoption allows developers to progressively improve the reliability, maintainability, and 
readability of their codebase. By comparing the typing imprecision with the previous code and requiring the 
new code's imprecision to be at least equal to the previous one, this action ensures some degree of typing 
is included. As a result, this promotes incremental improvements and prevents degradation of typing quality.

## Usage

To use this GitHub action in your own repository, add a new workflow file to your .github/workflows directory
and incorporate this action as shown in the example below.

```yaml

name: MyPy Imprecision Check

on:
    pull_request:
        types: [opened, synchronize, reopened, edited]
    push:
        branches: [main]
    workflow_dispatch:

permissions:
  contents: read
  actions: read

jobs:
  mypy-check:
    runs-on: ubuntu-latest
    name: MyPy Check
    steps:
      - name: Check out code
        uses: actions/checkout@v3
      - name: MyPy Check
        uses: photonbit/mypy-imprecision-action@main
        with:
          max_tip: '60'
          mypy_config: 'path_to_your_mypy.ini'
          enable_threshold_check: 'true'
          enable_base_tip_check: 'true'
          github_token: ${{ secrets.GITHUB_TOKEN }}
``` 

## Inputs

This action requires the following inputs:

- **max_tip**: Maximum allowed Total Imprecise Percent (TIP). The default value is '10'. 
- **mypy_config**`: Path to the MyPy configuration file in your repository. 
- **enable_threshold_check**: Enable or disable the threshold check. The default value is 'true'. 
- **enable_base_tip_check**: Enable or disable the base branch TIP check. The default value is 'true'. 
- **github_token**: GitHub token. This is required to fetch base branch TIP if base TIP check is enabled. Usually, you can use **secrets.GITHUB_TOKEN**. At
the moment it is also required to enable **Read repository contents and packages permissions** under the 
__Workflow permissions__ in the **Settings/Actions/General** tab of your repository.

## Limitations

When running on a pull request, this action requires that the base branch would have run the action previously
in order to check the artifact created with the file containing the TIP. Artifacts have a retention period of 90 days
by default, and this can be changed in the repository settings. If the base branch has not run the action previously,
or if the retention period has expired, the action will suppose that the base branch has no typing.

If your base branch last run the action more time than the retention time, you can manually trigger the action
on the base branch to generate or update the artifact and then update the pull request to perform the comparison.

## How to Collaborate

We welcome contributions from the community. If you would like to contribute to this action, please fork this repository, make your changes and create a Pull Request. Be sure to include a detailed description of your changes.
Contact @photonbit for more information.

If you have questions, issues or suggestions, feel free to open an issue in this repository. The maintainer will be notified and should respond as soon as they are able.

This project aims to foster an open and welcoming environment. Please respect the code of conduct and interact professionally with all participants.

## The Benefits of Incremental Typing Adoption

Incremental typing adoption offers multiple benefits:

- **Reduced Errors:** By gradually introducing static typing, you can identify and prevent certain types of errors before running your code.
- **Improved Code Readability:** Type annotations make it clear what kind of values functions expect and return, which can help other developers understand your code more quickly.
- **Better Autocompletion:** Many IDEs use type annotations to provide better autocompletion suggestions.
- **Smooth Refactoring:** Gradual typing allows safer refactoring by catching potential errors during the development phase itself.


The aim is not to be perfect but to be better than yesterday. This GitHub action is your ally on this path towards better software design,
be a better person and have regular bowel movements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.