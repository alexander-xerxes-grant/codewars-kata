install: 
	poetry install --no-root

local: install
	poetry run pre-commit install

lint: flake8 black isort newline-check

lint-fix: black-fix isort-fix

flake8:
	poetry run flake8

black:
	poetry run black --diff --check .

black-fix:
	poetry run black .

isort:
	poetry run isort --diff --check .

isort-fix:
	poetry run isort .

newline-check:
	scripts/newline_check.sh

new-problem difficulty problem:
	poetry run python utils/problem_folder_creator.py {{difficulty}} {{problem}}