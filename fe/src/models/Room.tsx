export type CreateRoomDTO = {
    roomID: number,
    message: string,
    side: string,
}

export type JoinRoomDTO = {
    message: string,
    side: string,
    status: boolean,
}
