from macros import *

class Board:
  def __init__(self, level):
    self.board = self.get_board(level)
  
  def get_board(self, level):
    if level == 1:
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
        [N, N, N, N, N, N, N, N, N],
        [N, N, N, N, B, N, N, N, N],
        [N, N, W, N, WK, B, W, B, W],
        [N, W, B, W, B, WW, BW, W, B],
        [N, N, W, B, WB, B, WB, B, W],
        [N, N, B, W, B, W, B, W, B],
        [N, N, N, N, N, N, N, N, N],
        [N, N, N, N, N, N, N, N, N]
      ]
    elif level == 3:
      return [
        [N, N, WB, N, N, N, N, N, N],
        [B, W, B, W, B, W, BW, WK, N],
        [N, N, W, B, N, N, W, B, WB],
        [B, W, B, W, B, WW, B, N, B],
        [WB, N, W, B, W, B, W, N, N],
        [B, N, B, WW, B, W, B, N, N],
        [W, N, W, B, N, N, N, N, N],
        [B, W, B, N, N, N, N, N, N],
        [N, N, N, N, N, N, N, N, N]
      ]
    elif level == 4:
      return [
        [N, N, N, N, N, N, N, N, N],
        [N, N, B, W, B, W, B, W, N],
        [N, N, W, N, N, BW, W, BW, N],
        [N, N, B, N, BB, W, BW, W, BB],
        [N, N, W, N, N, B, W, B, W],
        [BK, WW, B, W, B, W, B, W, BB],
        [N, N, N, N, N, N, W, B, W],
        [N, N, N, N, N, N, BB, W, B],
        [N, N, N, N, N, N, N, N, N]
      ]
    elif level == 5:
      return [
        [N, N, N, N, N, N, N, N, N],
        [N, N, N, N, N, N, N, N, N],
        [N, N, N, N, N, N, N, WB, N],
        [N, N, N, N, N, N, W, B, W],
        [B, W, B, W, N, N, B, W, B],
        [N, B, N, B, WK, BW, WW, N, WB],
        [B, WW, BB, W, N, N, B, W, B],
        [WB, B, W, B, W, B, W, BW, W],
        [N, N, N, N, N, N, N, N, N]
      ]
    elif level == 6:
      return [
        [N, N, N, N, WB, B, N, N, N],
        [N, N, N, N, N, W, N, N, N],
        [N, N, W, BB, W, B, W, BW, WK],
        [N, N, N, W, B, N, N, W, N],
        [N, B, W, B, W, B, WW, B, N],
        [N, W, N, W, B, W, B, W, N],
        [N, B, N, B, WW, BB, W, B, N],
        [N, W, N, W, B, N, N, N, N],
        [N, B, W, B, N, N, N, N, N]
      ]
    elif level == 7:
      return [
        [N, N, N, N, N, N, N, N, N],
        [N, N, WB, B, WB, N, N, N, N],
        [N, N, B, W, B, W, N, N, N],
        [N, N, N, BW, W, BW, W, B, N],
        [N, W, BW, W, B, W, N, W, N],
        [N, B, N, N, N, B, W, B, N],
        [N, W, B, N, N, W, N, N, N],
        [N, BK, W, B, W, B, N, N, N],
        [N, N, N, WB, N, N, N, N, N]
      ]
    elif level == 8:
      return [
        [N, N, N, N, N, N, N, N, N],
        [N, N, N, W, B, WW, B, N, N],
        [N, BB, N, B, W, B, WW, BK, WB],
        [B, W, BW, W, N, N, B, N, N],
        [W, N, N, B, N, N, W, BB, W],
        [B, N, N, W, B, W, B, W, B],
        [W, N, N, B, W, N, N, N, N],
        [B, W, B, W, B, N, N, N, N],
        [N, N, N, N, W, N, N, N, N]
      ]
    elif level == 9:
      return [
        [N, N, N, N, N, N, N, N, N],
        [N, N, B, W, B, WK, B, W, B],
        [N, N, WW, B, N, B, N, N, WB],
        [N, W, B, W, N, WW, N, N, B],
        [WB, B, WW, B, N, B, N, N, W],
        [N, W, B, W, BW, W, BW, W, B],
        [N, N, WB, B, W, B, W, BB, WB],
        [N, N, N, N, N, N, N, N, N],
        [N, N, N, N, N, N, N, N, N]
      ]
    elif level == 10:
      return [
        [N, N, N, N, N, N, BB, WB, N],
        [N, N, N, B, W, B, WB, N, N],
        [N, N, N, W, B, W, B, WB, N],
        [WB, N, N, BW, WW, BW, W, B, W],
        [N, N, B, W, BK, WW, BW, N, B],
        [N, N, W, N, N, N, W, B, W],
        [N, N, B, W, N, N, BW, N, BB],
        [N, N, W, B, W, B, W, N, N],
        [N, N, N, W, N, N, N, N, N]
      ]
    else:
      return []
