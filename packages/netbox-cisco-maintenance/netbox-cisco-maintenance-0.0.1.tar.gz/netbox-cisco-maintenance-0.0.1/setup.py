#!/usr/bin/env python3
"""Build the netbox-cisco-maintenance Python Package with setuptools"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="netbox-cisco-maintenance",
    version="0.0.1",
    author="Willi Kubny",
    author_email="willi.kubny@gmail.com",
    description="Implementing Cisco maintenance information with the Cisco Support APIs into NetBox",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Django",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: System :: Networking",
        "Topic :: System :: Systems Administration",
    ],
    license="MIT",
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
