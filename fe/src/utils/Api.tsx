import type { CreateRoomDTO, JoinRoomDTO } from "@/models/Room";
import { API_CREATE_ROOM, API_GET_BOARD, API_GET_MOVE, API_JOIN_ROOM, API_LOGIN, API_MOVE } from "../defs/Api";
import type { Credentials } from "../models/Credential";
import type { GetBoardDTO, GetMoveDTO } from "@/models/Game";

const baseApiUrl = import.meta.env.VITE_API_URL.replace(/\/+$/, "");

function buildApiUrl(suffix: string) {
    const trimmedSuffix = suffix.replace(/^\/+/, "");
    return `${baseApiUrl}/${trimmedSuffix}`;
}

export async function loginUser(credentials: Credentials) {
    const res = await fetch(buildApiUrl(API_LOGIN), {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(credentials),
    });

    if (!res.ok) throw new Error("Login failed");

    return res.json();
}

export async function getMoves(roomID: number) {
    if (roomID < 0) {
        return null;
    }
    const token = getToken()
    const res = await fetch(buildApiUrl(API_GET_MOVE), {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({
            roomID: roomID,
        }),
    });

    if (!res.ok) {
        throw new Error("Get board fail");
    }

    const boardData: GetMoveDTO = await res.json();
    return boardData;
}

export async function getBoardState(roomID: number) {
    if (roomID < 0) {
        return null;
    }
    const token = getToken()
    const res = await fetch(buildApiUrl(API_GET_BOARD), {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({
            roomID: roomID,
        }),
    });

    if (!res.ok) {
        throw new Error("Get board fail");
    }

    const boardData: GetBoardDTO = await res.json();
    return boardData;
}

export async function move(roomID: number, from: Array<number>, to: Array<number>) {
    const token = getToken()
    const res = await fetch(buildApiUrl(API_MOVE), {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({
            roomID: roomID,
            from: from,
            to: to,
        }),
    });

    if (!res.ok) {
        throw new Error("Move failed")
    }
}

export async function createRoom() {
    const token = getToken()
    const res = await fetch(buildApiUrl(API_CREATE_ROOM), {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({}),
    });

    if (!res.ok) throw new Error("Login failed");

    const roomData: CreateRoomDTO = await res.json();

    return roomData.roomID;
}

export async function joinRoom(roomID: string) {
    if (isNaN(Number(roomID))) {
        throw new Error("Invalid room ID")
    }
    const token = getToken()
    const res = await fetch(buildApiUrl(API_JOIN_ROOM), {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({
            roomID: Number(roomID),
        }),
    });

    if (!res.ok) throw new Error("Join room fail");

    const joinData: JoinRoomDTO = await res.json();

    if (!joinData.status) {
        throw new Error(joinData.message);
    }

    return joinData.status;
}

function getToken() {
    const token = localStorage.getItem("token");
    if (!token) {
        throw new Error("No login token!");
    }
    return token;
}
