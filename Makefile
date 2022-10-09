install:
	poetry install

gendiff:
	poetry run gendiff
	
build:
	poetry build
	
publish:
	poetry publish --dry-run
	
package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl
	
lint:
	poetry run flake8 gendiff

check:
	selfcheck test lint

test-coverage:
	poetry run coverage run -m pytest

test:
	poetry run pytest
