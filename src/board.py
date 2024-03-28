from macros import *

class Board:
  def __init__(self, level):
    self.board = self.get_board(level)
  
  def get_board(self, level):
    if level == 0:
      return [
        [N, N, N, N, N, N, N, N, N],
        [N, N, N, N, N, N, N, N, N],
        [N, N, W, B, W, B, W, N, N],
        [N, N, BK, WW, B, W, B, N, N],
        [N, N, W, B, W, B, W, N, N],
        [N, N, B, W, B, W, BB, N, N],
        [N, N, W, B, W, B, W, N, N],
        [N, N, N, N, N, N, N, N, N],
        [N, N, N, N, N, N, N, N, N],
      ]
    elif level == 1:
      return [
        [N, N, N, N, N, N, N, N, N],
        [N, N, N, N, N, N, BB, N, N],
        [N, N, WB, N, N, N, W, N, N],
        [N, N, B, W, B, W, B, N, N],
        [N, N, N, B, W, BW, N, N, N],
        [N, N, N, W, BW, WK, N, N, N],
        [N, N, N, B, W, B, N, N, N],
        [N, N, N, N, N, N, N, N, N],
        [N, N, N, N, N, N, N, N, N]
      ]
    elif level == 2:
      return [
        [N, N, N, N, N, N, N, N, N],
        [N, N, WB, N, W, N, W, N, N],
        [N, N, B, N, B, N, BB, N, N],
        [N, N, W, N, W, N, W, N, N],
        [N, N, B, N, B, N, B, N, N],
        [N, N, W, N, W, N, W, N, N],
        [N, N, B, WW, B, WW, B, N, N],
        [N, N, W, B, WK, B, W, N, N],
        [N, N, N, N, N, N, N, N, N]
      ]
    elif level == 3:
      return [
        [N, N, WB, N, N, N, N, N, N],
        [BB, W, B, W, B, W, BW, WK, N],
        [N, N, W, B, N, N, W, B, W],
        [B, W, B, W, B, WW, B, N, BB],
        [W, N, W, B, W, B, W, N, N],
        [B, N, B, WW, B, W, B, N, N],
        [W, N, W, B, N, N, N, N, N],
        [B, W, B, N, N, N, N, N, N],
        [N, N, N, N, N, N, N, N, N]
      ]
    elif level == 4:
      return [
        [N, N, N, N, N, N, N, N, N],
        [N, N, N, N, N, N, N, N, N],
        [N, N, N, N, B, N, N, N, N],
        [N, N, W, N, WK, B, W, B, W],
        [N, W, B, W, B, WW, BW, W, B],
        [N, N, W, B, WB, B, WB, B, W],
        [N, N, B, W, B, W, B, W, B],
        [N, N, N, N, N, N, N, N, N],
        [N, N, N, N, N, N, N, N, N]
      ]
    else:
      return []