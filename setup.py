#!/usr/bin/env python

from setuptools import find_packages, setup


def read_requirements(
    path: str,
) -> list[str]:
    """
    Return the PyPI packages contains in a `requirements.txt` given his `path`.

    Args:
        path (str): Path of the file.

    Returns:
        list[str]: Return a list of packages.
    """
    try:
        with open(path) as f:
            return [
                line.strip().split("=")[0]
                for line in f.readlines()
                if not line.startswith(("-", "--", "#"))
            ]
    except FileNotFoundError:
        return []


REQUIREMENTS = read_requirements("requirements.txt")
DEV_REQUIREMENTS = read_requirements("requirements-dev.txt")
EXTRAS = {"dev": DEV_REQUIREMENTS}

EXCLUDE_DIRS = [
    "test",
    "tests",
    "tests.*",
    "*.tests",
    "*.tests.*",
    "examples",
    "docs",
    "out",
    "dist",
    "media",
]

setup(
    name="package",
    version="0.0.1",
    description="",
    author="",
    author_email="",
    url="",
    packages=find_packages(
        exclude=EXCLUDE_DIRS,
    ),
    install_requires=REQUIREMENTS,
    extras_require=EXTRAS,
    entry_points={"console_scripts": []},
)
