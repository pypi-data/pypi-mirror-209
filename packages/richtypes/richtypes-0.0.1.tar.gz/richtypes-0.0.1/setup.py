from __future__ import print_function
from setuptools import setup
import setuptools


# Package meta-data.
NAME = "richtypes"
DESCRIPTION = "Enhanced python datatypes"
KEYWORDS = [NAME, "DATATYPES", "ENHANCEMENT", "LISTS", "DICTIONARY", "UTILITY"]
GIT_URL = "https://github.com/sarvesh4396/richtypes"
AUTHOR = "Sarvesh Kumar Dwivedi"
AUTHOR_EMAIL = "heysarvesh@pm.me"
REQUIRES_PYTHON = ">=3.7.0"
VERSION = "0.0.1"


setup(
    name=NAME,
    packages=[NAME],
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    long_description_content_type="text/markdown",
    long_description=open("README.md").read(),
    python_requires=REQUIRES_PYTHON,
    url=GIT_URL,
    install_requires=[],
    extras_require={"dev": ["pytest", "pytest-pep8", "pytest-cov"]},
    license="MIT",
    keywords=KEYWORDS,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: User Interfaces",
        "Typing :: Typed",
        "Topic :: Utilities",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
