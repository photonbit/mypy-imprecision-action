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