import pygame

# BOARD MACROS
N = 0
W = 1 # white square
B = 2 # black square
WW = 3 # white square and white knight
WB = 4 # white square and black knight
BW = 5 # black square and white knight
BB = 6 # black square and black knight
WK = 7 # white square and king
BK = 8 # black square and king

# SIZE MACROS
WIDTH, HEIGHT = 810, 810
SQUARE_SIZE = 90

# IMAGE PATH MACROS
# PIECES
WK_IMAGE_PATH = pygame.image.load("../img/pieces/white_knight.png")
BK_IMAGE_PATH = pygame.image.load("../img/pieces/black_knight.png")
K_IMAGE_PATH = pygame.image.load("../img/pieces/white_king.png")
# BUTTONS
START_IMAGE_PATH = pygame.image.load("../img/buttons/start.png")
EXIT_IMAGE_PATH = pygame.image.load("../img/buttons/exit.png")
TITLE_IMAGE_PATH = pygame.image.load("../img/buttons/title.png")
LEVELS_IMAGE_PATH = pygame.image.load("../img/buttons/levels.png")
CONFIG_IMAGE_PATH = pygame.image.load("../img/buttons/config.png")
HUMAN_IMAGE_PATH = pygame.image.load("../img/buttons/human.png")
DFS_IMAGE_PATH = pygame.image.load("../img/buttons/dfs.png")
BFS_IMAGE_PATH = pygame.image.load("../img/buttons/bfs.png")
A_STAR_IMAGE_PATH = pygame.image.load("../img/buttons/a_star.png")
IDDFS_IMAGE_PATH = pygame.image.load("../img/buttons/iddfs.png")
GREEDY_IMAGE_PATH = pygame.image.load("../img/buttons/greedy.png")
# LEVELS
LEVEL_ONE_IMAGE_PATH = pygame.image.load("../img/levels/level_one.png")
LEVEL_TWO_IMAGE_PATH = pygame.image.load("../img/levels/level_two.png")
LEVEL_THREE_IMAGE_PATH = pygame.image.load("../img/levels/level_three.png")
LEVEL_FOUR_IMAGE_PATH = pygame.image.load("../img/levels/level_four.png")
LEVEL_FIVE_IMAGE_PATH = pygame.image.load("../img/levels/level_five.png")
LEVEL_SIX_IMAGE_PATH = pygame.image.load("../img/levels/level_six.png")
LEVEL_SEVEN_IMAGE_PATH = pygame.image.load("../img/levels/level_seven.png")
LEVEL_EIGHT_IMAGE_PATH = pygame.image.load("../img/levels/level_eight.png")
LEVEL_NINE_IMAGE_PATH = pygame.image.load("../img/levels/level_nine.png")
LEVEL_TEN_IMAGE_PATH = pygame.image.load("../img/levels/level_ten.png")

# ALGORITHM MACROS
MAX_DEPTH = [2, 6, 8, 8, 14, 15, 15]