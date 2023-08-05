import codecs
import os.path

from setuptools import find_packages, setup


def read(rel_path: str) -> str:
    """Read a file."""
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), "r") as fp:
        return fp.read()


def get_version(rel_path: str) -> str:
    """Read version from a file."""
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


file = open("README.md", "r")
LONG_DESCRIPTION = file.read()
file.close()


base_packages = [
    "Click>=8.0.1",
    "rich>=10.3.0",
    "pyyaml>=5.4.1",
    "timeago>=1.0.15",
    "psutil>=5.8.0",
]
dev = [
    "mkdocs-material>=7.1",
    "mkdocs-macros-plugin",
    "pytest",
    "pytest-cov",
    "pytest-mock",
    "pre-commit",
    "black",
    "flake8",
    "mypy",
    "isort",
]

setup(
    name="doing-cli",
    version=get_version("src/doing/__init__.py"),
    packages=find_packages("src"),
    package_dir={"": "src"},
    description="CLI tool to simplify the development workflow on azure devops",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author="ING Bank N.V.",
    author_email="tim.vink@ing.com",
    url="https://github.com/ing-bank/doing-cli",
    install_requires=base_packages,
    extras_require={"all": base_packages + dev},
    entry_points={"console_scripts": ["doing = doing.cli:cli"]},
    python_requires=">=3.7",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
