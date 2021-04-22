import pygame
pygame.init()

INFO = pygame.display.Info()
MONITOR_HEIGHT = INFO.current_h

SQUARE_LENGTH = MONITOR_HEIGHT // 2

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
CADET_BLUE = (152, 255, 255)
WINNER_FONT = pygame.font.SysFont('comicsans', SQUARE_LENGTH // 10)
DRAW_FONT = pygame.font.SysFont('comicsans', SQUARE_LENGTH // 10)

GRID_VERT_WIDTH = SQUARE_LENGTH / 300
GRID_HORIZ_HEIGHT = SQUARE_LENGTH / 300
LETTER_LENGTH = (SQUARE_LENGTH - 2 * GRID_VERT_WIDTH) / 3 # since 3*LETTER_LENGTH + 2*GRID_VERT_WIDTH = SQUARE_LENGTH

GRID_VERT_1 = pygame.Rect(LETTER_LENGTH, 0, GRID_VERT_WIDTH, SQUARE_LENGTH)
GRID_VERT_2 = pygame.Rect(2 * LETTER_LENGTH + GRID_VERT_WIDTH, 0, GRID_VERT_WIDTH, SQUARE_LENGTH)
GRID_HORIZ_1 = pygame.Rect(0, LETTER_LENGTH, SQUARE_LENGTH, GRID_HORIZ_HEIGHT)
GRID_HORIZ_2 = pygame.Rect(0, 2 * LETTER_LENGTH + GRID_HORIZ_HEIGHT, SQUARE_LENGTH, GRID_HORIZ_HEIGHT)

LETTER_X_IMAGE = pygame.image.load("images/letter_x_image.png")
LETTER_X = pygame.transform.scale(LETTER_X_IMAGE, (int(round(LETTER_LENGTH)), int(round(LETTER_LENGTH))))
LETTER_O_IMAGE = pygame.image.load("images/letter_o_image.png")
LETTER_O = pygame.transform.scale(LETTER_O_IMAGE, (int(round(LETTER_LENGTH)), int(round(LETTER_LENGTH))))

LETTER_LOCATIONS = [(0, 0), (GRID_VERT_1.right, 0), (GRID_VERT_2.right, 0), (0, GRID_HORIZ_1.bottom), 
                                    (GRID_VERT_1.right, GRID_HORIZ_1.bottom), (GRID_VERT_2.right, GRID_HORIZ_1.bottom), 
                                    (0, GRID_HORIZ_2.bottom), (GRID_VERT_1.right, GRID_HORIZ_2.bottom), (GRID_VERT_2.right, GRID_HORIZ_2.bottom)]

CELLS = [pygame.Rect(item[0], item[1], LETTER_LENGTH, LETTER_LENGTH) for item in LETTER_LOCATIONS] # Represent grid cells as pygame rectangles