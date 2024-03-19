
import os
import re
from glob import glob

from setuptools import find_packages, setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def read_requires(fname):
    lines = read(fname).splitlines()
    # Remove comment lines, some versions of setup fail creating on requirements with comments
    lines = [
        line
        for line in lines
        if not (line.strip().startswith("#") or not line.strip())
    ]
    return lines


def read_version(fname):
    # determine version
    with open(fname) as f:
        constants = f.read()
    version = re.search(
        r'^\s*VERSION\s*=\s*[\'"](.+)[\'"]\s*$', constants, re.MULTILINE
    ).group(1)
    return version


setup(
    name="michael-scott-bot",
    version=read_version("python_boilerplate/constants.py"),
    author="",
    packages=find_packages(exclude=["tests", "tests.*"]),
    url="https://github.com",
    description="A boilerplate python library.",
    license=read("LICENSE.txt").replace("\n", " "),
    data_files=[("", glob("LICENSE*"))],
    long_description=read("README.md"),
    install_requires=read_requires("requirements.txt"),
    test_suite="tests",
    setup_requires=["pytest-runner"],
    tests_require=read_requires("requirements-dev.txt"),
    python_requires=">=3.11",
)
