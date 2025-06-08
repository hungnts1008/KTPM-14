import type { ChessPiece } from "@/models/ChessPiece";
import Piece from "./Piece";
import { useEffect, useState } from "react";
import { move } from "@/utils/Api";

function isInRiver(row: number) {
    return row == 4;
}

const diagLen = 64 * 2 * Math.sqrt(2);

type BoardProps = {
    pieces: ChessPiece[],
    possibleMoves: Array<Array<number>>,
    roomID: number,
}

export default function Board({ pieces, possibleMoves, roomID }: BoardProps) {

    const [selected, setSelected] = useState<string>("");
    const [highlightedCells, setHighlightedCells] = useState(new Set<string>);
    var pieceMoves = new Map<string, Set<string>>;
    var pieceMap = new Map<string, ChessPiece>

    const piecesComp = pieces.map(piece => {
        const id = `${piece.position.row}${piece.position.col}`;
        var set = new Set<string>;
        pieceMoves.set(id, set);
        piece.id = id;
        pieceMap.set(id, piece)
        return <Piece piece={piece} selected={selected} setSelected={setSelected} moves={set} />
    })

    const handleMove = (after: string) => {
        const from = [Number(selected[0]), Number(selected[1])];
        const to = [Number(after[0]), Number(after[1])]
        move(roomID, from, to);
    }

    possibleMoves.map(move => {
        const key = `${move[0]}${move[1]}`
        const val = `${move[2]}${move[3]}`
        pieceMoves.get(key)?.add(val);
    })

    useEffect(() => {
        const handleClickOutside = () => {
            setSelected("");
        };

        document.addEventListener("click", handleClickOutside);

        const moves = pieceMoves.get(selected);
        if (moves) {
            setHighlightedCells(moves);
        } else {
            setHighlightedCells(new Set<string>);
        }

        return () => {
            document.removeEventListener("click", handleClickOutside);
        };
    }, [selected]);

    return (
        <div>
            {Array.from({ length: 10 }).map((_, r) => {
                return Array.from({ length: 9 }).map((_, c) => (
                    <div
                        className="absolute w-[64px] h-[64px] flex justify-center items-center"
                        style={{
                            left: `${c * 64}px`,
                            top: `${r * 64}px`,
                            // border: '1px solid black'
                        }}
                    >
                        {highlightedCells.has(`${r}${c}`) &&
                            <div
                                className="w-5 h-5 rounded-full bg-rose-400 transition-transform duration-200 hover:scale-110"
                                style={{
                                    zIndex: 1000,
                                }}
                                onClick={() => { handleMove(`${r}${c}`) }}
                            >
                            </div>
                        }
                    </div >
                ))
            })}

            {
                piecesComp
            }

            {
                Array.from({ length: 9 }).map((_, r) => {
                    return Array.from({ length: 8 }).map((_, c) => (
                        <div
                            className={`absolute w-[64px] h-[64px]`}
                            style={{
                                left: `${c * 64 + 32}px`,
                                top: `${r * 64 + 32}px`,
                                border: `${isInRiver(r) ? '' : '2px solid #8F5050'}`,
                                background: `${isInRiver(r) ? '#8F5050' : ''}`
                            }}
                        >
                        </div>
                    ))
                })
            }

            {
                [45, 135].flatMap((deg) =>
                    [95.5, 542.5].map((dr, index) => (
                        <div
                            key={`${deg}-${index}`}
                            className="absolute left-[197.5px]"
                            style={{
                                top: `${dr}px`,
                                width: `${diagLen}px`,
                                border: '1px solid #8F5050',
                                transform: `rotate(${deg}deg)`,
                            }}
                        />
                    ))
                )
            }
        </div>
    );
}
