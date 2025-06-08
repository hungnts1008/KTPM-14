def calculate_possible_moves(board, playerSide):
    possible_moves = []

    for row in range(len(board)):
        for col in range(len(board[row])):
            piece = board[row][col]
            if piece != "." and getColor(piece) == playerSide:
                moves = get_piece_moves(board, row, col)
            else:
                continue
            for move in moves:
                tempBoard = [list(r) for r in board]
                tempBoard[row][col] = "."
                tempBoard[move[0]][move[1]] = piece
                kingPos = find_king(tempBoard, playerSide)
                if getColor(piece) == playerSide:
                    if not isCheck(tempBoard, kingPos[0], kingPos[1]):
                        possible_moves.append((row, col, move[0], move[1]))
    return possible_moves


def full_name_piece(piece):
    if piece.isupper():
        return {
            "R": "rook",
            "H": "horse",
            "E": "elephant",
            "A": "advisor",
            "K": "king",
            "C": "cannon",
            "P": "pawn",
        }[piece]
    else:
        return {
            "r": "rook",
            "h": "horse",
            "e": "elephant",
            "a": "advisor",
            "k": "king",
            "c": "cannon",
            "p": "pawn",
        }[piece]


def get_piece_moves(board, row, col):
    piece = board[row][col]
    if piece == "R" or piece == "r":
        return get_rook_moves(board, row, col)
    elif piece == "H" or piece == "h":
        return get_horse_moves(board, row, col)
    elif piece == "E" or piece == "e":
        return get_elephant_moves(board, row, col)
    elif piece == "A" or piece == "a":
        return get_advisor_moves(board, row, col)
    elif piece == "K" or piece == "k":
        return get_king_moves(board, row, col)
    elif piece == "C" or piece == "c":
        return get_canon_moves(board, row, col)
    elif piece == "P" or piece == "p":
        return get_pawn_moves(board, row, col)
    else:
        return []


def get_pawn_moves(board, row, col):
    # chinese chess pawn movement logic
    moves = []
    piece = board[row][col]
    direction = 1 if piece.isupper() else -1
    river_line = 5 if piece.isupper() else 4

    if row + direction >= 0 and row + direction < len(board):
        if (
            board[row + direction][col] == "."
            or board[row + direction][col].isupper() != piece.isupper()
        ):
            moves.append((row + direction, col))

    if piece.isupper() and row >= river_line:
        if col - 1 >= 0:
            if (
                board[row][col - 1] == "."
                or board[row][col - 1].isupper() != piece.isupper()
            ):
                moves.append((row, col - 1))
        if col + 1 < len(board[row]):
            if (
                board[row][col + 1] == "."
                or board[row][col + 1].isupper() != piece.isupper()
            ):
                moves.append((row, col + 1))

    if piece.islower() and row <= river_line:
        if col - 1 >= 0:
            if (
                board[row][col - 1] == "."
                or board[row][col - 1].isupper() != piece.isupper()
            ):
                moves.append((row, col - 1))
        if col + 1 < len(board[row]):
            if (
                board[row][col + 1] == "."
                or board[row][col + 1].isupper() != piece.isupper()
            ):
                moves.append((row, col + 1))
    return moves


def get_canon_moves(board, row, col):
    # chinese chess canon movement logic
    piece = board[row][col]
    moves = []
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    jumped = False

    for dr, dc in directions:
        jumped = False
        r, c = row + dr, col + dc
        while 0 <= r < len(board) and 0 <= c < len(board[r]):
            if board[r][c] == ".":
                if not jumped:
                    moves.append((r, c))
                else:
                    r += dr
                    c += dc
                    continue
            elif board[r][c].isupper() != piece.isupper():
                if jumped == True:
                    moves.append((r, c))
                    break
                else:
                    jumped = True
            else:
                break
            r += dr
            c += dc
    return moves


def get_rook_moves(board, row, col):
    # chinese chess rook movement logic
    piece = board[row][col]
    moves = []
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for dr, dc in directions:
        r, c = row + dr, col + dc
        while 0 <= r < len(board) and 0 <= c < len(board[r]):
            if board[r][c] == ".":
                moves.append((r, c))
                r += dr
                c += dc
            elif board[r][c].isupper() != piece.isupper():
                moves.append((r, c))
                break
            else:
                break
    return moves


def get_horse_moves(board, row, col):
    # chinese chess horse movement logic
    piece = board[row][col]
    moves = []
    directions = [
        (2, 1),
        (2, -1),
        (-2, 1),
        (-2, -1),
        (1, 2),
        (1, -2),
        (-1, 2),
        (-1, -2),
    ]
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < len(board) and 0 <= c < len(board[r]):
            if board[r][c] == "." or board[r][c].isupper() != piece.isupper():
                if dr == 2 or dr == -2:
                    # check if the front of the horse has a obstacle or not
                    if board[row + dr // 2][col] == ".":
                        moves.append((r, c))
                elif dc == 2 or dc == -2:
                    # check if the front of the horse has a obstacle or not
                    if board[row][col + dc // 2] == ".":
                        moves.append((r, c))
    return moves


def get_elephant_moves(board, row, col):
    # chinese chess elephant movement logic
    piece = board[row][col]
    moves = []
    directions = [(2, 2), (2, -2), (-2, 2), (-2, -2)]
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < len(board) and 0 <= c < len(board[r]):
            if board[r][c] == "." or board[r][c].isupper() != piece.isupper():
                if board[row + dr // 2][col + dc // 2] == ".":
                    moves.append((r, c))
    return moves


def get_advisor_moves(board, row, col):
    # chinese chess advisor movement logic
    piece = board[row][col]
    moves = []
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < len(board) and 0 <= c < len(board[r]):
            if board[r][c] == "." or board[r][c].isupper() != piece.isupper():
                if (piece.islower() and r >= 7 and c >= 3 and c <= 5) or (
                    piece.isupper() and r <= 2 and c >= 3 and c <= 5
                ):
                    moves.append((r, c))
    return moves


def get_king_moves(board, row, col):
    # chinese chess king movement logic
    piece = board[row][col]
    moves = []
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < len(board) and 0 <= c < len(board[r]):
            if board[r][c] == "." or board[r][c].isupper() != piece.isupper():
                if (piece.islower() and r >= 7 and c >= 3 and c <= 5) or (
                    piece.isupper() and r <= 2 and c >= 3 and c <= 5
                ):
                    if isCheck(board, r, c) == False:
                        moves.append((r, c))
    return moves


def isCheck(board, row, col):
    # Check if the king is in check
    another_king = "k" if board[row][col].isupper() else "K"
    pos_another_king = None
    checked = False
    print("Checking if the king is in check at position:", (row, col))

    piece = board[row][col]

    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == another_king:
                pos_another_king = (r, c)
                break

    for r in range(len(board)):
        for c in range(len(board[r])):
            if (
                board[r][c] != "."
                and board[r][c].isupper() != piece.isupper()
                and board[r][c] != another_king
            ):
                moves = get_piece_moves(board, r, c)
                print("Possible moves for piece at", (r, c), ":", moves)
                if (row, col) in moves:
                    checked = True
                    break

    if pos_another_king[1] == col:
        # Check if the king is in check by rook or canon
        ct = 0
        for r in range(
            min(pos_another_king[0], row) + 1, max(pos_another_king[0], row)
        ):
            if board[r][col] != ".":
                ct += 1
        if ct == 0:
            checked = True

    return checked


def isCheckMate(board):
    # red win if return 1, black win if return -1, game is still ongoing if return 0
    if not calculate_possible_moves(board, "red"):
        return -1
    elif not calculate_possible_moves(board, "black"):
        return 1
    else:
        return 0


def getColor(piece):
    if piece.isupper():
        return "black"
    else:
        return "red"


def hash_board(board):
    return hash("".join("".join(row) for row in board))


def find_king(board, playerSide):
    king_char = "K" if playerSide == "black" else "k"
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == king_char:
                return (r, c)
    return None
