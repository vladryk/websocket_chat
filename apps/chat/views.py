import aiohttp
import aiohttp_jinja2
from aiohttp import web
from nickname_generator import generate


async def index_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    request.app['websockets'].add(ws)
    user_nickname = generate()

    try:
        async for msg in ws:
            if msg.type == aiohttp.WSMsgType.TEXT:
                if msg.data == 'close':
                    await ws.close()
                else:
                    for _ws in request.app['websockets']:
                        await _ws.send_str(f'{user_nickname}: {msg.data}')
            elif msg.type == aiohttp.WSMsgType.ERROR:
                print('ws connection closed with exception %s' %
                      ws.exception())
    finally:
        request.app['websockets'].discard(ws)

    print('websocket connection closed')
    return ws


@aiohttp_jinja2.template('chat.html')
async def index(request):
    return {}
