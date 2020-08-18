# Copyright (c) 2020 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the COPYING file.

"""Import readme and create package info."""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cloudvision",
    version="1.0.0",
    description="A Python library for Arista's CloudVision APIs.",
    maintainer_email="support@arista.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aristanetworks/cloudvision-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)