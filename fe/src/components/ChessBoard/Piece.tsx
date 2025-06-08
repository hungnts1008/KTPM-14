import type { ChessPiece } from "@/models/ChessPiece"
import { pieceSymbols } from "@/defs/ChessPiece";
import type React from "react";

type PieceProps = {
    piece: ChessPiece;
    selected: string;
    setSelected: React.Dispatch<React.SetStateAction<string>>;
    moves: Set<string>;
}

export default function Piece({ piece, selected, setSelected, moves }: PieceProps) {
    const isSelected = piece.id == selected;

    const handleClick = (e: React.MouseEvent<HTMLDivElement>) => {
        e.stopPropagation();
        if (isSelected || moves.size == 0) {
            setSelected("")
        } else {
            setSelected(piece.id);
        }
    }

    return (
        <>
            <div
                className="absolute w-[64px] h-[64px] flex items-center justify-center transition-transform duration-200 hover:scale-105"
                style={{
                    top: `${piece.position.row * 64}px`,
                    left: `${piece.position.col * 64}px`,
                    zIndex: 999,
                }}
                onClick={handleClick}
            >
                <div
                    className={`w-12 h-12 rounded-full bg-[#F2F0DF] 
                                flex items-center justify-center`}
                    style={{
                        boxShadow: "0 0 2px rgba(0,0,0,0.1),0 0 6px rgba(0,0,0,0.2),0 0 12px rgba(0,0,0,0.3)",
                        scale: `${isSelected ? 1.2 : 1}`,
                    }}
                >
                    <div
                        className="w-10 h-10 rounded-full flex items-center justify-center select-none"
                        style={{
                            color: `${piece.color}`,
                            border: `2px solid ${piece.color}`,
                            fontWeight: "bolder",
                        }}>
                        {pieceSymbols[piece.color][piece.piece]}
                    </div>
                </div>
            </div>
        </>
    );
}
