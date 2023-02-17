#!/usr/bin/env python

import re

from setuptools import find_packages, setup


def get_package_version(package_version_path: str) -> str:
    """
    Return the version of the package given the path of the `_version.py` file on the root of the package.

    Args:
        package_version_path (str): Path of the `_version.py` file.

    Raises:
        ValueError: Raised if no groups has been captured given the pattern.
        RuntimeError: Raised if the file is not found.

    Returns:
        str: Package version.
    """
    try:
        with open(package_version_path) as f:
            _version = f.read().strip()
    except FileNotFoundError:
        raise RuntimeError(
            f"Unable to find version string in `{package_version_path}`."
        )

    pattern = r"^__version__ = ['\"]([^'\"]*)['\"]"
    s = re.search(pattern, _version, re.M)
    if s is not None:
        return str(s.group(1))
    raise ValueError(f"No group captured for the pattern `{pattern}`.")


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

VERSION_FILE = "package/_version.py"

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

if __name__ == "__main__":
    setup(
        name="package",
        version=get_package_version(VERSION_FILE),
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
