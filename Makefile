install:
	uv sync

run:
	uv run gendiff

test:
	uv run pytest

test-coverage:
	uv run pytest --cov ./tests

lint:
	uv run ruff check

lint-fix:
	uv run ruff check --fix

check: test lint

build:
	uv build

.PHONY: install test lint selfcheck check build