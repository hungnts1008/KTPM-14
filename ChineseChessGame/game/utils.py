import pygame
import os

pygame.init()
pygame.font.init()

# Width and height of the application
info = pygame.display.Info()
WIN_WIDTH = info.current_w
WIN_HEIGHT = info.current_h

# Red side, blue side indicator
RED_SIDE = RED_TURN = 1
BLUE_SIDE = BLUE_TURN = 0


class Color:
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)  # Sửa lại màu xanh dương đúng
    YELLOW = (255, 255, 0)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    PURPLE = (128, 0, 128)
    ORANGE = (255, 165, 0)
    GREY = (128, 128, 128)
    TURQUOISE = (64, 224, 208)


class Font:
    FONT_DIR = os.path.join(os.path.dirname(__file__), "../fonts")
    SCORE_TEXT_FONT = pygame.font.Font(os.path.join(FONT_DIR, "CursedTimerUlil-Aznm.ttf"), 30)
    SCORE_FONT = pygame.font.Font(os.path.join(FONT_DIR, "CursedTimerUlil-Aznm.ttf"), 30)
    SCORE_FONT.set_bold(True)
    NORMAL_FONT = pygame.font.Font(os.path.join(FONT_DIR, "Poppins-Bold.ttf"), 30)
    WRITING_FONT = pygame.font.Font(os.path.join(FONT_DIR, "Allison-Regular.ttf"), 30)
    SMALL_FONT = pygame.font.SysFont("Times New Roman", 30)


class ChessImages:
    IMG_DIR = os.path.join(os.path.dirname(__file__), "../images/pieces")
    RED_CHARIOT = pygame.image.load(os.path.join(IMG_DIR, "red-car.png"))
    RED_CANNON = pygame.image.load(os.path.join(IMG_DIR, "red-cannon.png"))
    RED_HORSE = pygame.image.load(os.path.join(IMG_DIR, "red-horse.png"))
    RED_ELEPHANT = pygame.image.load(os.path.join(IMG_DIR, "red-elephant.png"))
    RED_SOLDIER = pygame.image.load(os.path.join(IMG_DIR, "red-pawn.png"))
    RED_ADVISOR = pygame.image.load(os.path.join(IMG_DIR, "red-bodyguard.png"))
    RED_LORD = pygame.image.load(os.path.join(IMG_DIR, "red-king.png"))

    BLUE_CHARIOT = pygame.image.load(os.path.join(IMG_DIR, "blue-car.png"))
    BLUE_CANNON = pygame.image.load(os.path.join(IMG_DIR, "blue-cannon.png"))
    BLUE_HORSE = pygame.image.load(os.path.join(IMG_DIR, "blue-horse.png"))
    BLUE_ELEPHANT = pygame.image.load(os.path.join(IMG_DIR, "blue-elephant.png"))
    BLUE_SOLDIER = pygame.image.load(os.path.join(IMG_DIR, "blue-pawn.png"))
    BLUE_ADVISOR = pygame.image.load(os.path.join(IMG_DIR, "blue-bodyguard.png"))
    BLUE_LORD = pygame.image.load(os.path.join(IMG_DIR, "blue-king.png"))
    