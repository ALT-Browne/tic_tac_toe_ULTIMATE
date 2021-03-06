import pygame
from tic_tac_toe_class import tic_tac_toe_BASIC
from basic_gui_constants import *
pygame.init()

WIN = pygame.display.set_mode((SQUARE_LENGTH, SQUARE_LENGTH))
pygame.display.set_caption("tic-tac-toe-BASIC")

def draw_window(board):
    """
    Draw the present state of the board in the game window.

    param board: instance of tic_tac_toe_BASIC class.
    """
    WIN.fill(WHITE)
    for i in range(0, len(board.get_grid())): # Draw all symbols that have been played thus far
        if board.get_grid()[i] == "O": # Retrieve moves from board class variable
            WIN.blit(LETTER_O, LETTER_LOCATIONS[i])
        if board.get_grid()[i] == "X":
            WIN.blit(LETTER_X, LETTER_LOCATIONS[i])
    pygame.draw.rect(WIN, BLACK, GRID_VERT_1)
    pygame.draw.rect(WIN, BLACK, GRID_VERT_2)
    pygame.draw.rect(WIN, BLACK, GRID_HORIZ_1)
    pygame.draw.rect(WIN, BLACK, GRID_HORIZ_2)
    pygame.display.update()

def rematch(font, message_rect):
    """
    Offer the players a rematch and allow them to decide by clicking YES or NO.

    param font: Font object

    param message_rect: Rect object

    Return: bool.  
    """
    option_yes = font.render("YES", 1, RED)
    option_no = font.render("NO", 1, RED)
    option_yes_rect = pygame.Rect(SQUARE_LENGTH / 2 - option_yes.get_width() - SQUARE_LENGTH / 8, message_rect.bottom + SQUARE_LENGTH / 5, option_yes.get_width(), option_yes.get_height())
    option_no_rect = pygame.Rect(SQUARE_LENGTH / 2 + SQUARE_LENGTH / 8, message_rect.bottom + SQUARE_LENGTH / 5, option_no.get_width(), option_no.get_height())
    WIN.blit(option_yes, (option_yes_rect.left, option_yes_rect.top))
    WIN.blit(option_no, (option_no_rect.left, option_no_rect.top))
    pygame.display.update()
    pygame.time.delay(5000)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if option_yes_rect.collidepoint(mouse_pos):
                return True
            if option_no_rect.collidepoint(mouse_pos):
                return False

def draw_winner(text):
    """
    Draw message stating the winner. Call rematch function.

    param text: str - text saying which symbol won.

    Return: bool.  
    """
    draw_text = WINNER_FONT.render(text, 1, RED)
    draw_text_rect = pygame.Rect(SQUARE_LENGTH / 2 - draw_text.get_width() / 2, SQUARE_LENGTH / 2 - draw_text.get_height() / 2, draw_text.get_width(), draw_text.get_height())
    WIN.blit(draw_text, (SQUARE_LENGTH / 2 - draw_text.get_width() / 2, SQUARE_LENGTH / 2 - draw_text.get_height() / 2))
    pygame.display.update()
    if rematch(WINNER_FONT, draw_text_rect):
        return True
    else:
        return False

def draw_draw(text):
    """
    Draw message stating a draw. Call rematch function.

    param text: str - text saying it's a draw.

    Return: bool.  
    """
    draw_text = DRAW_FONT.render(text, 1, RED)
    draw_text_rect = pygame.Rect(SQUARE_LENGTH / 2 - draw_text.get_width() / 2, SQUARE_LENGTH / 2 - draw_text.get_height() / 2, draw_text.get_width(), draw_text.get_height())
    WIN.blit(draw_text, (SQUARE_LENGTH / 2 - draw_text.get_width() / 2, SQUARE_LENGTH / 2 - draw_text.get_height() / 2))
    pygame.display.update()
    if rematch(DRAW_FONT, draw_text_rect):
        return True
    else:
        return False

def main():
    board = tic_tac_toe_BASIC()
    clock = pygame.time.Clock()
    run = True
    previous_moves = []
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for cell in CELLS:
                    if cell.collidepoint(mouse_pos) and board.get_grid()[CELLS.index(cell)] == "free": # check if player clicked in a free cell
                        if len(previous_moves) == 0:
                            board.get_grid()[CELLS.index(cell)] = "O" # Player O goes first
                            previous_moves.append("O")
                        elif previous_moves[-1] == "X":
                            board.get_grid()[CELLS.index(cell)] = "O" # Alternate after that
                            previous_moves.append("O")
                        else:
                            board.get_grid()[CELLS.index(cell)] = "X" # Store move in board class variable
                            previous_moves.append("X")
                        break          
        draw_window(board) # Update game with new move
        game_over = False
        rematch = False
        for symbol in ["O", "X"]:
            winner_message = f"Player {symbol} wins!! Rematch?"
            if board.has_player_won((symbol)):
                game_over = True
                if draw_winner(winner_message):
                    rematch = True
        if game_over:
            break
        if board.is_game_drawn():
            if draw_draw("Game drawn!! Rematch?"):
                rematch = True
                break
    if rematch:
        main()
    pygame.quit()

if __name__ == "__main__":
    main()
