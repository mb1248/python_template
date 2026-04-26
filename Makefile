SHELL := /bin/sh

.PHONY: help install install-all fmt fmt-check lint type-check test test-cov docs-serve docs-build clean-site template-copy template-update

help:
	@echo "Available targets:"
	@echo "  install      - Install base dependencies"
	@echo "  install-all  - Install lint, test, and docs dependency groups"
	@echo "  fmt          - Format code"
	@echo "  fmt-check    - Check formatting without writing changes"
	@echo "  lint         - Run linter"
	@echo "  type-check   - Run mypy"
	@echo "  test         - Run tests"
	@echo "  test-cov     - Run tests with coverage report"
	@echo "  docs-serve   - Serve docs locally"
	@echo "  docs-build   - Build static docs into site/"
	@echo "  clean-site   - Remove generated docs site/"
	@echo "  template-copy DEST=../my-project - Generate project from this template"
	@echo "  template-update - Update generated project from its template"

install:
	pdm install

install-all:
	pdm install -G lint -G pytest -G docs

fmt:
	pdm run fmt

fmt-check:
	pdm run fmt-check

lint:
	pdm run lint

type-check:
	pdm run type-check

test:
	pdm run pytest tests/

test-cov:
	pdm run pytest --cov=python_template --cov-report=term-missing tests/

docs-serve:
	pdm run docs

docs-build:
	pdm run mkdocs build --strict

clean-site:
	rm -rf site/

template-copy:
	@test -n "$(DEST)" || (echo "Usage: make template-copy DEST=../my-project" && exit 1)
	copier copy . "$(DEST)"

template-update:
	copier update
