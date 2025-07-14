import abc
from typing import Any
from aiohttp import web


class BaseRoute(abc.ABC):
    _app: web.Application
    _path: str
    _method: str

    def __init__(self, app: web.Application):
        super().__init__()
        self._app = app

    @abc.abstractmethod
    def setup_route(self, request: web.Request) -> Any:
        pass
