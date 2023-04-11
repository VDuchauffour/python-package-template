<div align="center">

# Python-Package-Template

[![CI](https://github.com/VDuchauffour/python-package-template/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/VDuchauffour/python-package-template/actions?query=workflow%3Aci+branch%3Amain)
[![interrogate](.github/assets/badges/interrogate_badge.svg)](https://interrogate.readthedocs.io/en/latest/)

_Lightweight template for Python package_

</div>

## About this template

This project provide a flexible and lightweight Python package template. It includes the following components:

- a `pyproject.toml` file which define the configuration of the dependencies. The specifications defined by PEP 621 of project metadata are stored in this file.
- a `requirements.txt` file which contains dependencies.
- a `requirements-dev.txt` file which contains development dependencies.
- a `.pre-commit-config.yaml` pipeline which apply the same dependencies

### Github actions

The project contains multiple Github workflow, including:

- `ci`, apply linting and run tests with `pytest` and `pytest-cov`
- `draft`, draft a new release when a pull request are merged into "main" or "master"
- `release`, create and update a latest tag pointing to your latest release, publish this release to PyPI index.
- `submodules_update`, perform a `git pull` on every submodules, requires a `PAT_TOKEN` secret for checkout of private submodules
- `pre_commit_auto_update`, run a `pre-commit autoupdate` every week and open a pull request if needed
- `pr_description_enforcer`, enforce description on pull requests

Some of these actions requires you to allow Github actions to create or approve pull requests. [Learn more.](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#preventing-github-actions-from-creating-or-approving-pull-requests)

Things you have to do in order to properly set up our project:

- replace all references to `package` with the name of your project in the `pyproject.toml` and `README.md` files.
- change your name in the `LICENSE` file.
- set the code owners in the `.github` directory if necessary.
- add your PyPI API token as Github secret with the name `PYPI_API_TOKEN`.

The generated badges are located in the `.github/assets/badges/` folder.

## Acknowledgements

- [Lightning-hydra-template](https://github.com/ashleve/lightning-hydra-template)

**DELETE EVERYTHING ABOVE FOR YOUR PROJECT**

---

<div align="center">

# Your Project Name

[![CI](https://github.com/VDuchauffour/python-package-template/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/VDuchauffour/python-package-template/actions?query=workflow%3Aci+branch%3Amain)
[![interrogate](.github/assets/badges/interrogate_badge.svg)](https://interrogate.readthedocs.io/en/latest/)
[![codecov](https://codecov.io/gh/VDuchauffour/python-package-template/branch/main/graph/badge.svg)](https://codecov.io/gh/VDuchauffour/python-package-template)

</div>

## Description

My description

## Installation

Install the package from the latest commit of the repository.

```shell
pip install git+https://github.com/Username/Repo
```

## Development

Clone project

```shell
git clone https://github.com/Username/Repo
```

Install development requirements

```shell
pip install -r requirements-dev.txt
```

Install pre-commit hooks

```shell
pre-commit install
```
