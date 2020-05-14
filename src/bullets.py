import pygame as pg
from settings import *


class Bullet(pg.sprite.Sprite):
    # vel includes both magnitude and direction
    def __init__(self, game, pos=(0, 0), vel=(0, 0)):
        super().__init__()
        self.game = game

        self.game.all_sprites.add(self)
        self.game.bull_sprites.add(self)

        self.image = pg.Surface((8, 8))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect(center=pos)

        self.pos = pg.Vector2(self.rect.center)
        self.vel = pg.Vector2(vel)

    def cleanup(self):
        """ Remove bullet from memory if it is above or below the top or bottom of screen, respectively """
        if self.pos.y < -self.rect.h/2 or self.pos.y > SCREEN_HEIGHT + self.rect.h/2:
            self.kill()

    def wrap_around(self):
        """ Wrap around sides of screen """
        if self.pos.x < -self.rect.w/2:
            self.pos.x = SCREEN_WIDTH + self.rect.w/2
        if self.pos.x > SCREEN_WIDTH + self.rect.w/2:
            self.pos.x = -self.rect.w/2

    def move(self):
        self.pos += self.vel
        self.rect.center = self.pos

    def update(self):
        self.cleanup()
        self.wrap_around()
        self.move()





