import aiohttp_jinja2
from aiohttp import web
from typing import Any, Dict
from thalia.system.services import BaseRoute

routes = web.RouteTableDef()


class TestApi(BaseRoute):
    def __init__(self, app):
        super().__init__(app)

        self._path: str = "/test"
        self._method: str = "*"

    def setup_route(self, request):
        name = request.match_info.get("name", "Anonymous")
        text = "Howdy, " + name

        return web.Response(text=text)


class SampleView(BaseRoute):
    def __init__(self, app):
        super().__init__(app)
        self._path: str = "/{path:.*}"

    @aiohttp_jinja2.template("index.html")
    async def setup_route(self, request) -> Dict[str, Any]:
        return {
            "username": request.match_info.get("username", "fenguo"),
            "current_date": "January 17, 2024",
        }
