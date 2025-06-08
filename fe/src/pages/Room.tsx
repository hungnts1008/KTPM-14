import ChessBoard from "@/components/ChessBoard";
import { useParams } from "react-router-dom";


export default function Room() {
    const { roomID } = useParams();

    if (!roomID || isNaN(Number(roomID))) {
        return (
            <>
                <div>
                    How did we get here?
                </div>
            </>
        );
    }

    return (
        <>
            <div className="flex flex-col items-center justify-center p-5">
                <div>
                    Room ID: {roomID}
                </div>
                <div className="flex items-center justify-center">
                    <ChessBoard roomId={Number(roomID)} />
                </div>
            </div>
        </>
    );
}
