import aiohttp_jinja2
import jinja2
import weakref

from aiohttp import web
from aiohttp import WSCloseCode

from chat.urls import routes


async def on_shutdown(app):
    for ws in set(app['websockets']):
        await ws.close(code=WSCloseCode.GOING_AWAY,
                       message='Server shutdown')


def init_func():
    app = web.Application()
    app['websockets'] = weakref.WeakSet()
    app.on_shutdown.append(on_shutdown)
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('./chat/static'))
    app.add_routes(routes)

    return app


def main():
    app = init_func()
    web.run_app(app)


if __name__ == '__main__':
    main()
