export type Position = {
    row: number;
    col: number;
}

export type ChessPiece = {
    id: string;
    piece: 'king' | 'advisor' | 'elephant' | 'horse' | 'rook' | 'cannon' | 'pawn';
    color: 'red' | 'black';
    position: Position;
}
