import ChessBoard from "@/components/ChessBoard";
import { Button } from "@/components/ui/button";
import { Dialog, DialogContent, DialogDescription, DialogTitle } from "@/components/ui/dialog";
import { Input } from "@/components/ui/input";
import { ROOM_ROUTE } from "@/defs/Routes";
import { createRoom, joinRoom } from "@/utils/Api";
import { useState } from "react";
import { generatePath, useNavigate } from "react-router-dom";

export default function Home() {
    const [createRoomFailed, setCreateRoomFailed] = useState(false);
    const [joinRoomFailed, setJoinRoomFailed] = useState(false);
    const [noRoomId, setNoRoomId] = useState(false);
    const [roomId, setRoomId] = useState("");

    const navigate = useNavigate();

    const createRoomHandle = () => {
        createRoom().then(id => {
            const path = generatePath(ROOM_ROUTE, { roomID: String(id) });
            navigate(path);
        }).catch(() => {
            setCreateRoomFailed(true);
        })
    }

    const joinRoomHandle = () => {
        if (roomId === "") {
            setNoRoomId(true);
        } else {
            joinRoom(roomId).then(joined => {
                if (!joined) {
                    setRoomId("");
                    setJoinRoomFailed(true);
                } else {
                    const path = generatePath(ROOM_ROUTE, { roomID: roomId });
                    navigate(path);
                }
            }).catch(() => {
                setRoomId("");
                setJoinRoomFailed(true);
            })
        }
    }

    return (
        <div className="flex items-center justify-center">
            <Dialog open={createRoomFailed} onOpenChange={setCreateRoomFailed}>
                <DialogContent>
                    <DialogTitle>Create room failed!</DialogTitle>
                    <DialogDescription>
                        The server failed to create a room, try again later.
                    </DialogDescription>
                </DialogContent>
            </Dialog>

            <Dialog open={joinRoomFailed} onOpenChange={setJoinRoomFailed}>
                <DialogContent>
                    <DialogTitle>Join room failed!</DialogTitle>
                    <DialogDescription>
                        Failed to join room, make sure the room ID is valid.
                    </DialogDescription>
                </DialogContent>
            </Dialog>

            <Dialog open={noRoomId} onOpenChange={setNoRoomId}>
                <DialogContent>
                    <DialogTitle>No room ID provided!</DialogTitle>
                    <DialogDescription>
                        Please provide a room ID.
                    </DialogDescription>
                </DialogContent>
            </Dialog>

            <ChessBoard roomId={-1} />

            <div className="flex flex-col gap-10">
                <Button onClick={createRoomHandle}>
                    Create room!
                </Button>

                <div className="flex items-center w-full">
                    <div className="flex-grow border-t border-gray-300"></div>
                    <span className="mx-4 text-gray-500 text-sm whitespace-nowrap">or</span>
                    <div className="flex-grow border-t border-gray-300"></div>
                </div>

                <div className="flex items-center gap-2">
                    <Input type="text" placeholder="Enter Room ID" id="room-input" onChange={(e) => { setRoomId(e.target.value) }} />
                    <Button onClick={joinRoomHandle}>
                        Join!
                    </Button>
                </div>
            </div>
        </div>
    )
}
