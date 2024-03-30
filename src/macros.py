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
TITLE_IMAGE_PATH = pygame.image.load("../img/buttons/title.png")
SPACE_IAMGE_PATH = pygame.image.load("../img/buttons/space.png")
START_IMAGE_PATH = pygame.image.load("../img/buttons/start.png")
EXIT_IMAGE_PATH = pygame.image.load("../img/buttons/exit.png")
LEVELS_IMAGE_PATH = pygame.image.load("../img/buttons/levels.png")
RULES_IMAGE_PATH = pygame.image.load("../img/buttons/rules.png")
RULES_PAGE_IMAGE_PATH = pygame.image.load("../img/buttons/rules_page.png")
BACK_IMAGE_PATH = pygame.image.load("../img/buttons/back.png")
HUMAN_IMAGE_PATH = pygame.image.load("../img/buttons/human.png")
IDDFS_IMAGE_PATH = pygame.image.load("../img/buttons/iddfs.png")
BFS_IMAGE_PATH = pygame.image.load("../img/buttons/bfs.png")
A_STAR_SUM_DISTANCE_IMAGE_PATH = pygame.image.load("../img/buttons/a_star_sum_distance.png")
A_STAR_MAX_DISTANCE_IMAGE_PATH = pygame.image.load("../img/buttons/a_star_max_distance.png")
A_STAR_KNIGHTS_NOT_IN_POSITION_IMAGE_PATH = pygame.image.load("../img/buttons/a_star_knights_not_in_position.png")
A_STAR_COMBINED_IMAGE_PATH = pygame.image.load("../img/buttons/a_star_combined.png")
GREEDY_IMAGE_PATH = pygame.image.load("../img/buttons/greedy.png")
WON_IMAGE_PATH = pygame.image.load("../img/buttons/won.png")
LOST_IMAGE_PATH = pygame.image.load("../img/buttons/lost.png")
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
LEVEL_ZERO_IMAGE_PATH = pygame.image.load("../img/levels/level_zero.png")

# MOVEMENT MACROS
RIGHT = ['right', 1, 0]
UP = ['up', 0, -1]
LEFT = ['left', -1, 0]
DOWN = ['down', 0, 1]
MOVES = [RIGHT, UP, LEFT, DOWN]

# GAME STATE MACROS
KNIGHT_TAKEN = 2
