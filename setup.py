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
    url="https://github.com/jx2lee/dbt-incident",
    packages=find_namespace_packages(include=["dbt", "dbt.*"]),
    include_package_data=True,
    install_requires=[
        "dbt-core==1.4.1",
    ],
    python_requires=">=3.9"
)
