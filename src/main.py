import pygame
from time import sleep
from board import Board
from game import Game
from macros import *

def draw_levels_menu(win):
  win.fill((112, 113, 160))
  
  win.blit(TITLE_IMAGE_PATH, (105, 100))
  win.blit(LEVEL_ONE_IMAGE_PATH, (68, 400))
  win.blit(LEVEL_TWO_IMAGE_PATH, (216, 400))
  win.blit(LEVEL_THREE_IMAGE_PATH, (364, 400))
  win.blit(LEVEL_FOUR_IMAGE_PATH, (512, 400))
  win.blit(LEVEL_FIVE_IMAGE_PATH, (660, 400))
  win.blit(LEVEL_SIX_IMAGE_PATH, (68, 600))
  win.blit(LEVEL_SEVEN_IMAGE_PATH, (216, 600))
  win.blit(LEVEL_EIGHT_IMAGE_PATH, (364, 600))
  win.blit(LEVEL_NINE_IMAGE_PATH, (512, 600))
  win.blit(LEVEL_TEN_IMAGE_PATH, (660, 600))
  pygame.display.update()

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return -1
      if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = pygame.mouse.get_pos()
        if 68 <= x <= 148 and 400 <= y <= 480:
          return 0
        elif 216 <= x <= 296 and 400 <= y <= 480:
          return 1
        elif 364 <= x <= 444 and 400 <= y <= 480:
          return 2
        elif 512 <= x <= 592 and 400 <= y <= 480:
          return 3
        elif 660 <= x <= 740 and 400 <= y <= 480:
          return 4
        elif 68 <= x <= 148 and 600 <= y <= 680:
          return 5
        elif 216 <= x <= 296 and 600 <= y <= 680:
          return 6
        elif 364 <= x <= 444 and 600 <= y <= 680:
          return 7
        elif 512 <= x <= 592 and 600 <= y <= 680:
          return 8
        elif 660 <= x <= 740 and 600 <= y <= 680:
          return 9
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
          return -1
        elif event.key == pygame.K_1:
          return 0
        elif event.key == pygame.K_2:
          return 1
        elif event.key == pygame.K_3:
          return 2
        elif event.key == pygame.K_4:
          return 3
        elif event.key == pygame.K_5:
          return 4
        elif event.key == pygame.K_6:
          return 5
        elif event.key == pygame.K_7:
          return 6
        elif event.key == pygame.K_8:
          return 7
        elif event.key == pygame.K_9:
          return 8
        elif event.key == pygame.K_0:
          return 9

def draw_start_menu(win):
  win.fill((112, 113, 160))
  
  win.blit(TITLE_IMAGE_PATH, (105, 100))
  win.blit(HUMAN_IMAGE_PATH, (50, 500))
  win.blit(DFS_IMAGE_PATH, (460, 500))
  win.blit(BFS_IMAGE_PATH, (50, 600))
  win.blit(A_STAR_IMAGE_PATH, (460, 600))
  win.blit(IDDFS_IMAGE_PATH, (50, 700))
  pygame.display.update()

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return '', ''
      if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = pygame.mouse.get_pos()
        if 50 <= x <= 350 and 500 <= y <= 580:
          return 'Human', ''
        elif 460 <= x <= 760 and 500 <= y <= 580:
          return 'AI', 'DFS'
        elif 50 <= x <= 350 and 600 <= y <= 680:
          return 'AI', 'BFS'
        elif 460 <= x <= 760 and 600 <= y <= 680:
          return 'AI', 'A*'
        elif 50 <= x <= 350 and 700 <= y <= 780:
          return 'AI', 'IDDFS'
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
          return '', ''
        elif event.key == pygame.K_1:
          return 'Human', ''
        elif event.key == pygame.K_2:
          return 'AI', 'DFS'
        elif event.key == pygame.K_3:
          return 'AI', 'BFS'
        elif event.key == pygame.K_4:
          return 'AI', 'A*'
        elif event.key == pygame.K_5:
          return 'AI', 'IDDFS'

def draw_menu(win):
  win.fill((112, 113, 160))

  win.blit(TITLE_IMAGE_PATH, (105, 100))
  win.blit(START_IMAGE_PATH, (50, 500))
  win.blit(EXIT_IMAGE_PATH, (460, 500))
  win.blit(LEVELS_IMAGE_PATH, (50, 600))
  win.blit(CONFIG_IMAGE_PATH, (460, 600))
  pygame.display.update()

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return 2
      if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = pygame.mouse.get_pos()
        if 50 <= x <= 350 and 500 <= y <= 580:
          return 1
        elif 460 <= x <= 760 and 500 <= y <= 580:
          return 2
        elif 50 <= x <= 350 and 600 <= y <= 680:
          return 3
        elif 460 <= x <= 760 and 600 <= y <= 680:
          return 4
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_1:
          return 1
        elif event.key == pygame.K_2 or event.key == pygame.K_q:
          return 2
        elif event.key == pygame.K_3:
          return 3
        elif event.key == pygame.K_4:
          return 4

def main():
  # PYGAME INITIALIZATION
  pygame.init()
  pygame.display.set_caption("Chesskoban")
  pygame.display.set_icon(pygame.image.load("../img/pieces/white_king.png"))

  win = pygame.display.set_mode((WIDTH, HEIGHT))

  FONT = pygame.font.Font(None, 40)

  SPACE_TEXT = FONT.render("Press SPACE to finish", True, (255, 255, 255))
  WIN_TEXT = FONT.render("You win!", True, (0, 255, 0))
  LOSE_TEXT = FONT.render("You lose!", True, (255, 0, 0))
  AI_TEXT = FONT.render("Press N to continue", True, (255, 255, 255))

  SPACE_TEXT_RECT = SPACE_TEXT.get_rect()
  WIN_TEXT_RECT = WIN_TEXT.get_rect()
  LOSE_TEXT_RECT = LOSE_TEXT.get_rect()
  AI_TEXT_RECT = AI_TEXT.get_rect()
  
  SPACE_TEXT_RECT.center = (WIDTH // 2, 20)
  WIN_TEXT_RECT.center = (WIDTH // 2, 20)
  LOSE_TEXT_RECT.center = (WIDTH // 2, 20)
  AI_TEXT_RECT.center = (WIDTH // 2, 20)

  # GAME INITIALIZATION
  level = 0
  GAME = Game(Board(level).board)

  menu_option = draw_menu(win)
  
  if menu_option == 1:
    player, algorithm = draw_start_menu(win)
    if player == '':
      level = 7
  elif menu_option == 2:
    level = 7
  elif menu_option == 3:
    level_option = draw_levels_menu(win)
    if level_option == -1:
      level = 7
    else:
      player, algorithm = draw_start_menu(win)
      level = level_option
      if player == '':
        level = 7
  elif menu_option == 4:
    # TODO show how to play, change what is below
    player, algorithm = 'Human', ''

  while level < 7:
    GAME.set_board(Board(level).board)

    if player == 'AI':
      display_text = AI_TEXT
      display_textRect = AI_TEXT_RECT
    else:
      display_text = SPACE_TEXT
      display_textRect = SPACE_TEXT_RECT
    
    run = True
    dfs = 'DFS' == algorithm
    bfs = 'BFS' == algorithm
    iddfs = 'IDDFS' == algorithm

    move_count = 0
    moves = []

    while run:
      if dfs:
        moves = GAME.dfs(MAX_DEPTH[level], 0, [])
        GAME.set_board(Board(level).board)
        dfs = False
      elif bfs:
        moves = GAME.bfs()
        GAME.set_board(Board(level).board)
        bfs = False
      elif iddfs:
        moves = GAME.iddfs(MAX_DEPTH[level] + 1)
        GAME.set_board(Board(level).board)
        iddfs = False
      
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run = False
        elif event.type == pygame.KEYDOWN:
          direction = ''
          if player == 'Human':
            if event.key == pygame.K_w:
              direction = 'up'
            elif event.key == pygame.K_a:
              direction = 'left'
            elif event.key == pygame.K_s:
              direction = 'down'
            elif event.key == pygame.K_d:
              direction = 'right'
            elif event.key == pygame.K_SPACE:
              run = False
              if GAME.check_win():
                display_text = WIN_TEXT
                display_textRect = WIN_TEXT_RECT
                level += 1
              else:
                display_text = LOSE_TEXT
                display_textRect = LOSE_TEXT_RECT
            elif event.key == pygame.K_q:
              run = False
              level = 7
              break
            if direction != '':
              GAME.move(direction)
          else:
            if event.key == pygame.K_n and move_count < MAX_DEPTH[level]:
              GAME.move(moves[1][move_count][2])
              move_count += 1
              if move_count == MAX_DEPTH[level]:
                display_text = WIN_TEXT
                display_textRect = WIN_TEXT_RECT
                level += 1
                run = False
                break
            elif event.key == pygame.K_q:
              run = False
              level = 7
              break
            
      GAME.draw(win)
      
      pygame.draw.rect(win, (0, 0, 0), display_textRect)
      win.blit(display_text, display_textRect)

      pygame.display.update()

      if display_text in [WIN_TEXT, LOSE_TEXT]:
        sleep(0.5)

  sleep(0.5)

  pygame.quit()

if __name__ == "__main__":
  main()
