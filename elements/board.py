from elements.knight import Knight
from elements.king import King

W = 1 # white square
B = 2 # black square
WW = 3 # white square and white knight
WB = 4 # white square and black knight
BW = 5 # black square and white knight
BB = 6 # black square and black knight
WK = 7 # white square and king
BK = 8 # black square and king

class Board:
    def __init__(self, level):
        self.rows = 9
        self.cols = 9
        self.board = self.get_board(level)
    
    # getters

    def get_board(self, level):
        if level == 1:
            board = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, BB, 0, 0],
                [0, 0, WB, 0, 0, 0, W, 0, 0],
                [0, 0, B, W, B, W, B, 0, 0],
                [0, 0, 0, B, W, BW, 0, 0, 0],
                [0, 0, 0, W, BW, WK, 0, 0, 0],
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
                [0, 0, W, B, 0, 0, W, B, W],
                [B, W, B, W, B, W, B, 0, B],
                [W, 0, W, B, W, B, W, 0, 0],
                [B, 0, B, W, B, W, B, 0, 0],
                [W, 0, W, B, 0, 0, 0, 0, 0],
                [B, W, B, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]
        else:
            pass


'''
    def get_white_king(self, level):
        if level == 1:
            return King(4, 4, "img/white_king.png")
        elif level == 2:
            return King(4, 7, "img/white_king.png")
        elif level == 3:
            return King(2, 5, "img/white_king.png")
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
            for x, y in [(3, 5), (7, 1), (2, 2)]:
                white_knights.append(Knight(x, y, "img/white_knight.png"))
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
            for x, y in [(2, 0), (0, 1), (8, 3)]:
                black_knights.append(Knight(x, y, "img/black_knight.png"))
        else:
            pass
        return black_knights
'''
