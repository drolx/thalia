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
#  Created At: Mon 30 Dec 2024 15:27:19
#  Modified By: Godwin peter. O (me@godwin.dev)
#  Modified At: Mon 30 Dec 2024 15:27:19


from thalia.cli import cli
from thalia.cli.service_daemon import run
from thalia.cli.service_route import route
from thalia.cli.app_task import task
from thalia.cli.app_create import create


def bootstrap_cli() -> None:
    cli.add_command(run)
    cli.add_command(task)
    cli.add_command(route)
    cli.add_command(create)

    cli()
