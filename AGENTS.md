# AGENTS.md

Guidance for OpenCode sessions working in this repository.

## What this repo is

A **Copier template** for scaffolding Python projects. It is not itself a Python
package — there is no `pyproject.toml` or `src/` at the root. Do not run
`uv sync`, `make install`, or `pytest` at the repo root; they will fail.

All renderable project files live under `template/` as Jinja templates
(suffix `.jinja`). The template is defined by `copier.yml` at the root, which
sets `_subdirectory: template`.

## Two-tier layout — do not conflate

| Location                      | Purpose                                                                            |
| ----------------------------- | ---------------------------------------------------------------------------------- |
| `.github/workflows/` (root)   | CI for **this template repo** (PR title checks, template linting)                  |
| `template/.github/workflows/` | CI that **ships to generated projects** (ruff, ty, pytest, coverage, publish)      |
| `.gitignore` (root)           | Ignores for the template repo itself                                               |
| `template/.gitignore`         | Ignores that ship to generated projects                                            |

The same split applies to `.pre-commit-config.yaml`, `.yamlfix.toml`,
`.vscode/` — all live in `template/` and are rendered into generated projects,
not used by the template repo itself.

## Dynamic package directory

The Python package directory is templated as `template/src/{{ package_name }}/`.
Copier renders the directory name at copy time, so a `project_name` of
`my-python-project` produces `src/my_python_project/` (hyphens replaced with
underscores by the `package_name` default in `copier.yml`).

## Testing template changes locally

```sh
# Render the template into a temp dir. All three flags are mandatory:
#   --with jinja2-time  → copier.yml uses jinja2_time.TimeExtension
#   --vcs-ref=HEAD      → test the working tree, not the latest git tag
#   --trust             → _tasks run shell commands (rm -f ...)
uvx --with jinja2-time copier copy . /tmp/render \
	--defaults --vcs-ref=HEAD --trust

# Then verify the rendered project works:
cd /tmp/render && uv sync && make check-lint && make tests
```

To test a specific variant (e.g. no license, or with PyPI publish):

```sh
uvx --with jinja2-time copier copy . /tmp/render \
	--defaults --vcs-ref=HEAD --trust \
	--data license=None --data copyright_holder= --data publish_to_pypi=true
```

## Copier `_tasks` (post-render conditional deletion)

`copier.yml` defines two tasks that run after rendering:

- `publish_to_pypi=false` → removes `.github/workflows/publish-package.yml`
- `license=='None'` → removes `LICENSE`

These are shell commands, which is why `--trust` is required when copying.

## Toolchain notes

- **uv** is the package manager. Generated projects use `uv sync` to install
  dependencies and `uv run` to execute tools.
- **pre-commit** hooks are installed via `uv run pre-commit install`.
- **hatch-vcs** derives the package version from git tags. The
  `_version.py` file is generated at build time under
  `src/<package_name>/_version.py` and is gitignored.
- **No `uv.lock` committed** — gitignored at both root and template levels,
  since each generated project regenerates its own lockfile.

## Makefile recipes (in `template/Makefile`)

Available in rendered projects. Key shortcuts:

| Command              | What it does                                          |
| -------------------- | ----------------------------------------------------- |
| `make install`       | `uv venv` + `uv sync` + `uv pip install -e .`         |
| `make check-lint`    | `ruff check` + `ruff format --check` + `ty check`     |
| `make lint`          | `ruff check --fix` + `ruff format` + `ty check`       |
| `make tests`         | `pytest -vv -s` with coverage                         |
| `make pre-commit-install` | `uv run pre-commit install`                      |

## PR conventions

Enforced by `.github/workflows/pr-enhancement.yml` at the repo root:

- PR titles must follow **conventional commits** (e.g. `feat:`, `fix:`, `chore:`).
- Subject line must **not start with an uppercase letter**.
- PRs labeled `dependencies` bypass title validation (for Renovate).
