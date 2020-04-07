from apps.chat.views import index_handler, index
from aiohttp import web

routes = [
            web.get('/ws', index_handler),
            web.get('/', index)
]
