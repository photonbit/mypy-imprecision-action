.PHONY: install dev-install black flake8 mypy pre-commit

install:
	poetry install --only-root

dev-install: install
	poetry install --no-root
	poetry run pre-commit install
	poetry run pre-commit install --hook-type commit-msg
