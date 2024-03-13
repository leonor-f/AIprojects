import pygame
from time import sleep
from elements.board import Board
from elements.game import Game

W = 1
B = 2
WW = 3
WB = 4
BW = 5
BB = 6
WK = 7
BK = 8

def main():
  pygame.init()

  # Set up the window title
  pygame.display.set_caption("Chesskoban")
  pygame.display.set_icon(pygame.image.load("img/white_king.png"))

  # Set up some constants
  WIDTH, HEIGHT = 810, 810
  SQUARE_SIZE = 90
  LEVEL = 1

  # Create the display
  WIN = pygame.display.set_mode((WIDTH, HEIGHT))

  # Create the board
  GAME = Game(Board(LEVEL).board)
  WK_IMAGE_PATH = pygame.image.load("img/white_knight.png")
  BK_IMAGE_PATH = pygame.image.load("img/black_knight.png")
  K_IMAGE_PATH = pygame.image.load("img/white_king.png")

  font = pygame.font.Font(None, 40)

  # Render the text. "True" means anti-aliased text. 
  # (1, 1, 1) is the color of the text (in this case, white).
  text = font.render("Press SPACE to finish", True, (255, 255, 255))
  win_text = font.render("You win!", True, (0, 255, 0))
  lose_text = font.render("You lose!", True, (255, 0, 0))

  # Create a rectangle
  textRect = text.get_rect()
  win_textRect = win_text.get_rect()
  lose_textRect = lose_text.get_rect()

  # Center the text
  textRect.center = (WIDTH // 2, 20)
  win_textRect.center = (WIDTH // 2, 20)
  lose_textRect.center = (WIDTH // 2, 20)

  display_text = text
  display_textRect = textRect

  # Game loop
  run = True
  while run:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
      
      if event.type == pygame.KEYDOWN:
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
          if GAME.check_win():
            display_text = win_text
            display_textRect = win_textRect
          else:
            display_text = lose_text
            display_textRect = lose_textRect
        elif event.key == pygame.K_q:
          run = False
        
        if direction != '':
          GAME.check_move(direction)
                
    # TODO change to 0 0 0 after testing
    WIN.fill((100, 0, 0))

    # Draw the board and the pieces
    GAME.draw(WIN, SQUARE_SIZE, WK_IMAGE_PATH, BK_IMAGE_PATH, K_IMAGE_PATH)

    pygame.draw.rect(WIN, (0, 0, 0), display_textRect)
    WIN.blit(display_text, display_textRect)


    pygame.display.update()

    if not run:
      sleep(2)

  pygame.quit()

if __name__ == "__main__":
  main()