import pygame
from time import sleep
from board import Board
from game import Game
from macros import *

def draw_rules_menu(win):
  """Draws the rules menu on the screen."""
  win.fill((112, 113, 160))
  
  win.blit(RULES_PAGE_IMAGE_PATH, (0, 0))
  win.blit(BACK_IMAGE_PATH, (255, 700))
  pygame.display.update()

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return 0
      if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = pygame.mouse.get_pos()
        if 255 <= x <= 555 and 700 <= y <= 780:
          return 1
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
          return 0
        elif event.key == pygame.K_b:
          return 1

def draw_levels_menu(win):
  """Draws the levels menu on the screen."""
  win.fill((112, 113, 160))
  
  win.blit(TITLE_IMAGE_PATH, (105, 100))
  win.blit(LEVEL_ONE_IMAGE_PATH, (68, 400))
  win.blit(LEVEL_TWO_IMAGE_PATH, (216, 400))
  win.blit(LEVEL_THREE_IMAGE_PATH, (364, 400))
  win.blit(LEVEL_FOUR_IMAGE_PATH, (512, 400))
  win.blit(LEVEL_FIVE_IMAGE_PATH, (660, 400))
  win.blit(LEVEL_SIX_IMAGE_PATH, (68, 550))
  win.blit(LEVEL_SEVEN_IMAGE_PATH, (216, 550))
  win.blit(LEVEL_EIGHT_IMAGE_PATH, (364, 550))
  win.blit(LEVEL_NINE_IMAGE_PATH, (512, 550))
  win.blit(LEVEL_ZERO_IMAGE_PATH, (660, 550))
  win.blit(BACK_IMAGE_PATH, (255, 700))
  pygame.display.update()

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return 0
      if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = pygame.mouse.get_pos()
        if 68 <= x <= 148 and 400 <= y <= 480:
          return 1
        elif 216 <= x <= 296 and 400 <= y <= 480:
          return 2
        elif 364 <= x <= 444 and 400 <= y <= 480:
          return 3
        elif 512 <= x <= 592 and 400 <= y <= 480:
          return 4
        elif 660 <= x <= 740 and 400 <= y <= 480:
          return 5
        elif 68 <= x <= 148 and 550 <= y <= 630:
          return 6
        elif 216 <= x <= 296 and 550 <= y <= 630:
          return 7
        elif 364 <= x <= 444 and 550 <= y <= 630:
          return 8
        elif 512 <= x <= 592 and 550 <= y <= 630:
          return 9
        elif 660 <= x <= 740 and 550 <= y <= 630:
          return 10
        elif 255 <= x <= 555 and 700 <= y <= 780:
          return 11
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
          return 0
        elif event.key == pygame.K_1:
          return 1
        elif event.key == pygame.K_2:
          return 2
        elif event.key == pygame.K_3:
          return 3
        elif event.key == pygame.K_4:
          return 4
        elif event.key == pygame.K_5:
          return 5
        elif event.key == pygame.K_6:
          return 6
        elif event.key == pygame.K_7:
          return 7
        elif event.key == pygame.K_8:
          return 8
        elif event.key == pygame.K_9:
          return 9
        elif event.key == pygame.K_0:
          return 10
        elif event.key == pygame.K_b:
          return 11

def draw_start_menu(win):
  """Draws the start menu on the screen."""
  win.fill((112, 113, 160))
  
  win.blit(TITLE_IMAGE_PATH, (105, 100))
  win.blit(HUMAN_IMAGE_PATH, (50, 400))
  win.blit(IDDFS_IMAGE_PATH, (460, 400))
  win.blit(BFS_IMAGE_PATH, (50, 500))
  win.blit(A_STAR_SUM_DISTANCE_IMAGE_PATH, (460, 500))
  win.blit(A_STAR_MAX_DISTANCE_IMAGE_PATH, (50, 600))
  win.blit(A_STAR_KNIGHTS_NOT_IN_POSITION_IMAGE_PATH, (460, 600))
  win.blit(A_STAR_COMBINED_IMAGE_PATH, (50, 700))
  win.blit(GREEDY_IMAGE_PATH, (460, 700))
  pygame.display.update()

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return '', ''
      if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = pygame.mouse.get_pos()
        if 50 <= x <= 350 and 400 <= y <= 480:
          return 'Human', ''
        elif 460 <= x <= 760 and 400 <= y <= 480:
          return 'AI', 'IDDFS'
        elif 50 <= x <= 350 and 500 <= y <= 580:
          return 'AI', 'BFS'
        elif 460 <= x <= 760 and 500 <= y <= 580:
          return 'AI', 'A_STAR_SUM_DISTANCE'
        elif 50 <= x <= 350 and 600 <= y <= 680:
          return 'AI', 'A_STAR_MAX_DISTANCE'
        elif 460 <= x <= 760 and 600 <= y <= 680:
          return 'AI', 'A_STAR_KNIGHTS'
        elif 50 <= x <= 350 and 700 <= y <= 780:
          return 'AI', 'A_STAR_COMBINED'
        elif 460 <= x <= 760 and 700 <= y <= 780:
          return 'AI', 'Greedy'
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
          return '', ''
        elif event.key == pygame.K_1:
          return 'Human', ''
        elif event.key == pygame.K_2:
          return 'AI', 'IDDFS'
        elif event.key == pygame.K_3:
          return 'AI', 'BFS'
        elif event.key == pygame.K_4:
          return 'AI', 'A_STAR_SUM_DISTANCE'
        elif event.key == pygame.K_5:
          return 'AI', 'A_STAR_MAX_DISTANCE'
        elif event.key == pygame.K_6:
          return 'AI', 'A_STAR_KNIGHTS'
        elif event.key == pygame.K_7:
          return 'AI', 'A_STAR_COMBINED'
        elif event.key == pygame.K_8:
          return 'AI', 'A_STAR_COMBINED'

def draw_menu(win):
  """Draws the main menu on the screen."""
  win.fill((112, 113, 160))

  win.blit(TITLE_IMAGE_PATH, (105, 100))
  win.blit(START_IMAGE_PATH, (50, 500))
  win.blit(LEVELS_IMAGE_PATH, (460, 500))
  win.blit(RULES_IMAGE_PATH, (50, 600))
  win.blit(EXIT_IMAGE_PATH, (460, 600))
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
        elif event.key == pygame.K_2:
          return 2
        elif event.key == pygame.K_3:
          return 3
        elif event.key == pygame.K_4 or event.key == pygame.K_q:
          return 4

def main():
  """Main function of the game."""
  # PYGAME INITIALIZATION
  pygame.init()
  pygame.display.set_caption("Chesskoban")
  pygame.display.set_icon(pygame.image.load("../img/pieces/white_king.png"))

  win = pygame.display.set_mode((WIDTH, HEIGHT))

  font_moves = pygame.font.Font('../font/agency_fb_bold_condensed.otf', 36)
  font_score = pygame.font.Font('../font/agency_fb_bold_condensed.otf', 48)

  # GAME INITIALIZATION
  level = 1
  GAME = Game(Board(level).board)
  
  menu = True

  # MAIN MENU
  while menu:
    menu_option = draw_menu(win)
    if menu_option in [1, 2]:
      if menu_option == 2:
        level_option = draw_levels_menu(win)
        if level_option == 0:
          level = 11
          menu = False
          continue
        elif level_option == 11:
          continue
        level = level_option
      player, algorithm = draw_start_menu(win)
      level = level if player != '' else 11
      menu = False
    elif menu_option == 3:
      if draw_rules_menu(win) == 0:
        level = 11
        menu = False
    elif menu_option == 4:
      level = 11
      menu = False
    
  WON_LOST_IMAGE_PATH = ''
  won_lost = False

  # GAME LOOP
  while level < 11:
    GAME.set_board(Board(level).board)
    
    moves_made = 0
    run = True
    iddfs = 'IDDFS' == algorithm
    bfs = 'BFS' == algorithm
    greedy = 'Greedy' == algorithm
    a_star_sum_distance = 'A_STAR_SUM_DISTANCE' == algorithm
    a_star_max_distance = 'A_STAR_MAX_DISTANCE' == algorithm
    a_star_knights = 'A_STAR_KNIGHTS' == algorithm
    a_star_combined = 'A_STAR_COMBINED' == algorithm

    move_count = 0
    n_moves = 0
    moves = []

    while run:
      if iddfs:
        moves = GAME.iddfs()
        n_moves = len(moves[1])
        GAME.set_board(Board(level).board)
        iddfs = False
      elif bfs:
        moves = GAME.bfs()
        n_moves = len(moves[1])
        GAME.set_board(Board(level).board)
        bfs = False
      elif greedy:
        moves = GAME.greedy()
        n_moves = len(moves[1])
        GAME.set_board(Board(level).board)
        greedy = False
      elif a_star_sum_distance:
        moves = GAME.a_star_sum_distance()
        n_moves = len(moves[1])
        GAME.set_board(Board(level).board)
        a_star_sum_distance = False
      elif a_star_max_distance:
        moves = GAME.a_star_max_distance()
        n_moves = len(moves[1])
        GAME.set_board(Board(level).board)
        a_star_max_distance = False
      elif a_star_knights:
        moves = GAME.a_star_knights_not_in_position()
        n_moves = len(moves[1])
        GAME.set_board(Board(level).board)
        a_star_knights = False
      elif a_star_combined:
        moves = GAME.a_star_combined_heuristic()
        n_moves = len(moves[1])
        GAME.set_board(Board(level).board)
        a_star_combined = False
      
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
            elif event.key == pygame.K_r:
              GAME.set_board(Board(level).board)
              moves_made = 0
            elif event.key == pygame.K_h:
              if GAME.check_win():
                win.blit(NO_MOVES_NEEDED_IMAGE_PATH, (105, 0))
              else:
                move = GAME.hint()
                arrow_images = {
                  'up': ARROW_UP_IMAGE_PATH,
                  'down': ARROW_DOWN_IMAGE_PATH,
                  'right': ARROW_RIGHT_IMAGE_PATH,
                  'left': ARROW_LEFT_IMAGE_PATH
                }
                if move in arrow_images:
                  win.blit(arrow_images[move], (-250, 0))
                  moves_made += 1
                else:
                  win.blit(CANT_WIN_FROM_HERE_IMAGE_PATH, (105, 0))
              pygame.display.update()
              sleep(0.5)
            elif event.key == pygame.K_SPACE:
              run = False
              if GAME.check_win():
                WON_LOST_IMAGE_PATH = WON_IMAGE_PATH
                level += 1
              else:
                WON_LOST_IMAGE_PATH = LOST_IMAGE_PATH
              won_lost = True
            elif event.key == pygame.K_q:
              run = False
              level = 11
              break
            if direction != '':
              move_bool = GAME.move(direction)
              if move_bool or move_bool == KNIGHT_TAKEN:
                moves_made += 1
          else:
            if event.key == pygame.K_n and move_count < n_moves:
              GAME.move(moves[1][move_count][2])
              move_count += 1
              if move_count == n_moves:
                won_lost = True
                WON_LOST_IMAGE_PATH = WON_IMAGE_PATH
                level += 1
                run = False
                break
            elif event.key == pygame.K_q:
              run = False
              level = 11
              break
            
      GAME.draw(win)

      if player == 'Human':
        moves_text = font_moves.render(f'Moves: {moves_made}', True, (255, 255, 255))
        win.blit(moves_text, (700, 750))
      
      pygame.display.update()

      if won_lost:
        if player == 'AI':
          sleep(0.2)
        win.fill((112, 113, 160))
        win.blit(WON_LOST_IMAGE_PATH, (105, 350))
        if WON_LOST_IMAGE_PATH == WON_IMAGE_PATH and player == 'Human':
          score_text = font_score.render(f'Score: {MAX_SCORE - moves_made}', True, (255, 255, 255))
          score_rect = score_text.get_rect(center=(WIDTH/2, 500))
          win.blit(score_text, score_rect)
        pygame.display.update()
        sleep(0.7)
        won_lost = False
  
  sleep(0.5)

  pygame.quit()

if __name__ == "__main__":
  main()
