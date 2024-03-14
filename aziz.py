import asyncio
import websockets
import threading

def input_thread(loop, websocket):
    while True:
        message = input("Enter a message: ")
        asyncio.run_coroutine_threadsafe(websocket.send(message), loop)

async def client():
    uri = "ws://localhost:8000/ws/test"
    async with websockets.connect(uri) as websocket:
        threading.Thread(target=input_thread, args=(asyncio.get_event_loop(), websocket)).start()
        while True:
            message = await websocket.recv()
            print(f"Received message: {message}")

asyncio.run(client())