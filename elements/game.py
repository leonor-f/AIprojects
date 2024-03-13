import pygame

W = 1
B = 2
WW = 3
WB = 4
BW = 5
BB = 6
WK = 7
BK = 8

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
  
  def change_board(self, board, new_x, new_y, x, y):
    if board[new_y][new_x] == WW:
      board[new_y][new_x] = W
      board[y][x] = BW
    elif board[new_y][new_x] == BW:
      board[new_y][new_x] = B
      board[y][x] = WW
    return board
  
  def move_white_knight(self, new_x, new_y, direction):
    white_knights = self.white_knights
    board = self.board
    if [new_x, new_y] in white_knights:
      if direction == 'up' and self.board[new_y - 1][new_x] not in [0, WB, BB, WW, BW]:
        x, y = new_x, new_y - 1
        white_knight_index = white_knights.index([new_x, new_y])
        white_knights[white_knight_index] = [x, y]
      elif direction == 'left' and self.board[new_y][new_x - 1] not in [0, WB, BB, WW, BW]:
        x, y = new_x - 1, new_y
        white_knight_index = white_knights.index([new_x, new_y])
        white_knights[white_knight_index] = [x, y]
      elif direction == 'down' and self.board[new_y + 1][new_x] not in [0, WB, BB, WW, BW]:
        x, y = new_x, new_y + 1
        white_knight_index = white_knights.index([new_x, new_y])
        white_knights[white_knight_index] = [x, y]
      elif direction == 'right' and self.board[new_y][new_x + 1] not in [0, WB, BB, WW, BW]:
        x, y = new_x + 1, new_y
        white_knight_index = white_knights.index([new_x, new_y])
        white_knights[white_knight_index] = [x, y]
      else:
        return False
      self.set_white_knights(white_knights)
      self.set_board(self.change_board(board, new_x, new_y, x, y))
      return True
  
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