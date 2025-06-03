import random

class EasyBot:
    """
    Bot cờ tướng cấp độ dễ: chọn ngẫu nhiên một nước đi hợp lệ.
    """

    def __init__(self, game, color):
        """
        game: đối tượng Game hiện tại
        color: màu quân của bot ('red' hoặc 'black')
        """
        self.game = game
        self.color = color

    def get_all_valid_moves(self):
        """
        Lấy tất cả các nước đi hợp lệ cho bot.
        Trả về: [(piece, move), ...]
        """
        moves = []
        for piece in self.game.board.get_pieces(self.color):
            valid_moves = piece.get_valid_moves(self.game.board)
            for move in valid_moves:
                moves.append((piece, move))
        return moves

    def make_move(self):
        """
        Thực hiện một nước đi ngẫu nhiên.
        """
        moves = self.get_all_valid_moves()
        if not moves:
            return False  # Không còn nước đi
        piece, move = random.choice(moves)
        self.game.move_piece(piece, move)
        return True