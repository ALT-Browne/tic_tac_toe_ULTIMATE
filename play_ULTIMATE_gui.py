import pygame
from tic_tac_toe_class import *
pygame.init()

INFO = pygame.display.Info()
MONITOR_HEIGHT = INFO.current_h

SQUARE_LENGTH = MONITOR_HEIGHT // 2
WIN = pygame.display.set_mode((SQUARE_LENGTH, SQUARE_LENGTH))
pygame.display.set_caption("tic-tac-toe-ULTIMATE")
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0, 127)
CADET_BLUE = (152, 255, 255)
WINNER_FONT = pygame.font.SysFont('comicsans', SQUARE_LENGTH // 10)
DRAW_FONT = pygame.font.SysFont('comicsans', SQUARE_LENGTH // 10)

GRID_VERT_WIDTH = SQUARE_LENGTH / 300 # Used in big grid
GRID_HORIZ_HEIGHT = SQUARE_LENGTH / 300
LETTER_LENGTH = (SQUARE_LENGTH - 2 * GRID_VERT_WIDTH) / 3 # since 3*LETTER_LENGTH + 2*GRID_VERT_WIDTH = SQUARE_LENGTH
GRID_VERT_WIDTH_SUB = SQUARE_LENGTH / 600 # Used in sub-grids
GRID_HORIZ_HEIGHT_SUB = SQUARE_LENGTH / 600
LETTER_LENGTH_SUB = (LETTER_LENGTH - 2 * GRID_VERT_WIDTH_SUB) / 3 # since 3*LETTER_LENGTH_SUB + 2*GRID_VERT_WIDTH_SUB = LETTER_LENGTH

LETTER_X_IMAGE = pygame.image.load("images/letter_x_image.png")
LETTER_X_IMAGE_BLUE = pygame.image.load("images/letter_x_image_blue.png")
LETTER_X = pygame.transform.scale(LETTER_X_IMAGE_BLUE, (int(round(LETTER_LENGTH)), int(round(LETTER_LENGTH)))) # Used in big grid
LETTER_X_SUB = pygame.transform.scale(LETTER_X_IMAGE, (int(round(LETTER_LENGTH_SUB)), int(round(LETTER_LENGTH_SUB)))) # Used in sub-grids
LETTER_O_IMAGE = pygame.image.load("images/letter_o_image.png")
LETTER_O_IMAGE_BLUE = pygame.image.load("images/letter_o_image_blue.png")
LETTER_O = pygame.transform.scale(LETTER_O_IMAGE_BLUE, (int(round(LETTER_LENGTH)), int(round(LETTER_LENGTH))))
LETTER_O_SUB = pygame.transform.scale(LETTER_O_IMAGE, (int(round(LETTER_LENGTH_SUB)), int(round(LETTER_LENGTH_SUB))))

# The following rectangles represent the big vertical and horizontal lines used in the big grid
# Similarly the letter locations and cells are for the big grid

GRID_VERT_1 = pygame.Rect(LETTER_LENGTH, 0, GRID_VERT_WIDTH, SQUARE_LENGTH)
GRID_VERT_2 = pygame.Rect(2 * LETTER_LENGTH + GRID_VERT_WIDTH, 0, GRID_VERT_WIDTH, SQUARE_LENGTH)
GRID_HORIZ_1 = pygame.Rect(0, LETTER_LENGTH, SQUARE_LENGTH, GRID_HORIZ_HEIGHT)
GRID_HORIZ_2 = pygame.Rect(0, 2 * LETTER_LENGTH + GRID_HORIZ_HEIGHT, SQUARE_LENGTH, GRID_HORIZ_HEIGHT)

LETTER_LOCATIONS = [(0, 0), (GRID_VERT_1.right, 0), (GRID_VERT_2.right, 0), (0, GRID_HORIZ_1.bottom), 
                                    (GRID_VERT_1.right, GRID_HORIZ_1.bottom), (GRID_VERT_2.right, GRID_HORIZ_1.bottom), 
                                    (0, GRID_HORIZ_2.bottom), (GRID_VERT_1.right, GRID_HORIZ_2.bottom), (GRID_VERT_2.right, GRID_HORIZ_2.bottom)]

CELLS = [pygame.Rect(item[0], item[1], LETTER_LENGTH, LETTER_LENGTH) for item in LETTER_LOCATIONS] # Represent grid cells as pygame rectangles

# The following rectangles represent the small vertical and horizontal lines of each subgrid. The last two digits ij stand for the j'th vert or horiz within sub-grid i.
# Similarly the letter locations and cells are for the correspoding sub-grid

GRID_VERT_01 = pygame.Rect(LETTER_LENGTH_SUB, 0, GRID_VERT_WIDTH_SUB, LETTER_LENGTH)
GRID_VERT_02 = pygame.Rect(2 * LETTER_LENGTH_SUB + GRID_VERT_WIDTH_SUB, 0, GRID_VERT_WIDTH_SUB, LETTER_LENGTH)
GRID_HORIZ_01 = pygame.Rect(0, LETTER_LENGTH_SUB, LETTER_LENGTH, GRID_HORIZ_HEIGHT_SUB)
GRID_HORIZ_02 = pygame.Rect(0, 2 * LETTER_LENGTH_SUB + GRID_HORIZ_HEIGHT_SUB, LETTER_LENGTH, GRID_HORIZ_HEIGHT_SUB)

LETTER_LOCATIONS_0 = [(0, 0), (GRID_VERT_01.right, 0), (GRID_VERT_02.right, 0), (0, GRID_HORIZ_01.bottom), 
                                    (GRID_VERT_01.right, GRID_HORIZ_01.bottom), (GRID_VERT_02.right, GRID_HORIZ_01.bottom), 
                                    (0, GRID_HORIZ_02.bottom), (GRID_VERT_01.right, GRID_HORIZ_02.bottom), (GRID_VERT_02.right, GRID_HORIZ_02.bottom)]

CELLS_0 = [pygame.Rect(item[0], item[1], LETTER_LENGTH_SUB, LETTER_LENGTH_SUB) for item in LETTER_LOCATIONS_0]

GRID_VERT_11 = pygame.Rect(LETTER_LENGTH_SUB + LETTER_LENGTH + GRID_VERT_WIDTH, 0, GRID_VERT_WIDTH_SUB, LETTER_LENGTH)
GRID_VERT_12 = pygame.Rect(2 * LETTER_LENGTH_SUB + GRID_VERT_WIDTH_SUB + LETTER_LENGTH + GRID_VERT_WIDTH, 0, GRID_VERT_WIDTH_SUB, LETTER_LENGTH)
GRID_HORIZ_11 = pygame.Rect(LETTER_LENGTH + GRID_VERT_WIDTH, LETTER_LENGTH_SUB, LETTER_LENGTH, GRID_HORIZ_HEIGHT_SUB)
GRID_HORIZ_12 = pygame.Rect(LETTER_LENGTH + GRID_VERT_WIDTH, 2 * LETTER_LENGTH_SUB + GRID_HORIZ_HEIGHT_SUB, LETTER_LENGTH, GRID_HORIZ_HEIGHT_SUB)

LETTER_LOCATIONS_1 = [(GRID_VERT_1.right, 0), (GRID_VERT_11.right, 0), (GRID_VERT_12.right, 0), (GRID_VERT_1.right, GRID_HORIZ_11.bottom), 
                                    (GRID_VERT_11.right, GRID_HORIZ_11.bottom), (GRID_VERT_12.right, GRID_HORIZ_11.bottom), 
                                    (GRID_VERT_1.right, GRID_HORIZ_12.bottom), (GRID_VERT_11.right, GRID_HORIZ_12.bottom), (GRID_VERT_12.right, GRID_HORIZ_12.bottom)]

CELLS_1 = [pygame.Rect(item[0], item[1], LETTER_LENGTH_SUB, LETTER_LENGTH_SUB) for item in LETTER_LOCATIONS_1]

GRID_VERT_21 = pygame.Rect(LETTER_LENGTH_SUB + 2 * LETTER_LENGTH + 2 * GRID_VERT_WIDTH, 0, GRID_VERT_WIDTH_SUB, LETTER_LENGTH)
GRID_VERT_22 = pygame.Rect(2 * LETTER_LENGTH_SUB + GRID_VERT_WIDTH_SUB + 2 * LETTER_LENGTH + 2 * GRID_VERT_WIDTH, 0, GRID_VERT_WIDTH_SUB, LETTER_LENGTH)
GRID_HORIZ_21 = pygame.Rect(2 * LETTER_LENGTH + 2 * GRID_VERT_WIDTH, LETTER_LENGTH_SUB, LETTER_LENGTH, GRID_HORIZ_HEIGHT_SUB)
GRID_HORIZ_22 = pygame.Rect(2 * LETTER_LENGTH + 2 * GRID_VERT_WIDTH, 2 * LETTER_LENGTH_SUB + GRID_HORIZ_HEIGHT_SUB, LETTER_LENGTH, GRID_HORIZ_HEIGHT_SUB)

LETTER_LOCATIONS_2 = [(GRID_VERT_2.right, 0), (GRID_VERT_21.right, 0), (GRID_VERT_22.right, 0), (GRID_VERT_2.right, GRID_HORIZ_21.bottom), 
                                    (GRID_VERT_21.right, GRID_HORIZ_21.bottom), (GRID_VERT_22.right, GRID_HORIZ_21.bottom), 
                                    (GRID_VERT_2.right, GRID_HORIZ_22.bottom), (GRID_VERT_21.right, GRID_HORIZ_22.bottom), (GRID_VERT_22.right, GRID_HORIZ_22.bottom)]

CELLS_2 = [pygame.Rect(item[0], item[1], LETTER_LENGTH_SUB, LETTER_LENGTH_SUB) for item in LETTER_LOCATIONS_2]

GRID_VERT_31 = pygame.Rect(LETTER_LENGTH_SUB, LETTER_LENGTH + GRID_HORIZ_HEIGHT, GRID_VERT_WIDTH_SUB, LETTER_LENGTH)
GRID_VERT_32 = pygame.Rect(2 * LETTER_LENGTH_SUB + GRID_VERT_WIDTH_SUB, LETTER_LENGTH + GRID_HORIZ_HEIGHT, GRID_VERT_WIDTH_SUB, LETTER_LENGTH)
GRID_HORIZ_31 = pygame.Rect(0, LETTER_LENGTH_SUB + LETTER_LENGTH + GRID_HORIZ_HEIGHT, LETTER_LENGTH, GRID_HORIZ_HEIGHT_SUB)
GRID_HORIZ_32 = pygame.Rect(0, 2 * LETTER_LENGTH_SUB + GRID_HORIZ_HEIGHT_SUB + LETTER_LENGTH + GRID_HORIZ_HEIGHT, LETTER_LENGTH, GRID_HORIZ_HEIGHT_SUB)

LETTER_LOCATIONS_3 = [(0, GRID_HORIZ_1.bottom), (GRID_VERT_31.right, GRID_HORIZ_1.bottom), (GRID_VERT_32.right, GRID_HORIZ_1.bottom), (0, GRID_HORIZ_31.bottom), (GRID_VERT_31.right, GRID_HORIZ_31.bottom), (GRID_VERT_32.right, GRID_HORIZ_31.bottom), (0, GRID_HORIZ_32.bottom), (GRID_VERT_31.right, GRID_HORIZ_32.bottom), (GRID_VERT_32.right, GRID_HORIZ_32.bottom)]

CELLS_3 = [pygame.Rect(item[0], item[1], LETTER_LENGTH_SUB, LETTER_LENGTH_SUB) for item in LETTER_LOCATIONS_3]

GRID_VERT_41 = pygame.Rect(LETTER_LENGTH_SUB + LETTER_LENGTH + GRID_VERT_WIDTH, LETTER_LENGTH + GRID_HORIZ_HEIGHT, GRID_VERT_WIDTH_SUB, LETTER_LENGTH)
GRID_VERT_42 = pygame.Rect(2 * LETTER_LENGTH_SUB + GRID_VERT_WIDTH_SUB + LETTER_LENGTH + GRID_VERT_WIDTH, LETTER_LENGTH + GRID_HORIZ_HEIGHT, GRID_VERT_WIDTH_SUB, LETTER_LENGTH)
GRID_HORIZ_41 = pygame.Rect(LETTER_LENGTH + GRID_VERT_WIDTH, LETTER_LENGTH_SUB + LETTER_LENGTH + GRID_HORIZ_HEIGHT, LETTER_LENGTH, GRID_HORIZ_HEIGHT_SUB)
GRID_HORIZ_42 = pygame.Rect(LETTER_LENGTH + GRID_VERT_WIDTH, 2 * LETTER_LENGTH_SUB + GRID_HORIZ_HEIGHT_SUB + LETTER_LENGTH + GRID_HORIZ_HEIGHT, LETTER_LENGTH, GRID_HORIZ_HEIGHT_SUB)

LETTER_LOCATIONS_4 = [(GRID_VERT_1.right, GRID_HORIZ_1.bottom), (GRID_VERT_41.right, GRID_HORIZ_1.bottom), (GRID_VERT_42.right, GRID_HORIZ_1.bottom), (GRID_VERT_1.right, GRID_HORIZ_41.bottom), 
                                    (GRID_VERT_41.right, GRID_HORIZ_41.bottom), (GRID_VERT_42.right, GRID_HORIZ_41.bottom), 
                                    (GRID_VERT_1.right, GRID_HORIZ_42.bottom), (GRID_VERT_41.right, GRID_HORIZ_42.bottom), (GRID_VERT_42.right, GRID_HORIZ_42.bottom)]

CELLS_4 = [pygame.Rect(item[0], item[1], LETTER_LENGTH_SUB, LETTER_LENGTH_SUB) for item in LETTER_LOCATIONS_4]

GRID_VERT_51 = pygame.Rect(LETTER_LENGTH_SUB + 2 * LETTER_LENGTH + 2 * GRID_VERT_WIDTH, LETTER_LENGTH + GRID_HORIZ_HEIGHT, GRID_VERT_WIDTH_SUB, LETTER_LENGTH)
GRID_VERT_52 = pygame.Rect(2 * LETTER_LENGTH_SUB + GRID_VERT_WIDTH_SUB + 2 * LETTER_LENGTH + 2 * GRID_VERT_WIDTH, LETTER_LENGTH + GRID_HORIZ_HEIGHT, GRID_VERT_WIDTH_SUB, LETTER_LENGTH)
GRID_HORIZ_51 = pygame.Rect(2 * LETTER_LENGTH + 2 * GRID_VERT_WIDTH, LETTER_LENGTH_SUB + LETTER_LENGTH + GRID_HORIZ_HEIGHT, LETTER_LENGTH, GRID_HORIZ_HEIGHT_SUB)
GRID_HORIZ_52 = pygame.Rect(2 * LETTER_LENGTH + 2 * GRID_VERT_WIDTH, 2 * LETTER_LENGTH_SUB + GRID_HORIZ_HEIGHT_SUB + LETTER_LENGTH + GRID_HORIZ_HEIGHT, LETTER_LENGTH, GRID_HORIZ_HEIGHT_SUB)

LETTER_LOCATIONS_5 = [(GRID_VERT_2.right, GRID_HORIZ_1.bottom), (GRID_VERT_51.right, GRID_HORIZ_1.bottom), (GRID_VERT_52.right, GRID_HORIZ_1.bottom), (GRID_VERT_2.right, GRID_HORIZ_51.bottom), 
                                    (GRID_VERT_51.right, GRID_HORIZ_51.bottom), (GRID_VERT_52.right, GRID_HORIZ_51.bottom), 
                                    (GRID_VERT_2.right, GRID_HORIZ_52.bottom), (GRID_VERT_51.right, GRID_HORIZ_52.bottom), (GRID_VERT_52.right, GRID_HORIZ_52.bottom)]

CELLS_5 = [pygame.Rect(item[0], item[1], LETTER_LENGTH_SUB, LETTER_LENGTH_SUB) for item in LETTER_LOCATIONS_5]

GRID_VERT_61 = pygame.Rect(LETTER_LENGTH_SUB, 2 * LETTER_LENGTH + 2 * GRID_HORIZ_HEIGHT, GRID_VERT_WIDTH_SUB, LETTER_LENGTH)
GRID_VERT_62 = pygame.Rect(2 * LETTER_LENGTH_SUB + GRID_VERT_WIDTH_SUB, 2 * LETTER_LENGTH + 2 * GRID_HORIZ_HEIGHT, GRID_VERT_WIDTH_SUB, LETTER_LENGTH)
GRID_HORIZ_61 = pygame.Rect(0, LETTER_LENGTH_SUB + 2 * LETTER_LENGTH + 2 * GRID_HORIZ_HEIGHT, LETTER_LENGTH, GRID_HORIZ_HEIGHT_SUB)
GRID_HORIZ_62 = pygame.Rect(0, 2 * LETTER_LENGTH_SUB + GRID_HORIZ_HEIGHT_SUB + 2 * LETTER_LENGTH + 2 * GRID_HORIZ_HEIGHT, LETTER_LENGTH, GRID_HORIZ_HEIGHT_SUB)

LETTER_LOCATIONS_6 = [(0, GRID_HORIZ_2.bottom), (GRID_VERT_61.right, GRID_HORIZ_2.bottom), (GRID_VERT_62.right, GRID_HORIZ_2.bottom), (0, GRID_HORIZ_61.bottom), 
                                    (GRID_VERT_61.right, GRID_HORIZ_61.bottom), (GRID_VERT_62.right, GRID_HORIZ_61.bottom), 
                                    (0, GRID_HORIZ_62.bottom), (GRID_VERT_61.right, GRID_HORIZ_62.bottom), (GRID_VERT_62.right, GRID_HORIZ_62.bottom)]

CELLS_6 = [pygame.Rect(item[0], item[1], LETTER_LENGTH_SUB, LETTER_LENGTH_SUB) for item in LETTER_LOCATIONS_6]

GRID_VERT_71 = pygame.Rect(LETTER_LENGTH_SUB + LETTER_LENGTH + GRID_VERT_WIDTH, 2 * LETTER_LENGTH + 2 * GRID_HORIZ_HEIGHT, GRID_VERT_WIDTH_SUB, LETTER_LENGTH)
GRID_VERT_72 = pygame.Rect(2 * LETTER_LENGTH_SUB + GRID_VERT_WIDTH_SUB + LETTER_LENGTH + GRID_VERT_WIDTH, 2 * LETTER_LENGTH + 2 * GRID_HORIZ_HEIGHT, GRID_VERT_WIDTH_SUB, LETTER_LENGTH)
GRID_HORIZ_71 = pygame.Rect(LETTER_LENGTH + GRID_VERT_WIDTH, LETTER_LENGTH_SUB + 2 * LETTER_LENGTH + 2 * GRID_HORIZ_HEIGHT, LETTER_LENGTH, GRID_HORIZ_HEIGHT_SUB)
GRID_HORIZ_72 = pygame.Rect(LETTER_LENGTH + GRID_VERT_WIDTH, 2 * LETTER_LENGTH_SUB + GRID_HORIZ_HEIGHT_SUB + 2 * LETTER_LENGTH + 2 * GRID_HORIZ_HEIGHT, LETTER_LENGTH, GRID_HORIZ_HEIGHT_SUB)

LETTER_LOCATIONS_7 = [(GRID_VERT_1.right, GRID_HORIZ_2.bottom), (GRID_VERT_71.right, GRID_HORIZ_2.bottom), (GRID_VERT_72.right, GRID_HORIZ_2.bottom), (GRID_VERT_1.right, GRID_HORIZ_71.bottom), 
                                    (GRID_VERT_71.right, GRID_HORIZ_71.bottom), (GRID_VERT_72.right, GRID_HORIZ_71.bottom), 
                                    (GRID_VERT_1.right, GRID_HORIZ_72.bottom), (GRID_VERT_71.right, GRID_HORIZ_72.bottom), (GRID_VERT_72.right, GRID_HORIZ_72.bottom)]

CELLS_7 = [pygame.Rect(item[0], item[1], LETTER_LENGTH_SUB, LETTER_LENGTH_SUB) for item in LETTER_LOCATIONS_7]

GRID_VERT_81 = pygame.Rect(LETTER_LENGTH_SUB + 2 * LETTER_LENGTH + 2 * GRID_VERT_WIDTH, 2 * LETTER_LENGTH + 2 * GRID_HORIZ_HEIGHT, GRID_VERT_WIDTH_SUB, LETTER_LENGTH)
GRID_VERT_82 = pygame.Rect(2 * LETTER_LENGTH_SUB + GRID_VERT_WIDTH_SUB + 2 * LETTER_LENGTH + 2 * GRID_VERT_WIDTH, 2 * LETTER_LENGTH + 2 * GRID_HORIZ_HEIGHT, GRID_VERT_WIDTH_SUB, LETTER_LENGTH)
GRID_HORIZ_81 = pygame.Rect(2 * LETTER_LENGTH + 2 * GRID_VERT_WIDTH, LETTER_LENGTH_SUB + 2 * LETTER_LENGTH + 2 * GRID_HORIZ_HEIGHT, LETTER_LENGTH, GRID_HORIZ_HEIGHT_SUB)
GRID_HORIZ_82 = pygame.Rect(2 * LETTER_LENGTH + 2 * GRID_VERT_WIDTH, 2 * LETTER_LENGTH_SUB + GRID_HORIZ_HEIGHT_SUB + 2 * LETTER_LENGTH + 2 * GRID_HORIZ_HEIGHT, LETTER_LENGTH, GRID_HORIZ_HEIGHT_SUB)

LETTER_LOCATIONS_8 = [(GRID_VERT_2.right, GRID_HORIZ_2.bottom), (GRID_VERT_81.right, GRID_HORIZ_2.bottom), (GRID_VERT_82.right, GRID_HORIZ_2.bottom), (GRID_VERT_2.right, GRID_HORIZ_81.bottom), 
                                    (GRID_VERT_81.right, GRID_HORIZ_81.bottom), (GRID_VERT_82.right, GRID_HORIZ_81.bottom), 
                                    (GRID_VERT_2.right, GRID_HORIZ_82.bottom), (GRID_VERT_81.right, GRID_HORIZ_82.bottom), (GRID_VERT_82.right, GRID_HORIZ_82.bottom)]

CELLS_8 = [pygame.Rect(item[0], item[1], LETTER_LENGTH_SUB, LETTER_LENGTH_SUB) for item in LETTER_LOCATIONS_8]

SUB_GRID_CELLS = [CELLS_0, CELLS_1, CELLS_2, CELLS_3, CELLS_4, CELLS_5, CELLS_6, CELLS_7, CELLS_8]

SUB_GRID_LETTER_LOCATIONS = [LETTER_LOCATIONS_0, LETTER_LOCATIONS_1, LETTER_LOCATIONS_2, LETTER_LOCATIONS_3, LETTER_LOCATIONS_4, LETTER_LOCATIONS_5, LETTER_LOCATIONS_6, LETTER_LOCATIONS_7, LETTER_LOCATIONS_8]

SMALL_GRID_LINES = [GRID_VERT_01, GRID_VERT_02, GRID_HORIZ_01, GRID_HORIZ_02, GRID_VERT_11, GRID_VERT_12, GRID_HORIZ_11, GRID_HORIZ_12, GRID_VERT_21, GRID_VERT_22, GRID_HORIZ_21, GRID_HORIZ_22, GRID_VERT_31, GRID_VERT_32, GRID_HORIZ_31, GRID_HORIZ_32, GRID_VERT_41, GRID_VERT_42, GRID_HORIZ_41, GRID_HORIZ_42, GRID_VERT_51, GRID_VERT_52, GRID_HORIZ_51, GRID_HORIZ_52, GRID_VERT_61, GRID_VERT_62, GRID_HORIZ_61, GRID_HORIZ_62, GRID_VERT_71, GRID_VERT_72, GRID_HORIZ_71, GRID_HORIZ_72, GRID_VERT_81, GRID_VERT_82, GRID_HORIZ_81, GRID_HORIZ_82]

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
