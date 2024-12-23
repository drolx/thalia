# Copyright (c) 2024 <Godwin peter. O>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
#  Project: thalia
#  Author: Godwin peter. O (me@godwin.dev)
#  Created At: Thu 19 Dec 2024 12:32:37
#  Modified By: Godwin peter. O (me@godwin.dev)
#  Modified At: Thu 19 Dec 2024 12:32:37

import os
from setuptools import setup


def read(filename: str):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setup(
    name="thalia",
    version="0.1",
    description="An easy to use python background task scheduler",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Godwin Peter .O",
    author_email="<peter@drolx.com>",
    url="https://github.com/drolx/thalia/wiki",
    download_url="https://github.com/drolx/thalia",
    license="MIT",
    packages=["thalia"],
    python_requires=">=3.10",
    package_data={
        "thalia": [
            ("configs/*.yml"),
            ("data/*.txt, *.csv, *.xlsx"),
        ]
    },
    install_requires=[
        "PyMySQL>=1.1.1",
        "pysqlite3>=0.5.4",
        "SQLAlchemy>=2.0.36",
        "dependency-injector>=4.44.0",
        "PyYAML>=6.0.2",
        "aiohttp>=3.11.11",
        "click>=8.1.8",
    ],
    entry_points={
        "console_scripts": [
            "thalia = thalia.__main__:main",
        ]
    },
    keywords=["Jobs", "Tasks", "Background", "Tool", "Utility"],
    classifiers=[
        "Development Status :: 0.1 - Alpha/Experimental",
        "Environment :: Other Environment",
        "Intended Audience :: Utility",
        "License :: OSI Approved :: MIT",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Background Task Runner",
    ],
)
