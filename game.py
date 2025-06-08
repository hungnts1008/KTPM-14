from flask import Blueprint, request, jsonify
from auth import token_required
from logic import hash_board

game_bp = Blueprint("game", __name__)


@game_bp.route("/move", methods=["POST"])
@token_required
def move(current_user):
    from room import rooms
    from logic import calculate_possible_moves
    from logic import isCheckMate
    from logic import full_name_piece


    data = request.json
    fromPos = data.get("from")
    toPos = data.get("to")
    roomID = data.get("roomID")

    if roomID not in rooms:
        return jsonify({"message": "Room not found"}), 404
    pieceAtBeforePosition = rooms[roomID]["board"][int(fromPos[0])][int(fromPos[1])]
    pieceAtAfterPosition = rooms[roomID]["board"][int(toPos[0])][int(toPos[1])]
    checkValidMove = (int(fromPos[0]), int(fromPos[1]), int(toPos[0]), int(toPos[1]))
    checkTurn = (
        pieceAtBeforePosition.isupper() and rooms[roomID]["turn"] == "black"
    ) or (pieceAtBeforePosition.islower() and rooms[roomID]["turn"] == "red")

    redPlayer = None
    blackPlayer = None
    for player in rooms[roomID]["players"]:
        if player[1] == "red":
            redPlayer = player[0]
        elif player[1] == "black":
            blackPlayer = player[0]

    if checkValidMove in rooms[roomID]["possibleMoves"] and checkTurn == True:
        rooms[roomID]["board"][int(toPos[0])][int(toPos[1])] = pieceAtBeforePosition
        rooms[roomID]["board"][int(fromPos[0])][int(fromPos[1])] = "."
        rooms[roomID]["historyMoves"].append({"from": fromPos, "to": toPos})
        rooms[roomID]["possibleMoves"] = calculate_possible_moves(
            rooms[roomID]["board"], "black" if rooms[roomID]["turn"] == "red" else "red"
        )
        rooms[roomID]["turn"] = "black" if rooms[roomID]["turn"] == "red" else "red"
        checkmate = isCheckMate(rooms[roomID]["board"])
        if checkmate != 0:
            rooms[roomID]["gameOver"] = True
            checkmate = "red" if checkmate == 1 else "black"
        else:
            checkmate = "ongoing"

        board = rooms[roomID]["board"]
        exportedBoard = []
        for row in range(len(board)):
            for col in range(len(board[row])):
                piece = board[row][col]
                if piece == ".":
                    continue
                exportedBoard.append(
                    {
                        "piece": full_name_piece(piece),
                        "position": {
                            "row": row,
                            "col": col,
                        },
                        "color": "red" if piece.islower() else "black",
                    }
                )

        rooms[roomID]["hashBoard"] = hash_board(rooms[roomID]["board"])
        return (
            jsonify(
                {
                    "message": "Move successful",
                    "status": True,
                    "board": exportedBoard,
                    "turn": rooms[roomID]["turn"],
                    "checkMate": checkmate,
                    "historyMoves": rooms[roomID]["historyMoves"],
                    "redSide": redPlayer,
                    "blackSide": blackPlayer,
                    "hashBoard": rooms[roomID]["hashBoard"],
                }
            ),
            200,
        )
    else:
        return (
            jsonify(
                {
                    "message": "Invalid move",
                    "status": False,
                    "board": rooms[roomID]["board"],
                    "turn": rooms[roomID]["turn"],
                    "redSide": redPlayer,
                    "blackSide": blackPlayer,
                }
            ),
            400,
        )


@game_bp.route("/get_board", methods=["POST"])
@token_required
def get_board(current_user):
    data = request.json
    roomID = data.get("roomID")
    from room import rooms
    from logic import full_name_piece

    if roomID not in rooms:
        return jsonify({"message": "Room not found"}), 404
    board = rooms[roomID]["board"]

    exportedBoard = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            piece = board[row][col]
            if piece == ".":
                continue
            exportedBoard.append(
                {
                    "piece": full_name_piece(piece),
                    "position": {
                        "row": row,
                        "col": col,
                    },
                    "color": "red" if piece.islower() else "black",
                }
            )
    redPlayer = None
    blackPlayer = None
    for player in rooms[roomID]["players"]:
        if player[1] == "red":
            redPlayer = player[0]
        elif player[1] == "black":
            blackPlayer = player[0]
    return (
        jsonify(
            {
                "message": "Board retrieved successfully",
                "roomID": roomID,
                "board": exportedBoard,
                "turn": rooms[roomID]["turn"],
                "checkMate": rooms[roomID]["checkMate"],
                "redSide": redPlayer,
                "blackSide": blackPlayer,
                "hashBoard": rooms[roomID]["hashBoard"],
                "historyMoves": rooms[roomID]["historyMoves"],
            }
        ),
        200,
    )


@game_bp.route("/get_move", methods=["POST"])
@token_required
def get_possible_move(current_user):
    from logic import calculate_possible_moves

    data = request.json
    roomID = data.get("roomID")
    from room import rooms

    if roomID not in rooms:
        return jsonify({"message": "Room not found"}), 404
    board = rooms[roomID]["board"]
    playerSide = None
    for player in rooms[roomID]["players"]:
        if player[0] == current_user:
            playerSide = player[1]
    possible_moves = calculate_possible_moves(board, playerSide)
    return (
        jsonify(
            {
                "roomID": roomID,
                "possibleMoves": possible_moves,
                "hashBoard": rooms[roomID]["hashBoard"],
                "turn": rooms[roomID]["turn"],
            }
        ),
        200,
    )
