import pygame
import random
from time import sleep
from board import Board
from game import Game

def main():
  pygame.init()

  pygame.display.set_caption("Chesskoban")
  pygame.display.set_icon(pygame.image.load("../img/white_king.png"))

  WIDTH, HEIGHT = 810, 810
  SQUARE_SIZE = 90
  LEVEL = 4

  WIN = pygame.display.set_mode((WIDTH, HEIGHT))

  WK_IMAGE_PATH = pygame.image.load("../img/white_knight.png")
  BK_IMAGE_PATH = pygame.image.load("../img/black_knight.png")
  K_IMAGE_PATH = pygame.image.load("../img/white_king.png")

  font = pygame.font.Font(None, 40)

  text = font.render("Press SPACE to finish", True, (255, 255, 255))
  win_text = font.render("You win!", True, (0, 255, 0))
  lose_text = font.render("You lose!", True, (255, 0, 0))

  textRect = text.get_rect()
  win_textRect = win_text.get_rect()
  lose_textRect = lose_text.get_rect()

  textRect.center = (WIDTH // 2, 20)
  win_textRect.center = (WIDTH // 2, 20)
  lose_textRect.center = (WIDTH // 2, 20)

  while LEVEL < 5:
    GAME_IA = Game(Board(LEVEL).board)
    GAME_PLAYER = Game(Board(LEVEL).board)

    display_text = text
    display_textRect = textRect
    
    run = True
    dfs = True
    max_depth = [1, 6, 23, 23, 8]

    move_count = 0
    moves = []

    while run:
      # GAME.move(random.choice(['up', 'down', 'left', 'right']))
      if dfs:
        moves = GAME_IA.dfs_king(max_depth[LEVEL], 0, [])
        print(moves)
        dfs = False
      
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run = False
        elif event.type == pygame.KEYDOWN:
          direction = ''
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
            if GAME_IA.check_win():
              display_text = win_text
              display_textRect = win_textRect
            else:
              display_text = lose_text
              display_textRect = lose_textRect
              LEVEL -= 1
            break
          elif event.key == pygame.K_q:
            run = False
            LEVEL = 4
            break
          elif event.key == pygame.K_n and move_count < max_depth[LEVEL]:
            GAME_PLAYER.move(moves[1][move_count][2])
            move_count += 1
          
          if direction != '':
            GAME_PLAYER.move(direction)
                  
      WIN.fill((0, 0, 0))

      GAME_PLAYER.draw(WIN, SQUARE_SIZE, WK_IMAGE_PATH, BK_IMAGE_PATH, K_IMAGE_PATH)
      
      pygame.draw.rect(WIN, (0, 0, 0), display_textRect)
      WIN.blit(display_text, display_textRect)

      pygame.display.update()

      if display_text in [win_text, lose_text]:
        sleep(0.5)

    LEVEL += 1

  sleep(0.5)

  pygame.quit()

if __name__ == "__main__":
  main()
