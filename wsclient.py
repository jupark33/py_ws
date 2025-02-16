import websockets
import asyncio
import datetime

def nowdt():
    now = datetime.datetime.now()
    return now


class WebSocketManager:
    def __int__(self):
        self.websocket = None

    async def disconnect(self):
        print('disconnect')
        self.websocket.close()

    async def send(self):
        print('send')
        await self.websocket.send(f'{nowdt()}[Client]Hello')

    async def connect(self):
        print('connect')
        try:
            url = 'ws://localhost:8765'
            async with websockets.connect(url, ping_interval=None) as websocket:
                # print('send')
                self.websocket = websocket
                await websocket.send(f'{nowdt()}[Client]Hello')

                while True:
                    a=1
        except Exception as e:
            print('웹소켓 CONNECT() exception')
            print(e)

if __name__ == '__main__':
    wsm = WebSocketManager()
    # await wsm.connect()
    asyncio.run(wsm.connect())
    asyncio.run(wsm.send())

