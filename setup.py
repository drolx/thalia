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


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setup(
    name="thalia",
    version="0.1",
    description="An easy to use python background task scheduler",
    long_description=read("README.md"),
    author="Godwin Peter .O",
    author_email="me@drolx.com",
    url="https://github.com/drolx/thalia",
    license="MIT",
    platforms=["windows", "osx", "linux"],
    packages=["aiohttp>=3.3.2"],
    python_requires=">=3.6",
    package_data={"thalia": ["configs/*.yml"]},
    install_requires=[
        # "click",
    ],
    classifiers=[
        "Development Status :: 3 - Experimental",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={
        "console_scripts": [
            "thalia=thalia:main",
        ]
    },
)
