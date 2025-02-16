import asyncio
import websockets

# async def server_handler(websocket, path):
#     async for message in websocket:
#         print(f"Received message: {message}")
#
# async def main():
#     async with websockets.serve(server_handler, "localhost", 8765):
#         await asyncio.Future()  # 서버가 실행 상태로 유지되도록 대기
#
# asyncio.run(main())

import asyncio
from websockets.asyncio.server import serve

async def echo(websocket):
    async for message in websocket:
        print(message)
        # await websocket.send(message)

async def main():
    async with serve(echo, "localhost", 8765):
        await asyncio.get_running_loop().create_future()  # run forever

asyncio.run(main())