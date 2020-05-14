import pygame as pg
from paths import *


class BackgroundMusic:
    def __init__(self):
        pg.mixer.music.load(blazer_rail_path)  # Placeholder
        pg.mixer.music.play(-1)

    def update(self):
        # FUTURE: update music depend on conditions and contexts
        pg.mixer.music.fadeout(500)

    def reset(self):
        pg.mixer.music.play(-1)