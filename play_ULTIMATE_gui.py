import pygame
from tic_tac_toe_class import *
from ultimate_gui_constants import *
pygame.init()

WIN = pygame.display.set_mode((SQUARE_LENGTH, SQUARE_LENGTH))
pygame.display.set_caption("tic-tac-toe-ULTIMATE")

def draw_window(board):
    """
    Draw the present state of the board in the game window.

    param board: instance of tic_tac_toe_ULTIMATE class.
    """
    WIN.fill(WHITE)
    if len(board.move_sequence) != 0 and not board.is_sub_grid_full(board.move_sequence[-1][2]):
        pygame.draw.rect(WIN, GREEN, CELLS[board.move_sequence[-1][2]])
    for i in range(0, 9):
        if board.get_big_grid()[i][0] == "O":
            WIN.blit(LETTER_O, LETTER_LOCATIONS[i])
        if board.get_big_grid()[i][0] == "X":
            WIN.blit(LETTER_X, LETTER_LOCATIONS[i])
    for i in range(0, 9):
        for j in range(0, 9): # Draw all symbols played in sub-grids
            if board.get_big_grid()[i][1].get_grid()[j] == "O": # Retrieve moves from board class variable
                WIN.blit(LETTER_O_SUB, SUB_GRID_LETTER_LOCATIONS[i][j])
            if board.get_big_grid()[i][1].get_grid()[j] == "X":
                WIN.blit(LETTER_X_SUB, SUB_GRID_LETTER_LOCATIONS[i][j])
    pygame.draw.rect(WIN, BLACK, GRID_VERT_1)
    pygame.draw.rect(WIN, BLACK, GRID_VERT_2)
    pygame.draw.rect(WIN, BLACK, GRID_HORIZ_1)
    pygame.draw.rect(WIN, BLACK, GRID_HORIZ_2)
    for line in SMALL_GRID_LINES:
        pygame.draw.rect(WIN, CADET_BLUE, line)
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

def handle_first_move(board, mouse_pos):
    """
    Find sub-grid cell where player clicked first move. Update board accordingly.

    param board: instance of tic_tac_toe_ULTIMATE class.

    param mouse_pos: tuple of ints 
    """
    for cells in SUB_GRID_CELLS:
        for cell in cells: # all cells are free for the first move
            if cell.collidepoint(mouse_pos): 
                board.update_big_grid("O", SUB_GRID_CELLS.index(cells), cells.index(cell)) # Player O goes first
                break
        else:
            continue
        break

def handle_free_move(board, mouse_pos):
    """
    Find sub-grid cell where player clicked free move. Update board accordingly.

    param board: instance of tic_tac_toe_ULTIMATE class.

    param mouse_pos: tuple of ints 
    """
    for i in board.get_non_full_sub_grids():
        for cell in SUB_GRID_CELLS[i]:
            if cell.collidepoint(mouse_pos) and board.get_big_grid()[i][1].get_grid()[SUB_GRID_CELLS[i].index(cell)] == "free": # check if player clicked in a free cell of any non-full sub-grid
                if board.move_sequence[-1][0] == "X":
                    board.update_big_grid("O", i, SUB_GRID_CELLS[i].index(cell)) # Play alternates.
                else:
                    board.update_big_grid("X", i, SUB_GRID_CELLS[i].index(cell))
                for j in range(0, 9):
                    if board.get_big_grid()[j][0] == "free":
                        for symbol in ["X", "O"]:
                            if board.has_player_won_sub_grid(symbol, j):
                                board.get_big_grid()[j][0] = symbol
                break
        else:
            continue
        break

def handle_next_move(board, mouse_pos):
    """
    Find cell in valid sub-grid where player clicked their move. Update board accordingly.

    param board: instance of tic_tac_toe_ULTIMATE class.

    param mouse_pos: tuple of ints 
    """
    for cell in SUB_GRID_CELLS[board.move_sequence[-1][2]]: # only check valid sub-grid
        if cell.collidepoint(mouse_pos) and board.get_big_grid()[board.move_sequence[-1][2]][1].get_grid()[SUB_GRID_CELLS[board.move_sequence[-1][2]].index(cell)] == "free": 
            if board.move_sequence[-1][0] == "X":
                board.update_big_grid("O", board.move_sequence[-1][2], SUB_GRID_CELLS[board.move_sequence[-1][2]].index(cell)) # Play alternates.
            else:
                board.update_big_grid("X", board.move_sequence[-1][2], SUB_GRID_CELLS[board.move_sequence[-1][2]].index(cell))
            for i in range(0, 9):
                if board.get_big_grid()[i][0] == "free":
                    for symbol in ["X", "O"]:
                        if board.has_player_won_sub_grid(symbol, i):
                            board.get_big_grid()[i][0] = symbol
            break

def main():
    board = tic_tac_toe_ULTIMATE()
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if len(board.move_sequence) == 0: # first move
                    handle_first_move(board, mouse_pos)
                elif board.is_sub_grid_full(board.move_sequence[-1][2]):
                    handle_free_move(board, mouse_pos)
                else:
                    handle_next_move(board, mouse_pos)
        draw_window(board) # Update game with new move
        game_over = False
        rematch = False
        for symbol in ["O", "X"]:
            winner_message = f"Player {symbol} wins!! Rematch?"
            if board.has_player_won((symbol)):
                game_over = True
                if draw_winner(winner_message):
                    rematch = True
                break
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
