import asyncio
import websockets
import json

async def play_game():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        room_id = input("Nhập mã phòng: ")
        await websocket.send(json.dumps({"type": "join", "room": room_id}))

        async def receiver():
            async for message in websocket:
                data = json.loads(message)
                if data["type"] == "move":
                    print(f"Đối thủ đi từ {data['from']} đến {data['to']}")

        asyncio.create_task(receiver())

        while True:
            move = input("Nhập nước đi (vd: 1 2 3 4): ")
            x1, y1, x2, y2 = map(int, move.strip().split())
            await websocket.send(json.dumps({
                "type": "move",
                "from": [x1, y1],
                "to": [x2, y2]
            }))

asyncio.run(play_game())
