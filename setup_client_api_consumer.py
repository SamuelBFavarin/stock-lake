#!/usr/bin/env python

"""The setup script."""

__package_name__ = "client-api-consumer"
__version__ = "0.1.1"

from setuptools import setup, find_packages

with open("client_api_consumer/requirements.txt") as f:
    requirements = [line for line in f.read().splitlines() if len(line) > 0]

setup(
    author="samuel-favarin",
    python_requires=">=3.7",
    classifiers=[
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    description="Extract data from crypto api",
    install_requires=requirements,
    include_package_data=True,
    keywords="client-api-consumer",
    name=__package_name__,
    version=__version__,
    packages=find_packages(
        include=[
            "client_api_consumer",
            "client_api_consumer.*",
        ]
    ),
)