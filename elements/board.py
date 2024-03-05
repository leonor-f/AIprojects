from elements.knight import Knight
from elements.king import King

W = 1
B = 2

class Board:
    def __init__(self, level):
        self.white_knights = self.get_white_knights(level)
        self.black_knights = self.get_black_knights(level)
        self.board = self.get_board(level)
        self.white_king = self.get_white_king(level)

    def check_move(self, piece, new_x, new_y):
        if self.board[new_y][new_x] == 0:
            return False
        else:
            return True
    # setters
    def set_white_knights(self, white_knights):
        self.white_knights = white_knights
    
    def set_black_knights(self, black_knights):
        self.black_knights = black_knights
    
    def set_white_king(self, white_king):
        self.white_king = white_king

    # getters

    def get_board(self, level):
        white_knights = []
        black_knights = []

        if level == 1:
            board = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, B, 0, 0],
                [0, 0, W, 0, 0, 0, W, 0, 0],
                [0, 0, B, W, B, W, B, 0, 0],
                [0, 0, 0, B, W, B, 0, 0, 0],
                [0, 0, 0, W, B, W, 0, 0, 0],
                [0, 0, 0, B, W, B, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]

            return board
        elif level == 2:
            return [
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, W, 0, W, 0, W, 0, 0],
                [0, 0, B, 0, B, 0, B, 0, 0],
                [0, 0, W, 0, W, 0, W, 0, 0],
                [0, 0, B, 0, B, 0, B, 0, 0],
                [0, 0, W, 0, W, 0, W, 0, 0],
                [0, 0, B, W, B, W, B, 0, 0],
                [0, 0, W, B, W, B, W, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]
        elif level == 3:
            return [
                [0, 0, W, 0, 0, 0, 0, 0, 0],
                [B, W, B, W, B, W, B, W, 0],
                [W, 0, W, B, 0, 0, W, B, W],
                [B, W, B, W, B, W, B, 0, B],
                [W, 0, W, B, W, B, W, 0, 0],
                [B, 0, B, W, B, W, B, 0, 0],
                [W, 0, W, B, 0, 0, 0, 0, 0],
                [B, W, B, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]
        else:
            pass

    def get_white_king(self, level):
        if level == 1:
            return King(4, 4, "img/white_king.png")
        elif level == 2:
            return King(4, 7, "img/white_king.png")
        elif level == 3:
            return King(2, 2, "img/white_king.png")
        else:
            pass
    
    def get_white_knights(self, level):
        white_knights = []
        if level == 1:
            for x, y in [(3, 5), (5, 4)]:
                white_knights.append(Knight(x, y, "img/white_knight.png"))
        elif level == 2:
            for x, y in [(3, 6), (5, 6)]:
                white_knights.append(Knight(x, y, "img/white_knight.png"))
        elif level == 3:
            pass
        else:
            pass
        return white_knights

    def get_black_knights(self, level):
        black_knights = []
        if level == 1:
            for x, y in [(2, 2), (6, 1)]:
                black_knights.append(Knight(x, y, "img/black_knight.png"))
        elif level == 2:
            for x, y in [(2, 1), (6, 2)]:
                black_knights.append(Knight(x, y, "img/black_knight.png"))
        elif level == 3:
            pass
        else:
            pass
        return black_knights
