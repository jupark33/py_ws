import websockets
import asyncio
import datetime
import time

def nowdt():
    now = datetime.datetime.now()
    return now

class WebSocketManager:
    def __init__(self):
        self.websocket = None
        self.running = None

    async def disconnect(self):
        print('disconnect')
        await self.websocket.close()
        # self.running = False

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

                while self.running is True:
                    time.sleep(1)
        except Exception as e:
            print('웹소켓 CONNECT() exception')
            print(e)


if __name__ == '__main__':
    wsm = WebSocketManager()

    # 연결 후 3초후 연결해제 성공
    asyncio.run(wsm.connect())
    time.sleep(3)
    asyncio.run(wsm.disconnect())

    time.sleep(3)
    asyncio.run(wsm.connect())

