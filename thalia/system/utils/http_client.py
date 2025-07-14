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
#  Created At: Thu 19 Dec 2024 12:57:14
#  Modified By: Godwin peter. O (me@godwin.dev)
#  Modified At: Thu 19 Dec 2024 12:57:14

import urllib3
from thalia.common.utils.log import logger
import json


class http:

    response = None

    def __init__(self, payload):
        self.payload = payload

    def execute(self):
        params = self.payload
        # Params sample content
        # params = {
        #   "callType": "POST",
        #   "host": "https://localhost/test",
        #   "headers": {
        #     "Content-Type": "application/json",
        #     "Accept-Charset": "UTF-8",
        #     "Authorization": "",
        #   },
        #   "body": {
        #     "from": "xxxx",
        #     "to": ["+2347xxxxxxxxx", "+2348xxxxxxxxx"],
        #     "text": "",
        #   },
        #   "params": {},
        # }
        try:
            callback_instance = urllib3.PoolManager()
            response = callback_instance.request(
                params["callType"],
                params["host"],
                body=json.dumps(params["body"]).encode("utf-8"),
                headers=params["headers"],
                fields=params["params"],
            )
            self.response = response

            if response.status >= 200 & response.status <= 204:
                logger.info("HTTP request completed..")
            else:
                logger.error("HTTP request encountered some errors..")

        except urllib3.exceptions.NewConnectionError:
            logger.warn("HTTP request failed to complete..")

    def result(self):
        return self.response.data
