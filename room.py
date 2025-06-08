from flask import Blueprint, request, jsonify
from auth import token_required

rooms = {}

room_bp = Blueprint("room", __name__)


def mexRoomID(rooms):
    for ID in range(10000):
        if ID not in rooms:
            return ID


def init_board():
    """
    K: King: Tướng
    A: Advisor: Sĩ
    E: Elephant: Tượng
    H: Horse: Mã
    R: Rook: Xe
    C: Cannon: Pháo
    P: Pawn: Tốt
    Uppercase letters represent black pieces, lowercase letters represent red pieces.
    The board is represented as a 2D list with 10 rows and 9 columns.
    """
    return [
        ["R", "H", "E", "A", "K", "A", "E", "H", "R"],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", "C", ".", ".", ".", ".", ".", "C", "."],
        ["P", ".", "P", ".", "P", ".", "P", ".", "P"],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ["p", ".", "p", ".", "p", ".", "p", ".", "p"],
        [".", "c", ".", ".", ".", ".", ".", "c", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ["r", "h", "e", "a", "k", "a", "e", "h", "r"],
    ]


@room_bp.route("/create_room", methods=["POST"])
@token_required
def create_room(current_user):
    from logic import calculate_possible_moves, hash_board

    roomID = mexRoomID(rooms)
    board = init_board()
    hashBoard = hash_board(board)
    rooms[roomID] = {
        "players": [(current_user, "red")],
        "board": board,
        "turn": "red",
        "historyMoves": [],
        "possibleMoves": calculate_possible_moves(board, "red"),
        "gameOver": False,
        "checkMate": "ongoing",
        "hashBoard": hashBoard,
    }
    return (
        jsonify(
            {
                "roomID": roomID,
                "message": f"Room created by {current_user}",
                "side": "red",
            }
        ),
        201,
    )


@room_bp.route("/join_room", methods=["POST"])
@token_required
def join_room(current_user):
    data = request.json
    roomID = data.get("roomID")
    if roomID is None:
        return jsonify({"message": "Room ID is required"}), 400

    accepted = False
    if roomID in rooms:
        if len(rooms[roomID]["players"]) < 2:
            if current_user in [player[0] for player in rooms[roomID]["players"]]:
                return (
                    jsonify(
                        {
                            "message": f"{current_user} is already in room {roomID}",
                            "status": True,
                        }
                    ),
                    200,
                )
            rooms[roomID]["players"].append((current_user, "black"))
            accepted = True
            return (
                jsonify(
                    {
                        "message": f"{current_user} joined room {roomID}",
                        "status": accepted,
                        "side": (
                            "black" if len(rooms[roomID]["players"]) == 2 else "red"
                        ),
                    }
                ),
                200,
            )
        else:
            if current_user in [player[0] for player in rooms[roomID]["players"]]:
                accepted = True
                return (
                    jsonify(
                        {
                            "message": f"{current_user} is already in room {roomID}",
                            "status": accepted,
                        }
                    ),
                    200,
                )
            return jsonify({"message": "Room is full", "status": accepted}), 400
    else:
        return jsonify({"message": "Room does not exist", "status": accepted}), 404


@room_bp.route("/room_created", methods=["GET"])
@token_required
def room_created(current_user):
    roomID = request.json.get("roomID")
    if roomID is None:
        return jsonify({"message": "Room ID is required"}), 400
    if roomID in rooms:
        return jsonify({"roomID": roomID, "status": True}), 200
    else:
        return jsonify({"roomID": roomID, "status": False}), 404
