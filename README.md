<div align="center">

# Python-Package-Template

<a href="https://black.readthedocs.io/en/stable/">
    <img alt="Black" src="https://img.shields.io/badge/Code%20Style-Black-black.svg?labelColor=gray"/>
</a>
<a href="https://github.com/VDuchauffour/python-package-template/actions/workflows/pr_code_quality.yml">
    <img alt="Code quality PR" src="https://github.com/VDuchauffour/python-package-template/actions/workflows/pr_code_quality.yml/badge.svg"/>
</a>
<a href="https://github.com/pre-commit/pre-commit">
    <img alt="Pre-commit" src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white"/>
</a>

*Lightweight template for Python package*

</div>

## About this template

This project provide a flexible and lightweight Python package template. It includes the following components:

- a `pre-commit` pipeline which apply the same dependencies
- a `pyproject.toml` file which define the configuration of the dependencies. You can use it later with your favorite package manager like `Poetry` or `PDM` with commands, resp. `poetry init` and `pdm init`

The `requirements-dev.txt` file which contains development dependencies.

The project contains multiple Github workflow, including:

- `black`, apply black formatter when a push or a PR occurs
- `interrogate`, apply interrogate (docstring coverage) and generate its badge when a push or a PR occurs
- `publish`, publish to PyPI once a release has been published (requires a `PYPI_API_TOKEN` secret)
- `pre_commit_auto_update`, run a `pre-commit autoupdate` every week and open a pull request if needed
- `pr_code_quality`, apply `pre-commit` on modified files when a pull request occurs
- `pr_description_enforcer`, enforce description on pull requests
- `release_drafter`, draft a new release when a pull request are merged into "main" or "master"

Some of these actions requires you to allow Github actions to create or approve pull requests. [Learn more.](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#preventing-github-actions-from-creating-or-approving-pull-requests)

The generated badges are located in the `badges` folder.

## Acknowledgements

- [Lightning-hydra-template](https://github.com/ashleve/lightning-hydra-template)

**DELETE EVERYTHING ABOVE FOR YOUR PROJECT**

______________________________________________________________________

<div align="center">

# Your Project Name

<a href="https://black.readthedocs.io/en/stable/">
    <img alt="Black" src="https://img.shields.io/badge/Code%20Style-Black-black.svg?labelColor=gray"/>
</a>
<a href="https://github.com/pre-commit/pre-commit">
    <img alt="Pre-commit" src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white"/>
</a>
<a href="https://interrogate.readthedocs.io/en/latest/#">
    <img alt="Interrogate" src="./badges/interrogate_badge.svg"/>
</a>

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
