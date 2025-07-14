import os
from aiohttp import web
import aiohttp_jinja2
import jinja2
from thalia.system.services import default_route
from thalia.system.services import BaseRoute
from thalia.system.utils import get_child_classes


def setup_routes(app: web.Application) -> web.Application:
    current_dir_path: str = os.path.dirname(os.path.abspath(__file__))
    static_dir = os.path.join(current_dir_path, "..", "static")
    template_path: str = os.path.join(current_dir_path, "..", "templates")

    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(template_path))

    app.router.add_static("/static", static_dir)
    # app.router.add_route('GET', "/test/{name}", test_handler)
    # app.router.add_view("/{username}", page_sample)
    # app.router.add_view("/{path:.*}", page_sample)

    # testing = get_child_classes(default_route, BaseRoute)
    # click.echo(testing)

    discovered_routes = BaseRoute.__subclasses__()
    for child_route in discovered_routes:
        instance = child_route(app=app)
        child_route_name = instance.__class__.__name__

        if child_route_name.endswith("View"):
            app.router.add_view(instance._path, instance.setup_route)
        else:
            app.router.add_route(instance._method, instance._path, instance.setup_route)

    return app
