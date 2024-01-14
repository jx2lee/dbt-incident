#!/usr/bin/env python
from setuptools import find_namespace_packages, setup

package_name = "dbt-incident"
# make sure this always matches dbt/adapters/{adapter}/__version__.py
package_version = "0.0.1"
description = """The IncidentAdapter adapter plugin for dbt"""

setup(
    name=package_name,
    version=package_version,
    description=description,
    long_description=description,
    author="jx2lee",
    author_email="dev.jaejun.lee.1991@gmail.com",
    url="If you have already made a github repo to tie the project to place it here, otherwise update in setup.py later.",
    packages=find_namespace_packages(include=["dbt", "dbt.*"]),
    include_package_data=True,
    install_requires=[
        "dbt-core~=0.0.1.",
    ],
)
