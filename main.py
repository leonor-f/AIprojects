import pygame
from elements.board import Board

W = 1
B = 2

def main():
    pygame.init()

    # Set up the window title
    pygame.display.set_caption("Chesskoban")
    pygame.display.set_icon(pygame.image.load("img/white_king.png"))

    # Set up some constants
    WIDTH, HEIGHT = 810, 810
    SQUARE_SIZE = 90
    ROWS, COLS = 9, 9
    LEVEL = 1

    # Create the display
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))

    # Create the board
    board = Board(LEVEL)
    white_knights = board.white_knights
    black_knights = board.black_knights
    white_king = board.white_king

    # Game loop
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                new_x, new_y = white_king.get_position()
                if event.key == pygame.K_w:
                    if board.check_move(white_king.x, white_king.y - 1, 'up'):
                        new_x = white_king.x
                        new_y = white_king.y - 1
                elif event.key == pygame.K_a:
                    if board.check_move(white_king.x - 1, white_king.y, 'left'):
                        new_x = white_king.x - 1
                        new_y = white_king.y
                elif event.key == pygame.K_s:
                    if board.check_move(white_king.x, white_king.y + 1, 'down'):
                        new_x = white_king.x
                        new_y = white_king.y + 1
                elif event.key == pygame.K_d:
                    if board.check_move(white_king.x + 1, white_king.y, 'right'):
                        new_x = white_king.x + 1
                        new_y = white_king.y
                
                white_king.move(new_x, new_y)
                
        WIN.fill((0, 0, 0))

        # Draw the board
        for y in range(ROWS):
            for x in range(COLS):
                if board.board[y][x] == W:
                    pygame.draw.rect(WIN, (255, 255, 255), (x*SQUARE_SIZE, y*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                elif board.board[y][x] == B:
                    pygame.draw.rect(WIN, (0, 0, 0), (x*SQUARE_SIZE, y*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                elif board.board[y][x] == 0:
                    pygame.draw.rect(WIN, (112, 113, 160), (x*SQUARE_SIZE, y*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

        # Draw the pieces
        for knight in white_knights:
            WIN.blit(pygame.image.load(knight.image_path), (knight.x*SQUARE_SIZE, knight.y*SQUARE_SIZE))
        for knight in black_knights:
            WIN.blit(pygame.image.load(knight.image_path), (knight.x*SQUARE_SIZE, knight.y*SQUARE_SIZE))
        
        WIN.blit(pygame.image.load(white_king.image_path), (white_king.x*SQUARE_SIZE, white_king.y*SQUARE_SIZE))

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()