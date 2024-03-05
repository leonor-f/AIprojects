import pygame
from board import Board

def main():
    pygame.init()

    # Set up some constants
    WIDTH, HEIGHT = 900, 900
    SQUARE_SIZE = 100
    ROWS, COLS = 9, 9
    LEVEL = 1

    # Create the display
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))

    # Create the board
    board = Board(LEVEL)

    # Game loop
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = pos[0] // SQUARE_SIZE, pos[1] // SQUARE_SIZE
                board.fill_cell(row, col)

        # Draw everything
        WIN.fill((0, 0, 0))
        board.draw(WIN)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()