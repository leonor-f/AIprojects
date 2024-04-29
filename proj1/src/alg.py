import random

W = 1
B = 2
WW = 3
WB = 4
BW = 5
BB = 6
WK = 7
BK = 8

# função para calcular as posições em que os cavalos brancos matam os cavalos pretos
# função para posições válidas dos cavalos brancos
def get_valid_pos(knights, moves, board):
  valid_pos = []
  for knight in knights:
    valid_pos_knight = []
    x, y = knight[:2]
    for move in moves:
      new_x, new_y = x + move[0], y + move[1]
      if 0 <= new_x < 9 and 0 <= new_y < 9 and board[new_y][new_x] != 0:
        valid_pos_knight.append([new_x, new_y])
    valid_pos.append(valid_pos_knight)
  return valid_pos

# função para verificar se as posições válidas dos cavalos brancos são possíveis

# função para calcular a distância entre a posição do cavalo branco e uma posição TAKE
def calculate_distance(white_knight, take_positions):
    x, y = white_knight[:2]
    distances = []
    for take_position in take_positions:
        for pos in take_position:
            dist = abs(pos[0] - x) + abs(pos[1] - y)
            distances.append(dist)
    return min(distances) if distances else 0

# função principal
