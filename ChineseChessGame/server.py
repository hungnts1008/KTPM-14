import asyncio
import websockets
import json

rooms = {}  # room_id -> [player1, player2]

async def handler(websocket):
    print("New client connected")
    room_id = None

    try:
        async for message in websocket:
            data = json.loads(message)

            # Lệnh tạo/join phòng
            if data["type"] == "join":
                room_id = data["room"]
                if room_id not in rooms:
                    rooms[room_id] = []
                rooms[room_id].append(websocket)

                # Thông báo số người chơi trong phòng
                await websocket.send(json.dumps({"type": "joined", "players": len(rooms[room_id])}))

            # Lệnh gửi nước đi
            elif data["type"] == "move":
                # Gửi nước đi cho đối thủ
                for player in rooms.get(room_id, []):
                    if player != websocket:
                        await player.send(json.dumps({
                            "type": "move",
                            "from": data["from"],
                            "to": data["to"],
                        }))

    except websockets.ConnectionClosed:
        print("Client disconnected")
        if room_id and websocket in rooms.get(room_id, []):
            rooms[room_id].remove(websocket)

async def main():
    async with websockets.serve(handler, "localhost", 8765):
        print("Server started on ws://localhost:8765")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())
