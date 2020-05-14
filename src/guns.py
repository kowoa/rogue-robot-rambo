import pygame as pg
from settings import *
from paths import *
from bullets import *


class Gun(pg.sprite.Sprite):
    # Can be attached to a character sprite
    def __init__(self, game, char):
        super().__init__()
        self.game = game
        self.char = char

        self.game.all_sprites.add(self)
        self.game.gun_sprites.add(self)

        self.image = pg.image.load(gun_path).convert()
        self.image = pg.transform.scale(self.image, (28, 28))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        # Position relative to character (NOT the actual coordinate position of gun); used as direction
        self.attach_pos = pg.Vector2(1, 0)

        # Rotating images by angles not divisible by 90 auto-pads image; avoid using rotate
        self.imageEast = self.image
        self.imageWest = pg.transform.flip(self.image, 1, 0)

        self.shot_delay = 200
        self.last_shot_time = pg.time.get_ticks()
        self.bullet_speed = 5

    def shoot(self):
        pressed = pg.key.get_pressed()
        current_time = pg.time.get_ticks()
        if (pressed[pg.K_UP] or pressed[pg.K_LEFT] or pressed[pg.K_DOWN] or pressed[pg.K_RIGHT]) \
                and (current_time - self.last_shot_time > self.shot_delay):
            self.last_shot_time = current_time
            Bullet(self.game, self.rect.center, self.attach_pos)

    def update(self):
        pressed = pg.key.get_pressed()

        # Moves gun with player (WASD)
        if not pressed[pg.K_UP] and not pressed[pg.K_LEFT] and not pressed[pg.K_DOWN] and not pressed[pg.K_RIGHT]:
            if pressed[pg.K_w]:
                self.attach_pos += (0, -1)
            if pressed[pg.K_a]:
                self.attach_pos += (-1, 0)
                self.image = self.imageWest
            if pressed[pg.K_s]:
                self.attach_pos += (0, 1)
            if pressed[pg.K_d]:
                self.attach_pos += (1, 0)
                self.image = self.imageEast

        # Moves gun when aiming (Arrow keys)
        if pressed[pg.K_UP]:
            self.attach_pos += (0, -1)
        if pressed[pg.K_LEFT]:
            self.attach_pos += (-1, 0)
            if not pressed[pg.K_RIGHT]:
                self.image = self.imageWest
        if pressed[pg.K_DOWN]:
            self.attach_pos += (0, 1)
        if pressed[pg.K_RIGHT]:
            self.attach_pos += (1, 0)
            if not pressed[pg.K_LEFT]:
                self.image = self.imageEast

        # Normalization ensures consistent movement
        if self.attach_pos[0] + self.attach_pos[1] != 0:
            self.attach_pos.normalize_ip()

        # Adjust num in (self.pos[i] * num) for distance from player
        self.rect.x = self.char.pos.x + (self.attach_pos[0] * 50)
        self.rect.y = (self.char.pos.y - self.char.rect.h / 2) + (self.attach_pos[1] * 50)

        # Shoot
        self.attach_pos.scale_to_length(self.bullet_speed)
        self.shoot()

