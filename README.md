<div align="center">

# Python Package Template

_Lightweight template for Python package._

</div>

## How to complete to setup your project

Things you have to do in order to properly set up our project:

- replace all references of `package_name` with the corresponding value of your project in the `pyproject.toml`, `src` folder and `README.md` files.
- replace all references of `owner_name` with the corresponding value of your project in the `pyproject.toml` and `README.md` files.
- setup the corresponding Python versions in the `pyproject.toml` and `.github/workflows/ci.yml` files
- uncomment the necessary `wheels` part in `.github/workflows/release.yml`. If you choose the cibuildwheel (which only works if the build of your project is platform related, e.g. if it has C or C++ extensions) you may need to set Python versions used for the build.
- set the code owners in the `.github` directory if necessary.
- add your PyPI API token as Github secret with the name `PYPI_API_TOKEN`.
- change your name in the `LICENSE` file.

## About this template

This project provide a flexible and lightweight Python package template. It includes the following components:

- a `pyproject.toml` file which define the configuration of the dependencies. The specifications defined by PEP 621 of project metadata are stored in this file.
- a `requirements-dev.txt` file which contains development dependencies.
- a `.pre-commit-config.yaml` pipeline which apply the same dependencies

### Github actions

The project contains multiple Github workflow, including:

- `ci`, apply linting and run tests with `pytest` and `pytest-cov`.
- `draft`, draft a new release when a commit is pushed on branch `main` or `master` given its config file located at `.github/release-drafter.yml`.
- `release`, build the package with `cibuildwheel` when a release is published and upload it to the PyPI index.
- `pre_commit_auto_update`, run a `pre-commit autoupdate` every month and open a pull request if needed.
- `pr_description_enforcer`, enforce description on pull requests, otherwise close the pull request.
- `pr_labeler`, apply a corresponding label on a pull request given its config file located at `.github/pr-labeler.yml`

Some of these actions requires you to allow Github actions to create or approve pull requests. [Learn more.](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#preventing-github-actions-from-creating-or-approving-pull-requests)

The generated badges are located in the `.github/assets/badges/` folder.

## Acknowledgements

- [Lightning-hydra-template](https://github.com/ashleve/lightning-hydra-template)

**DELETE EVERYTHING ABOVE FOR YOUR PROJECT**

______________________________________________________________________

<div align="center">

# Your Project Name

<table>
  <tr>
    <td>
    </td>
    <td>
    </td>
  </tr>
  <tr>
    <td>
      CI/CD
    </td>
    <td>
      <a href="https://github.com/owner_name/package_name/actions/workflows/ci.yml">
        <img src="https://github.com/owner_name/package_name/actions/workflows/ci.yml/badge.svg" alt="CI Pipeline">
      </a>
      <a href="https://github.com/owner_name/package_name/actions/workflows/release.yml">
        <img src="https://github.com/owner_name/package_name/actions/workflows/release.yml/badge.svg" alt="Release">
      </a>
      <a href="https://interrogate.readthedocs.io/en/latest/">
        <img src=".github/assets/badges/interrogate_badge.svg" alt="Interrogate">
      </a>
      <a href="https://codecov.io/gh/owner_name/package_name">
        <img src="https://codecov.io/gh/owner_name/package_name/branch/main/graph/badge.svg" alt="Codecov">
      </a>
    </td>
  </tr>
  <tr>
    <td>
        Meta
    </td>
    <td>
      <a href="https://github.com/astral-sh/ruff">
        <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json" alt="Ruff">
      </a>
      <a href="https://github.com/psf/black">
        <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Black">
      </a>
      <a href="https://github.com/pre-commit/pre-commit">
        <img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit" alt="Pre-commit">
      </a>
      <a href="https://spdx.org/licenses/">
        <img src="https://img.shields.io/github/license/owner_name/package_name?color=blueviolet" alt="License">
      </a>
    </td>
  </tr>
  <tr>
    <td>
        Package
    </td>
    <td>
      <a href="https://pypi.org/project/package_name/">
        <img src="https://img.shields.io/pypi/pyversions/package_name.svg?logo=python&label=Python&logoColor=gold" alt="PyPI - Python version">
      </a>
      <a href="https://pypi.org/project/package_name/">
        <img src="https://img.shields.io/pypi/v/package_name.svg?logo=pypi&label=PyPI&logoColor=gold" alt="PyPI - Version">
      </a>
    </td>
  </tr>
</table>

</div>

______________________________________________________________________

## About this project

My description

## ️️⚙️ Installation

Install the package from the PyPI registry.

```shell
pip install package
```

Install the package from the latest commit of the repository.

```shell
pip install git+https://github.com/owner_name/package_name
```

## ⚡ Usage

### Example

```python
from package_name import foo
```

Insert example usage here.

## ⛏️ Development

Clone the project

```shell
git clone https://github.com/owner_name/package_name
```

In order to install all development dependencies, run the following command:

```shell
pip install -e ".[dev]"
```

To ensure that you follow the development workflow, please setup the pre-commit hooks:

```shell
pre-commit install
```
