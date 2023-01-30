#!/usr/bin/env python

from setuptools import find_packages, setup

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

DEV_REQUIREMENTS = open("requirements-dev.txt").read().strip().split()
EXTRAS = {"dev": DEV_REQUIREMENTS}

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
    install_requires=[],
    extras_require=EXTRAS,
    entry_points={"console_scripts": []},
)
