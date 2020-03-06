import pygame
pygame.font.init()

# Screen
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Boss Battle!"
SCREEN_ICON = "resources/sprites/oubliette.png"
SCORE_FILE = "highscore.txt"
FPS = 60

# Fonts
FONT_SMALL = pygame.font.SysFont("monospace", 24)
FONT_MEDIUM = pygame.font.SysFont("monospace", 40)
FONT_LARGE = pygame.font.SysFont("monospace", 60)
FONT_XLARGE = pygame.font.SysFont("monospace", 80)