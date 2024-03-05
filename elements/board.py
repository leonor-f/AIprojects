# Macro definitions

W = 1
B = 2

class Board:
    def __init__(self, level):
        self.board = self.get_board(level)

    def display(self):
        for row in self.grid:
            print(' '.join(str(cell) for cell in row))

    def fill_cell(self, x, y):
        if 0 <= x < self.rows and 0 <= y < self.cols:
            self.grid[y][x] = 1
        else:
            print("Invalid coordinates")
    
    def empty_cell(self, x, y):
        if 0 <= x < self.rows and 0 <= y < self.cols:
            self.grid[y][x] = 0
        else:
            print("Invalid coordinates")

    # getters

    def get_board(self, level):
        if level == 1:
            self.rows = 5
            self.cols = 6
            return [
                [0, 0, 0, 0, B],
                [W, 0, 0, 0, W],
                [B, W, B, W, B],
                [0, B, W, B, 0],
                [0, W, B, W, 0],
                [0, B, W, B, 0]
            ]
        elif level == 2:
            self.rows = 5
            self.cols = 7
            return [
                [W, 0, W, 0, W],
                [B, 0, B, 0, B],
                [W, 0, W, 0, W],
                [B, 0, B, 0, B],
                [W, 0, W, 0, W],
                [B, W, B, W, B],
                [W, B, W, B, W]
            ]
        elif level == 3:
            self.rows = 8
            self.cols = 9
            return [
                [0, 0, W, 0, 0, 0, 0, 0, 0],
                [B, W, B, W, B, W, B, W, 0],
                [W, 0, W, B, 0, 0, W, B, W],
                [B, W, B, W, B, W, B, 0, B],
                [W, 0, W, B, W, B, W, 0, 0],
                [B, 0, B, W, B, W, B, 0, 0],
                [W, 0, W, B, 0, 0, 0, 0, 0],
                [B, W, B, 0, 0, 0, 0, 0, 0]
            ]
        else:
            pass

    def get_rows(self):
        return self.rows
    
    def get_cols(self):
        return self.cols
    