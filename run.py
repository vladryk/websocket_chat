import aiohttp_jinja2
import jinja2
from aiohttp import web
from chat.views import index_handler


def init_func():
    app = web.Application()
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('./chat/static'))
    app.router.add_get("/", index_handler)
    return app


def main():
    app = init_func()
    web.run_app(app)


if __name__ == '__main__':
    main()
