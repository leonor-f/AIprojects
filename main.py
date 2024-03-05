import pygame
from time import sleep
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
    LEVEL = 3

    # Create the display
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))

    # Create the board
    board = Board(LEVEL)
    white_knights = board.white_knights
    black_knights = board.black_knights
    white_king = board.white_king

    font = pygame.font.Font(None, 32)

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
    win_textRect.center = (WIDTH // 2, HEIGHT // 4)
    lose_textRect.center = (WIDTH // 2, HEIGHT // 4)

    display_text = text
    display_textRect = textRect

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
                elif event.key == pygame.K_SPACE:
                    run = False
                    if board.check_win():
                        display_text = win_text
                        display_textRect = win_textRect
                    else:
                        display_text = lose_text
                        display_textRect = lose_textRect
                elif event.key == pygame.K_q:
                    run = False
                
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
        
        WIN.blit(display_text, display_textRect)

        pygame.display.update()

        if not run:
            sleep(2)

    pygame.quit()

if __name__ == "__main__":
    main()