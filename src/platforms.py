import pygame as pg
from settings import *
from random import randint, choice, random


class Platform(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h, friction=-0.12):
        super().__init__()
        self.game = game
        self.image = pg.Surface((w, h))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(topleft=(x, y))

        # Add to sprite groups
        self.game.plat_sprites.add(self)
        self.game.all_sprites.add(self)

        # Different platforms have different frictions
        self.friction = friction

    def reproduce(self):
        # TODO: Fix platform generation --- if player goes up too fast, platforms don't spawn high enough
        # Put this method in here to make Game class cleaner
        # Spawn new platforms to keep similar number of platforms
        while len(self.game.plat_sprites) < 5:
            plat_width = randint(SCREEN_WIDTH//4, SCREEN_WIDTH//2)
            plat_pos_x = randint(0, SCREEN_WIDTH - plat_width)
            plat_pos_y = choice((-32, -64, -96))  # EDIT THIS TO FIX PLATFORM GENERATION
            #plat_friction = -random() / 4 - 0.05
            # New platform created and automatically added to sprite groups
            Platform(self.game, plat_pos_x, plat_pos_y, plat_width, 32)

    def cleanup(self):
        # Platforms below screen are removed
        if self.rect.top >= SCREEN_HEIGHT:
            self.kill()
            self.game.score += 10

    def update(self):
        self.cleanup()
        self.reproduce()


