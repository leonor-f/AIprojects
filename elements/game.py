import pygame

W = 1 # white square
B = 2 # black square
WW = 3 # white square and white knight
WB = 4 # white square and black knight
BW = 5 # black square and white knight
BB = 6 # black square and black knight
WK = 7 # white square and king
BK = 8 # black square and king

class Game:
  def __init__(self, board):
    self.board = board
    self.rows = 9
    self.cols = 9
    self.positions = self.get_positions()
    self.king = self.positions[2][0]
    self.white_knights = self.positions[0]
    self.black_knights = self.positions[1]

  def set_board(self, board):
    self.board = board

  def set_king(self, x, y):
    self.king = (x, y)
  
  def set_white_knights(self, white_knights):
    self.white_knights = white_knights
  
  def set_black_knights(self, black_knights):
    self.black_knights = black_knights

  def get_positions(self):
    positions = [[], [], []] # white_knights, black_knights, king
    for y in range(self.rows):
      for x in range(self.cols):
        if self.board[y][x] == WW or self.board[y][x] == BW:
          positions[0].append([x, y])
        elif self.board[y][x] == WB or self.board[y][x] == BB:
          positions[1].append([x, y])
        elif self.board[y][x] == WK or self.board[y][x] == BK:
          positions[2].append((x, y))
        else:
          pass
    return positions
  
  def move_white_knight(self, new_x, new_y, direction):
    white_knights = self.white_knights
    board = self.board
    for white_knight in white_knights:
      x, y = white_knight
      if x == new_x and y == new_y:
        if direction == 'up' and self.board[new_y - 1][new_x] != 0:
          if not self.check_move_black_knights(new_x, new_y - 1) and not self.check_move_white_knights(new_x, new_y - 1):
            white_knight[0] = new_x
            white_knight[1] = new_y - 1
            if board[y][x] == WW:
              board[y][x] = W
              board[new_y-1][new_x] = BW
            elif board[y][x] == BW:
              board[y][x] = B
              board[new_y-1][new_x] = WW
            self.set_white_knights(white_knights)
            self.set_board(board)
          else:
            return False
        elif direction == 'left' and self.board[new_y][new_x - 1] != 0:
          if not self.check_move_black_knights(new_x - 1, new_y) and not self.check_move_white_knights(new_x - 1, new_y):
            white_knight[0] = new_x - 1
            white_knight[1] = new_y
            if board[y][x] == WW:
              board[y][x] = W
              board[new_y][new_x-1] = BW
            elif board[y][x] == BW:
              board[y][x] = B
              board[new_y][new_x-1] = WW
            self.set_white_knights(white_knights)
            self.set_board(board)
          else:
            return False
        elif direction == 'down' and self.board[new_y + 1][new_x] != 0:
          if not self.check_move_black_knights(new_x, new_y + 1) and not self.check_move_white_knights(new_x, new_y + 1):
            white_knight[0] = new_x
            white_knight[1] = new_y + 1
            if board[y][x] == WW:
              board[y][x] = W
              board[new_y+1][new_x] = BW
            elif board[y][x] == BW:
              board[y][x] = B
              board[new_y+1][new_x] = WW
            self.set_white_knights(white_knights)
            self.set_board(board)
          else:
            return False
        elif direction == 'right' and self.board[new_y][new_x + 1] != 0:
          if not self.check_move_black_knights(new_x + 1, new_y) and not self.check_move_white_knights(new_x + 1, new_y):
            white_knight[0] = new_x + 1
            white_knight[1] = new_y
            if board[y][x] == WW:
              board[y][x] = W
              board[new_y][new_x+1] = BW
            elif board[y][x] == BW:
              board[y][x] = B
              board[new_y][new_x+1] = WW
            self.set_white_knights(white_knights)
            self.set_board(board)
          else:
            return False
        else:
          return False
        return True
  
  def check_move_black_knights(self, new_x, new_y):
    black_knights = self.black_knights
    for black_knight in black_knights:
      if black_knight[0] == new_x and black_knight[1] == new_y:
        return True
    return False
  
  def check_move_white_knights(self, new_x, new_y):
    white_knights = self.white_knights
    for white_knight in white_knights:
      if white_knight[0] == new_x and white_knight[1] == new_y:
        return True
    return False
  
  def check_move(self, direction):
    x, y = self.king
    board = self.board
    if direction == 'up':
      new_x, new_y = x, y - 1
    elif direction == 'left':
      new_x, new_y = x - 1, y
    elif direction == 'down':
      new_x, new_y = x, y + 1
    elif direction == 'right':
      new_x, new_y = x + 1, y
    else:
      return
    
    if board[new_y][new_x] in [0, WB, BB]:
      return
    elif board[new_y][new_x] in [WW, BW]:
      if self.move_white_knight(new_x, new_y, direction):
        if board[y][x] == WK:
          board[y][x] = W
          board[new_y][new_x] = BK
        elif board[y][x] == BK:
          board[y][x] = B
          board[new_y][new_x] = WK
        self.set_king(new_x, new_y)
    else:
      if board[y][x] == WK:
        board[y][x] = W
        board[new_y][new_x] = BK
      elif board[y][x] == BK:
        board[y][x] = B
        board[new_y][new_x] = WK
      self.set_king(new_x, new_y)
      self.set_board(board)
      return

  def check_win(self):
    while True:
      temp_white_knights = self.white_knights.copy()
      temp_black_knights = self.black_knights.copy()

      for white_knight in temp_white_knights:
        white_knight.append(False)
      
      for black_knight in temp_black_knights:
        black_knight.append(False)

      for white_knight in temp_white_knights:
        if not white_knight[2]:
          for black_knight in temp_black_knights:
            if not black_knight[2]:
              if white_knight[0] + 1 == black_knight[0] and white_knight[1] - 2 == black_knight[1]:
                white_knight[2] = True
                black_knight[2] = True
                break
              elif white_knight[0] + 1 == black_knight[0] and white_knight[1] + 2 == black_knight[1]:
                white_knight[2] = True
                black_knight[2] = True
                break
              elif white_knight[0] - 1 == black_knight[0] and white_knight[1] - 2 == black_knight[1]:
                white_knight[2] = True
                black_knight[2] = True
                break
              elif white_knight[0] - 1 == black_knight[0] and white_knight[1] + 2 == black_knight[1]:
                white_knight[2] = True
                black_knight[2] = True
                break
              elif white_knight[0] + 2 == black_knight[0] and white_knight[1] - 1 == black_knight[1]:
                white_knight[2] = True
                black_knight[2] = True
                break
              elif white_knight[0] + 2 == black_knight[0] and white_knight[1] + 1 == black_knight[1]:
                white_knight[2] = True
                black_knight[2] = True
                break
              elif white_knight[0] - 2 == black_knight[0] and white_knight[1] - 1 == black_knight[1]:
                white_knight[2] = True
                black_knight[2] = True
                break
              elif white_knight[0] - 2 == black_knight[0] and white_knight[1] + 1 == black_knight[1]:
                white_knight[2] = True
                black_knight[2] = True
                break
      
      for white_knight in temp_white_knights:
        if not white_knight[2]:
          return False
      
      for black_knight in temp_black_knights:
        if not black_knight[2]:
          return False
    
      return True
  
  def draw(self, WIN, SQUARE_SIZE, WK_IMAGE_PATH, BK_IMAGE_PATH, K_IMAGE_PATH):
    board = self.board
    for y in range(self.rows):
      for x in range(self.cols):
        if board[y][x] == W:
          pygame.draw.rect(WIN, (255, 255, 255), (x*SQUARE_SIZE, y*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        elif board[y][x] == B:
          pygame.draw.rect(WIN, (0, 0, 0), (x*SQUARE_SIZE, y*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        elif board[y][x] == 0:
          pygame.draw.rect(WIN, (112, 113, 160), (x*SQUARE_SIZE, y*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        elif board[y][x] == WW:
          pygame.draw.rect(WIN, (255, 255, 255), (x*SQUARE_SIZE, y*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
          WIN.blit(WK_IMAGE_PATH, (x*SQUARE_SIZE, y*SQUARE_SIZE))
        elif board[y][x] == WB:
          pygame.draw.rect(WIN, (255, 255, 255), (x*SQUARE_SIZE, y*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
          WIN.blit(BK_IMAGE_PATH, (x*SQUARE_SIZE, y*SQUARE_SIZE))
        elif board[y][x] == BW:
          pygame.draw.rect(WIN, (0, 0, 0), (x*SQUARE_SIZE, y*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
          WIN.blit(WK_IMAGE_PATH, (x*SQUARE_SIZE, y*SQUARE_SIZE))
        elif board[y][x] == BB:
          pygame.draw.rect(WIN, (0, 0, 0), (x*SQUARE_SIZE, y*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
          WIN.blit(BK_IMAGE_PATH, (x*SQUARE_SIZE, y*SQUARE_SIZE))
        elif board[y][x] == WK:
          pygame.draw.rect(WIN, (255, 255, 255), (x*SQUARE_SIZE, y*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
          WIN.blit(K_IMAGE_PATH, (x*SQUARE_SIZE, y*SQUARE_SIZE))
        elif board[y][x] == 8:
          pygame.draw.rect(WIN, (0, 0, 0), (x*SQUARE_SIZE, y*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
          WIN.blit(K_IMAGE_PATH, (x*SQUARE_SIZE, y*SQUARE_SIZE))