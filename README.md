# [[ project_name ]]

A modern Python project template powered by [Copier](https://copier.readthedocs.io/), [PDM](https://pdm-project.org/), and [Ruff](https://docs.astral.sh/ruff/).

## Features

- **Package management**: PDM with `src/` layout
- **Linting & formatting**: Ruff (replaces flake8, isort, pyupgrade)
- **Type checking**: mypy in strict mode
- **Testing**: pytest with coverage reporting
- **Documentation**: MkDocs Material theme
- **CI**: Forgejo Actions with format, lint, and matrix test jobs

## Requirements

- Python >= [[ python_version ]]
- [PDM](https://pdm-project.org/) — `pip install pdm`

## Development setup

```bash
# Install all dependency groups
pdm install -G lint -G pytest -G docs

# Format code
pdm run fmt

# Check formatting (non-destructive)
pdm run fmt-check

# Lint
pdm run lint

# Type-check
pdm run type-check

# Run tests with coverage
pdm run pytest --cov=[[ module_name ]] --cov-report=term-missing tests/

# Serve docs locally
pdm run docs

# Build docs into site/
pdm run mkdocs build --strict
```

## Makefile shortcuts

```bash
make install-all
make fmt-check
make lint
make type-check
make test-cov
make docs-build
make template-copy DEST=../my-new-project
```

## Use this template with Copier

```bash
# Install Copier
pip install copier

# Generate a new project
copier copy https://your-forgejo-instance/your-user/python-template my-new-project
```

You will be prompted for:
- `project_name` — PyPI package name (e.g. `my-project`)
- `module_name` — Python package name (auto-derived, e.g. `my_project`)
- `description` — Short project description
- `author_name` / `author_email`
- `python_version` — Minimum Python version (3.11 / 3.12 / 3.13 / 3.14)

Keep `.copier-answers.yml` committed in generated projects. It stores the chosen template answers and enables `copier update` later.

To regenerate/update via Makefile shortcuts:

```bash
# Generate a new project from this template
make template-copy DEST=../my-new-project

# In a generated project: pull changes from the template
make template-update
```

## Documentation deployment (Forgejo)

This template includes [.forgejo/workflows/docs.yml](.forgejo/workflows/docs.yml):
- Builds docs on each push to `main`
- Publishes static output to `gh-pages` branch

If your Forgejo instance has Pages enabled, you can serve that branch as a website.
If Pages is not enabled, you can still use the generated `site/` artifact with any static host.

## License

MIT
