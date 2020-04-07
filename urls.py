from aiohttp import web

from apps.chat.urls import routes as chat_urls


routes = [
    web.static('/static', 'static/')
]

routes = routes + chat_urls
