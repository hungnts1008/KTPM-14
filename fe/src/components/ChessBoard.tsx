import { useEffect, useRef, useState } from "react";
import Board from "./ChessBoard/Board";
import type { ChessPiece } from "@/models/ChessPiece";
import { getBoardState, getMoves } from "@/utils/Api";
import { Link, useNavigate } from "react-router-dom";
import { HOME_ROUTE } from "@/defs/Routes";
import { Dialog, DialogContent, DialogTitle } from "@radix-ui/react-dialog";
import { DialogFooter } from "./ui/dialog";
import { Button } from "./ui/button";

type ChessBoardProps = {
    roomId: number,
}

export default function ChessBoard({ roomId }: ChessBoardProps) {

    const [pieces, setPieces] = useState(Array<ChessPiece>);
    const [possibleMoves, setPossibleMoves] = useState(Array<Array<number>>);
    const [colorTurn, setColorTurn] = useState("red");
    const [playerTurn, setPlayerTurn] = useState("");
    const [gameEnd, setGameEnd] = useState(false);
    const [playerWin, setPlayerWin] = useState("");
    const lastHashRef = useRef(0);

    const navigate = useNavigate()
    const currentUser = localStorage.getItem("username");

    const fetchMoves = () => {
        getMoves(roomId).then(getMoveDTO => {
            if (!getMoveDTO) {
                return;
            }
            const { possibleMoves } = getMoveDTO;
            setPossibleMoves(possibleMoves);
        })
    }

    const fetchBoard = () => {
        getBoardState(roomId).then(boardState => {
            if (!boardState) {
                return;
            }
            const { board, hashBoard, turn, redSide, blackSide, checkMate } = boardState;
            if (hashBoard != lastHashRef.current) {
                lastHashRef.current = hashBoard;
                setPieces(board);
                setColorTurn(turn);

                if (turn === "red") {
                    setPlayerTurn(redSide);
                } else {
                    setPlayerTurn(blackSide);
                }

                if (checkMate !== "ongoing") {
                    if (checkMate === "red") {
                        setPlayerWin(redSide);
                    } else {
                        setPlayerWin(blackSide);
                    }
                    setGameEnd(true);
                }

                fetchMoves();
            }
        }).catch(() => {
            navigate(HOME_ROUTE)
        });
    }

    useEffect(() => {
        fetchBoard();
        const intervalId = setInterval(fetchBoard, 200);

        return () => {
            clearInterval(intervalId);
        }
    }, [])

    return (
        <>
            <Dialog open={gameEnd}>
                <DialogContent onInteractOutside={(e) => {
                    e.preventDefault();
                }}>
                    <DialogTitle>
                        GAME OVER!
                    </DialogTitle>
                    <DialogContent>
                        {playerWin === currentUser ? "You won!" : "You lost!"}
                    </DialogContent>
                    <DialogFooter>
                        <Button asChild>
                            <Link to={HOME_ROUTE}>Confirm</Link>
                        </Button>
                    </DialogFooter>
                </DialogContent>
            </Dialog>

            <div className="p-[15px] flex flex-col">
                {
                    (roomId >= 0) && <div className="flex items-center justify-center"
                        style={{
                            color: colorTurn,
                        }}
                    >
                        {playerTurn}'s turn
                    </div>
                }
                <div className="flex justify-center items-center">
                    <div className="relative w-[576px] h-[640px]">
                        <Board pieces={pieces} possibleMoves={possibleMoves} roomID={roomId} />
                    </div>
                </div>
            </div>
        </>
    );
}
