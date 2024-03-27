import pygame
import copy
from time import sleep
from collections import deque

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
    self.set_positions()

  def set_king(self, x, y):
    self.king = (x, y)
  
  def set_white_knights(self, white_knights):
    self.white_knights = white_knights

  def set_positions(self):
    self.positions = self.get_positions()
    self.king = self.positions[2][0]
    self.white_knights = self.positions[0]
    self.black_knights = self.positions[1]

  def get_positions(self):
    board = self.board
    positions = [[], [], []] # white_knights, black_knights, king
    for y in range(self.rows):
      for x in range(self.cols):
        if board[y][x] == WW or board[y][x] == BW:
          positions[0].append([x, y])
        elif board[y][x] == WB or board[y][x] == BB:
          positions[1].append([x, y])
        elif board[y][x] == WK or board[y][x] == BK:
          positions[2].append((x, y))
        else:
          pass
    return positions
  
  def change_white_knight_board(self, new_x, new_y, x, y):
    board = self.board
    if board[new_y][new_x] == WW:
      board[new_y][new_x] = W
      board[y][x] = BW
    elif board[new_y][new_x] == BW:
      board[new_y][new_x] = B
      board[y][x] = WW
    return board
  
  def change_king_board(self, x, y, new_x, new_y):
    board = self.board
    if board[y][x] == WK:
      board[y][x] = W
      board[new_y][new_x] = BK
    elif board[y][x] == BK:
      board[y][x] = B
      board[new_y][new_x] = WK
    return board
  
  def move_white_knight(self, x, y, direction):
    white_knights = self.white_knights
    if [x, y] in white_knights:
      if direction == 'up' and y - 1 >= 0 and self.board[y - 1][x] not in [0, WB, BB, WW, BW]:
        new_x, new_y = x, y - 1
      elif direction == 'left' and x - 1 >= 0 and self.board[y][x - 1] not in [0, WB, BB, WW, BW]:
        new_x, new_y = x - 1, y
      elif direction == 'down' and y + 1 <= 8 and self.board[y + 1][x] not in [0, WB, BB, WW, BW]:
        new_x, new_y = x, y + 1
      elif direction == 'right' and x + 1 <= 8 and self.board[y][x + 1] not in [0, WB, BB, WW, BW]:
        new_x, new_y = x + 1, y
      else:
        return False
      white_knight_index = white_knights.index([x, y])
      white_knights[white_knight_index] = [new_x, new_y]
      self.set_board(self.change_white_knight_board(x, y, new_x, new_y))
      return True
  
  def move(self, direction):
    x, y = self.king
    board = self.board
    if direction == 'up':
      new_x, new_y = x % 9, (y - 1) % 9
    elif direction == 'left':
      new_x, new_y = (x - 1) % 9, y % 9
    elif direction == 'down':
      new_x, new_y = x % 9, (y + 1) % 9
    elif direction == 'right':
      new_x, new_y = (x + 1) % 9, y % 9
    else:
      return False
    
    if board[new_y][new_x] in [0, WB, BB]:
      return False
    elif board[new_y][new_x] in [WW, BW]:
      if self.move_white_knight(new_x, new_y, direction):
        self.set_board(self.change_king_board(x, y, new_x, new_y))
        return 2
      return False
    self.set_board(self.change_king_board(x, y, new_x, new_y))
    return True

  def undo_move(self, move):
    x, y, direction, knight_moved = move
    white_knights = self.white_knights
    if direction == 'up':
      new_x, new_y = x % 9, (y + 1) % 9
      knight_x, knight_y = x % 9, (y - 1) % 9
    elif direction == 'left':
      new_x, new_y = (x + 1) % 9, y % 9
      knight_x, knight_y = (x - 1) % 9, y % 9
    elif direction == 'down':
      new_x, new_y = x % 9, (y - 1) % 9
      knight_x, knight_y = x % 9, (y + 1) % 9
    elif direction == 'right':
      new_x, new_y = (x - 1) % 9, y % 9
      knight_x, knight_y = (x + 1) % 9, y % 9
    self.set_board(self.change_king_board(x, y, new_x, new_y))
    self.set_king(new_x, new_y)
    if knight_moved:
      white_knight_index = white_knights.index([knight_x, knight_y])
      white_knights[white_knight_index] = [x, y]
      self.set_white_knights(white_knights)
      self.set_board(self.change_white_knight_board(knight_x, knight_y, x, y))

  def simulate(self, white_knights, black_knights):
    if all(knight[2] for knight in black_knights):
      return True

    moves = [(1, -2), (1, 2), (-1, -2), (-1, 2), (2, -1), (2, 1), (-2, -1), (-2, 1)]
    for white_knight in white_knights:
      if not white_knight[2]:
        for move in moves:
          for black_knight in black_knights:
            if not black_knight[2] and white_knight[0] + move[0] == black_knight[0] and white_knight[1] + move[1] == black_knight[1]:
              white_knights_copy = [list(knight) for knight in white_knights]
              black_knights_copy = [list(knight) for knight in black_knights]
              white_knights_copy[white_knights.index(white_knight)][2] = True
              black_knights_copy[black_knights.index(black_knight)][2] = True
              if self.simulate(white_knights_copy, black_knights_copy):
                return True

    return False

  def check_win(self):
    while True:
      white_knights = copy.deepcopy(self.white_knights)
      black_knights = copy.deepcopy(self.black_knights)

      for white_knight in white_knights:
        white_knight.append(False)
      
      for black_knight in black_knights:
        black_knight.append(False)

      if self.simulate(white_knights, black_knights):
        return True
      return False
  
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

  def menu(self):
    while True:
      print("1. Human")
      print("2. Computer")
      choice = input("Choose your player (1 or 2): ")
      if choice == '1':
        return 'Human', ''
      elif choice == '2':
        while True:
          print("1. BFS Algorithm")
          print("2. DFS Algorithm")
          # Add more algorithms here
          algo_choice = input("Choose your algorithm (1 or 2): ")
          if algo_choice == '1':
            return 'Computer', 'BFS'
          elif algo_choice == '2':
            return 'Computer', 'DFS'
          else:
            print("Invalid choice. Please choose a valid algorithm.")
      else:
        print("Invalid choice. Please choose 1 for Human or 2 for Computer.")

  def dfs_king(self, max_depth, depth, path):
    king = self.king
    if depth >= max_depth:
      return []
    moves = [['right', 1, 0], ['left', -1, 0], ['down', 0, 1], ['up', 0, -1]]
    for [direction, x, y] in moves:
      new_x, new_y = king[0] + x, king[1] + y
      value = self.move(direction)
      if value or value == 2:
        path.append((new_x, new_y, direction, value == 2))
        if self.check_win():
          return ["WIN", path]
        tail = self.dfs_king(max_depth, depth + 1, path)
        if len(tail) == 0:
          if len(path) != 0:
            self.undo_move(path.pop())
        elif tail[0] == "WIN":
          return tail
        else:
          path = tail
    return []

  def bfs_king(self):
    directions = {'right': (1, 0), 'left': (-1, 0), 'down': (0, 1), 'up': (0, -1)}
    queue = deque([(copy.deepcopy(self.board), move, []) for move in directions.keys()])
    while queue:
      board, direction, path = queue.popleft()
      self.set_board(board)
      self.set_positions()
      dx, dy = directions[direction]
      new_king = (self.king[0] + dx, self.king[1] + dy)
      value = self.move(direction)
      if value or value == 2:
        tail = (new_king[0], new_king[1], direction, value == 2)
        if self.check_win():
          return ["WIN", path + [tail]]
        queue.extend((copy.deepcopy(self.board), new_move, path + [tail]) for new_move in directions.keys())
        self.undo_move(tail)
    return []
