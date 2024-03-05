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
    
    def move_white_knight(self, new_x, new_y, direction):
        for white_knight in self.white_knights:
            if white_knight.x == new_x and white_knight.y == new_y:
                if direction == 'up' and self.board[new_y - 1][new_x] != 0:
                    white_knight.move(new_x, new_y - 1)
                elif direction == 'left' and self.board[new_y][new_x - 1] != 0:
                    white_knight.move(new_x - 1, new_y)
                elif direction == 'down' and self.board[new_y + 1][new_x] != 0:
                    white_knight.move(new_x, new_y + 1)
                elif direction == 'right' and self.board[new_y][new_x + 1] != 0:
                    white_knight.move(new_x + 1, new_y)
                else:
                    return False
                return True
    
    def check_move_black_knights(self, new_x, new_y):
        for black_knight in self.black_knights:
            if black_knight.x == new_x and black_knight.y == new_y:
                return True
        return False
    
    def check_move_white_knights(self, new_x, new_y):
        for white_knight in self.white_knights:
            if white_knight.x == new_x and white_knight.y == new_y:
                return True
        return False
    
    def check_move(self, new_x, new_y, direction):
        if self.board[new_y][new_x] == 0 or self.check_move_black_knights(new_x, new_y):
            return False
        elif self.check_move_white_knights(new_x, new_y):
            if self.move_white_knight(new_x, new_y, direction):
                return True
            else:
                return False
        else:
            return True

    def check_win(self):
        while True:
            temp_white_knights = self.white_knights.copy()
            temp_black_knights = self.black_knights.copy()

            for white_knight in temp_white_knights:
                if not white_knight.flag:
                    for black_knight in temp_black_knights:
                        if not black_knight.flag:
                            if white_knight.x + 1 == black_knight.x and white_knight.y - 2 == black_knight.y:
                                white_knight.flag = True
                                black_knight.flag = True
                                break
                            elif white_knight.x + 1 == black_knight.x and white_knight.y + 2 == black_knight.y:
                                white_knight.flag = True
                                black_knight.flag = True
                                break
                            elif white_knight.x - 1 == black_knight.x and white_knight.y - 2 == black_knight.y:
                                white_knight.flag = True
                                black_knight.flag = True
                                break
                            elif white_knight.x - 1 == black_knight.x and white_knight.y + 2 == black_knight.y:
                                white_knight.flag = True
                                black_knight.flag = True
                                break
                            elif white_knight.x + 2 == black_knight.x and white_knight.y - 1 == black_knight.y:
                                white_knight.flag = True
                                black_knight.flag = True
                                break
                            elif white_knight.x + 2 == black_knight.x and white_knight.y + 1 == black_knight.y:
                                white_knight.flag = True
                                black_knight.flag = True
                                break
                            elif white_knight.x - 2 == black_knight.x and white_knight.y - 1 == black_knight.y:
                                white_knight.flag = True
                                black_knight.flag = True
                                break
                            elif white_knight.x - 2 == black_knight.x and white_knight.y + 1 == black_knight.y:
                                white_knight.flag = True
                                black_knight.flag = True
                                break
            
            for white_knight in temp_white_knights:
                if not white_knight.flag:
                    return False
            
            for black_knight in temp_black_knights:
                if not black_knight.flag:
                    return False
            
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
