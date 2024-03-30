import pygame
import copy
import heapq
from collections import deque
from macros import *

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
    """Set the board to the given board."""
    self.board = board
    self.set_positions()

  def set_king(self, x, y):
    """Set the king to the given position."""
    self.king = (x, y)
  
  def set_white_knights(self, white_knights):
    """Set the white knights to the given positions."""
    self.white_knights = white_knights

  def set_positions(self):
    """Set the positions of the white knights, black knights and the king."""
    self.positions = self.get_positions()
    self.king = self.positions[2][0]
    self.white_knights = self.positions[0]
    self.black_knights = self.positions[1]

  def get_positions(self):
    """Get the positions of the white knights, black knights and the king."""
    board = self.board
    # Positions of the white knights, black knights and the king
    positions = [[], [], []]
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
  
  def get_take_positions(self):
    """Get the positions that the white knights can take the black knights."""
    board = self.board
    black_knights = self.black_knights
    take_positions = []
    for black_knight in black_knights:
      x, y = black_knight[:2]
      # Calculate the positions that a white knight can move to take this black knight
      take_positions_knight = [[x + 2, y + 1], [x + 1, y + 2], [x - 1, y + 2], [x - 2, y + 1], [x - 2, y - 1], [x - 1, y - 2], [x + 1, y - 2], [x + 2, y - 1]]
      valid_take_positions_knight = []
      for pos in take_positions_knight:
        new_x, new_y = pos
        if 0 <= new_x < 9 and 0 <= new_y < 9 and board[new_y][new_x] not in [N, WB, BB]:
          valid_take_positions_knight.append(pos)
      # Add the list of valid take positions for this black knight to the overall list
      take_positions.append(valid_take_positions_knight)
    return take_positions
  
  def change_white_knight_board(self, new_x, new_y, x, y):
    """Change the board when a white knight moves."""
    board = self.board
    if board[new_y][new_x] == WW:
      board[new_y][new_x] = W
      board[y][x] = BW
    elif board[new_y][new_x] == BW:
      board[new_y][new_x] = B
      board[y][x] = WW
    return board

  def change_king_board(self, x, y, new_x, new_y):
    """Change the board when the king moves."""
    board = self.board
    if board[y][x] == WK:
      board[y][x] = W
      board[new_y][new_x] = BK
    elif board[y][x] == BK:
      board[y][x] = B
      board[new_y][new_x] = WK
    return board
  
  def move_white_knight(self, x, y, direction):
    """Move the white knight in the given direction."""
    white_knights = self.white_knights
    # Check if the white knight can move in the given direction
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
      # Move the white knight
      white_knight_index = white_knights.index([x, y])
      white_knights[white_knight_index] = [new_x, new_y]
      self.set_board(self.change_white_knight_board(x, y, new_x, new_y))
      return True
  
  def move(self, direction):
    """Move the king in the given direction."""
    x, y = self.king
    board = self.board
    if direction == 'up':
      new_x, new_y = x, (y - 1) if y > 0 else 0
    elif direction == 'left':
      new_x, new_y = (x - 1) if x > 0 else 0, y
    elif direction == 'down':
      new_x, new_y = x, (y + 1) if y < 8 else 8
    elif direction == 'right':
      new_x, new_y = (x + 1) if x < 8 else 8, y
    else:
      return False
    
    # Check if the king can move in the given direction
    cell_value = board[new_y][new_x]
    if cell_value in [0, WB, BB, WK, BK]:
      return False
    elif cell_value in [WW, BW] and not self.move_white_knight(new_x, new_y, direction):
      return False
    self.set_board(self.change_king_board(x, y, new_x, new_y))
    return KNIGHT_TAKEN if cell_value in [WW, BW] else True

  def undo_move(self, move):
    """Undo the move."""
    x, y, direction, knight_moved = move
    white_knights = self.white_knights
    # Depending on the direction, move the king in the opposite direction
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
    # If a white knight was moved, move it back
    if knight_moved:
      white_knight_index = white_knights.index([knight_x, knight_y])
      white_knights[white_knight_index] = [x, y]
      self.set_white_knights(white_knights)
      self.set_board(self.change_white_knight_board(knight_x, knight_y, x, y))

  def simulate(self, white_knights, black_knights):
    """Simulate a game round to check if there's a winning state."""
    # Check if all the black knights have been taken
    if all(knight[2] for knight in black_knights):
      return True

    # Check if there's a white knight that can take a black knight
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
    """Check if there's a winning state for the current game."""
    while True:
      white_knights = copy.deepcopy(self.white_knights)
      black_knights = copy.deepcopy(self.black_knights)

      # Add a flag to check if a knight has been taken
      for white_knight in white_knights:
        white_knight.append(False)
      
      for black_knight in black_knights:
        black_knight.append(False)

      # Use the simulate function to check if there's a winning state
      if self.simulate(white_knights, black_knights):
        return True
      return False
  
  def draw(self, win):
    """Draw the game board."""
    board = self.board
    for y in range(self.rows):
      for x in range(self.cols):
        if board[y][x] == W:
          pygame.draw.rect(win, (255, 255, 255), (x*SQUARE_SIZE, y*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        elif board[y][x] == B:
          pygame.draw.rect(win, (0, 0, 0), (x*SQUARE_SIZE, y*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        elif board[y][x] == N:
          pygame.draw.rect(win, (112, 113, 160), (x*SQUARE_SIZE, y*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        elif board[y][x] == WW:
          pygame.draw.rect(win, (255, 255, 255), (x*SQUARE_SIZE, y*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
          win.blit(WK_IMAGE_PATH, (x*SQUARE_SIZE, y*SQUARE_SIZE))
        elif board[y][x] == WB:
          pygame.draw.rect(win, (255, 255, 255), (x*SQUARE_SIZE, y*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
          win.blit(BK_IMAGE_PATH, (x*SQUARE_SIZE, y*SQUARE_SIZE))
        elif board[y][x] == BW:
          pygame.draw.rect(win, (0, 0, 0), (x*SQUARE_SIZE, y*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
          win.blit(WK_IMAGE_PATH, (x*SQUARE_SIZE, y*SQUARE_SIZE))
        elif board[y][x] == BB:
          pygame.draw.rect(win, (0, 0, 0), (x*SQUARE_SIZE, y*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
          win.blit(BK_IMAGE_PATH, (x*SQUARE_SIZE, y*SQUARE_SIZE))
        elif board[y][x] == WK:
          pygame.draw.rect(win, (255, 255, 255), (x*SQUARE_SIZE, y*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
          win.blit(K_IMAGE_PATH, (x*SQUARE_SIZE, y*SQUARE_SIZE))
        elif board[y][x] == BK:
          pygame.draw.rect(win, (0, 0, 0), (x*SQUARE_SIZE, y*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
          win.blit(K_IMAGE_PATH, (x*SQUARE_SIZE, y*SQUARE_SIZE))

  def dfs(self, max_depth, depth, path):
    """Depth-first search algorithm."""
    if depth >= max_depth:
      return []
    for [direction, x, y] in MOVES:
      new_x, new_y = self.king[0] + x, self.king[1] + y
      value = self.move(direction)
      if value or value == KNIGHT_TAKEN:
        path.append((new_x, new_y, direction, value == KNIGHT_TAKEN))
        if self.check_win():
          return ["WIN", path]
        tail = self.dfs(max_depth, depth + 1, path)
        if len(tail) == 0:
          if len(path) != 0:
            self.undo_move(path.pop())
        elif tail[0] == "WIN":
          return tail
        else:
          path = tail
    return []
  
  def iddfs(self):
    """Iterative deepening depth-first search algorithm."""
    depth = 0
    result = []
    while len(result) == 0:
      result = self.dfs(depth, 0, [])
      depth += 1
    return result

  def bfs(self):
    """Breadth-first search algorithm."""
    queue = deque([(copy.deepcopy(self.board), [])])
    visited = set()
    while queue:
      board, path = queue.popleft()
      board_tuple = tuple(map(tuple, board))
      if board_tuple in visited:
          continue
      visited.add(board_tuple)
      self.set_board(board)
      self.set_positions()
      for [direction, x, y] in MOVES:
        new_x, new_y = self.king[0] + x, self.king[1] + y
        value = self.move(direction)
        if value or value == KNIGHT_TAKEN:
          tail = (new_x, new_y, direction, value == KNIGHT_TAKEN)
          if self.check_win():
            return ["WIN", path + [tail]]
          queue.append((copy.deepcopy(self.board), path + [tail]))
          self.undo_move(tail)
    return []

  def greedy(self):
    """Greedy algorithm."""
    path = []
    queue = []
    # Push the initial state to the priority queue
    heapq.heappush(queue, (0, copy.deepcopy(self.board), path))
    # Set to keep track of visited states
    visited = set()
    while queue:
      _, board, path = heapq.heappop(queue)
      board_tuple = tuple(map(tuple, board))
      if board_tuple in visited:
        continue
      visited.add(board_tuple)
      self.set_board(board)
      self.set_positions()
      take_positions = self.get_take_positions()
      for [direction, x, y] in MOVES:
        new_x, new_y = self.king[0] + x, self.king[1] + y
        value = self.move(direction)
        if value or value == KNIGHT_TAKEN:
          white_knights = self.white_knights
          tail = (new_x, new_y, direction, value == KNIGHT_TAKEN)
          new_path = path + [tail]
          if self.check_win():
            return ["WIN", new_path]
          distances = []
          for white_knight in white_knights:
            distances.append(min([abs(white_knight[0] - pos[0]) + abs(white_knight[1] - pos[1]) for pos in take_positions[white_knights.index(white_knight)]], default=0))
          if sum(distances) == 0:
            return ["WIN", new_path]
          heapq.heappush(queue, (sum(distances), copy.deepcopy(self.board), new_path))
          self.undo_move(tail)
    return []
  
  def heuristic_sum_distances(self):
    """Heuristic function for the sum of distances."""
    distances = []
    for white_knight in self.white_knights:
      distances.append(min([abs(white_knight[0] - pos[0]) + abs(white_knight[1] - pos[1]) for pos in self.get_take_positions()[self.white_knights.index(white_knight)]], default=0))
    return sum(distances)

  def a_star_sum_distance(self):
    """A* algorithm with the sum of distances heuristic."""
    path = []
    queue = []
    # Set to keep track of visited states
    visited = set()
    # Push the initial state to the priority queue
    heapq.heappush(queue, (0, self.board, path))
    while queue:
      cost, board, path = heapq.heappop(queue)
      board_tuple = tuple(map(tuple, board))
      if board_tuple in visited:
        continue
      visited.add(board_tuple)
      self.set_board(board)
      self.set_positions()
      for [direction, x, y] in MOVES:
        new_x, new_y = self.king[0] + x, self.king[1] + y
        value = self.move(direction)
        if value or value == KNIGHT_TAKEN:
          tail = (new_x, new_y, direction, value == KNIGHT_TAKEN)
          new_path = path + [tail]
          if self.check_win():
            return ["WIN", new_path]
          heuristic = self.heuristic_sum_distances()
          heapq.heappush(queue, (heuristic + cost + 1, copy.deepcopy(self.board), new_path))
          self.undo_move(tail)
    return []
  
  def heuristic_max_distance(self):
    """Heuristic function for the max distance."""
    distances = []
    for white_knight in self.white_knights:
      distances.append(min([abs(white_knight[0] - pos[0]) + abs(white_knight[1] - pos[1]) for pos in self.get_take_positions()[self.white_knights.index(white_knight)]], default=0))
    return max(distances) if distances else 0
  
  def a_star_max_distance(self):
    """A* algorithm with the max distance heuristic."""
    path = []
    queue = []
    # Push the initial state to the priority queue
    heapq.heappush(queue, (0, copy.deepcopy(self.board), path))
    # Set to keep track of visited states
    visited = set()
    while queue:
      _, board, path = heapq.heappop(queue)
      board_tuple = tuple(map(tuple, board))
      if board_tuple in visited:
        continue
      visited.add(board_tuple)
      self.set_board(board)
      self.set_positions()
      for [direction, x, y] in MOVES:
        new_x, new_y = self.king[0] + x, self.king[1] + y
        value = self.move(direction)
        if value or value == KNIGHT_TAKEN:
          tail = (new_x, new_y, direction, value == KNIGHT_TAKEN)
          new_path = path + [tail]
          if self.check_win():
            return ["WIN", new_path]
          heuristic = self.heuristic_max_distance()
          heapq.heappush(queue, (len(new_path) + heuristic, copy.deepcopy(self.board), new_path))
          self.undo_move(tail)
    return []
  
  def heuristic_knights_not_in_position(self):
    """Heuristic function for the number of knights not in take positions."""
    count = 0
    for white_knight in self.white_knights:
      if white_knight not in self.get_take_positions()[self.white_knights.index(white_knight)]:
        count += 1
    return count

  def a_star_knights_not_in_position(self):
    """A* algorithm with the number of knights not in take positions heuristic."""
    path = []
    queue = []
    # Push the initial state to the priority queue
    heapq.heappush(queue, (0, copy.deepcopy(self.board), path))
    # Set to keep track of visited states
    visited = set()
    while queue:
      _, board, path = heapq.heappop(queue)
      board_tuple = tuple(map(tuple, board))
      if board_tuple in visited:
        continue
      visited.add(board_tuple)
      self.set_board(board)
      self.set_positions()
      for [direction, x, y] in MOVES:
        new_x, new_y = self.king[0] + x, self.king[1] + y
        value = self.move(direction)
        if value or value == KNIGHT_TAKEN:
          tail = (new_x, new_y, direction, value == KNIGHT_TAKEN)
          new_path = path + [tail]
          if self.check_win():
            return ["WIN", new_path]
          heuristic = self.heuristic_knights_not_in_position()
          heapq.heappush(queue, (len(new_path) + heuristic, copy.deepcopy(self.board), new_path))
          self.undo_move(tail)
    return []
  
  def combined_heuristic(self):
    """Combined heuristic function."""
    # Weights for the heuristics
    weight1 = 1.0
    weight2 = 1.0
    weight3 = 1.0

    # Heuristics
    heuristic1 = self.heuristic_sum_distances()
    heuristic2 = self.heuristic_max_distance()
    heuristic3 = self.heuristic_knights_not_in_position()

    combined_heuristic = weight1 * heuristic1 + weight2 * heuristic2 + weight3 * heuristic3

    return combined_heuristic
  
  def a_star_combined_heuristic(self):
    """A* algorithm with the combined heuristic."""
    path = []
    queue = []
    # Push the initial state to the priority queue
    heapq.heappush(queue, (0, copy.deepcopy(self.board), path))
    # Set to keep track of visited states
    visited = set()
    while queue:
      _, board, path = heapq.heappop(queue)
      board_tuple = tuple(map(tuple, board))
      if board_tuple in visited:
        continue
      visited.add(board_tuple)
      self.set_board(board)
      self.set_positions()
      for [direction, x, y] in MOVES:
        new_x, new_y = self.king[0] + x, self.king[1] + y
        value = self.move(direction)
        if value or value == KNIGHT_TAKEN:
          tail = (new_x, new_y, direction, value == KNIGHT_TAKEN)
          new_path = path + [tail]
          if self.check_win():
            return ["WIN", new_path]
          heuristic = self.combined_heuristic()
          heapq.heappush(queue, (len(new_path) + heuristic, copy.deepcopy(self.board), new_path))
          self.undo_move(tail)
    return []

  def hint(self):
    """Get a hint for the next move."""
    current_board = copy.deepcopy(self.board)
    moves = self.a_star_sum_distance()
    self.set_board(current_board)
    if moves:
      return moves[1][0][2]
    return ''
