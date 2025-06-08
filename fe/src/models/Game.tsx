import type { ChessPiece } from "./ChessPiece"

export type GetBoardDTO = {
    blackSide: string,
    redSide: string,
    board: ChessPiece[],
    message: string,
    roomID: number,
    turn: "red" | "black",
    hashBoard: number,
    checkMate: "red" | "black" | "ongoing",
}

export type GetMoveDTO = {
    possibleMoves: Array<Array<number>>,
    roomID: number,
    turn: "red" | "black",
    hashBoard: number,
}
