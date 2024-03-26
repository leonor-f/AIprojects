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
    self.board = self.get_board(level)
  
  def get_board(self, level):
    if level == 0:
      return [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, W, B, W, B, W, 0, 0],
        [0, 0, B, W, B, W, B, 0, 0],
        [0, 0, W, B, W, B, W, 0, 0],
        [0, 0, B, W, BW, W, BB, 0, 0],
        [0, 0, W, B, WK, B, W, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
      ]
    elif level == 1:
      return [
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
    elif level == 2:
      return [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, WB, 0, W, 0, W, 0, 0],
        [0, 0, B, 0, B, 0, BB, 0, 0],
        [0, 0, W, 0, W, 0, W, 0, 0],
        [0, 0, B, 0, B, 0, B, 0, 0],
        [0, 0, W, 0, W, 0, W, 0, 0],
        [0, 0, B, WW, B, WW, B, 0, 0],
        [0, 0, W, B, WK, B, W, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
      ]
    elif level == 3:
      return [
        [0, 0, WB, 0, 0, 0, 0, 0, 0],
        [BB, W, B, W, B, W, BW, WK, 0],
        [0, 0, W, B, 0, 0, W, B, W],
        [B, W, B, W, B, WW, B, 0, BB],
        [W, 0, W, B, W, B, W, 0, 0],
        [B, 0, B, WW, B, W, B, 0, 0],
        [W, 0, W, B, 0, 0, 0, 0, 0],
        [B, W, B, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
      ]
    elif level == 4:
      return [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, B, 0, 0, 0, 0],
        [0, 0, W, 0, WK, B, W, B, W],
        [0, W, B, W, B, WW, BW, W, B],
        [0, 0, W, B, WB, B, WB, B, W],
        [0, 0, B, W, B, W, B, W, B],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
      ]
    else:
      pass

