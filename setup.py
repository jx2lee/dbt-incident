#!/usr/bin/env python
import sys

# require a supported version of Python
if sys.version_info < (3, 8):
    print("Error: dbt does not support this version of Python.")
    print("Please upgrade to Python 3.8 or higher.")
    sys.exit(1)

try:
    from setuptools import find_namespace_packages
except ImportError:
    # the user has a downlevel version of setuptools.
    print("Error: dbt requires setuptools v40.1.0 or higher.")
    print('Please upgrade setuptools with "pip install --upgrade setuptools" and try again')
    sys.exit(1)

from pathlib import Path
from setuptools import setup

# pull the long description from the README
README = Path(__file__).parent / "README.md"

# used for adapter's version and the compatible dbt-core version
VERSION = Path(__file__).parent / "dbt/adapters/incident/__version__.py"

package_name = "dbt-incident"
package_version = "0.0.1"

setup(
    name=package_name,
    version=package_version,
    description="The IncidentAdapter adapter plugin for dbt",
    long_description=README.read_text(),
    author="jx2lee",
    author_email="dev.jaejun.lee.1991@gmail.com",
    url="https://github.com/jx2lee/dbt-incident",
    packages=find_namespace_packages(include=["dbt", "dbt.*"]),
    include_package_data=True,
    install_requires=[
        "dbt-core==1.4.1",
        "dbt-bigquery==1.4.2"
    ],
    python_requires=">=3.9"
)
