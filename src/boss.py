import pygame as pg
from settings import *
from math import copysign
from bullets import *


class Boss(pg.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game

        # Add to sprite groups
        self.game.char_sprites.add(self)
        self.game.all_sprites.add(self)

        # Initialize pygame elements
        self.image = pg.Surface((36, 36))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(midtop=(SCREEN_WIDTH / 2, 10))

        # Initialize vectors for realistic movements
        self.pos = pg.Vector2(self.rect.midbottom)
        self.vel = pg.Vector2(0, 0)
        self.acc = pg.Vector2(0, 0)

        # Physics constants
        self.MAX_ACC = 1
        self.FRICTION = -0.12

        # Shooting
        self.last_shot_time = 0

    def collide_edge(self):
        if self.pos.x < 0:
            self.pos.x = 0
            self.vel.x = 0
        elif self.pos.x > SCREEN_WIDTH - self.rect.width:
            self.pos.x = SCREEN_WIDTH - self.rect.width
            self.vel.x = 0

    def track_player(self):
        # Predict and follow player (AI)
        dist_to_player_x = self.game.player.ft_pos.x - self.pos.x
        dist_to_player_x_norm = dist_to_player_x / (SCREEN_WIDTH / 2 - self.rect.width / 2)
        self.acc.x += copysign(1, dist_to_player_x_norm) * max(abs(dist_to_player_x_norm * self.MAX_ACC), 0.1)

    def shoot(self):
        now = pg.time.get_ticks()
        if now - self.last_shot_time > 1000:
            self.last_shot_time = now
            # Shoot bullet
            Bullet(self.game, self.pos, (0, 3))


    def update(self):
        self.acc = pg.Vector2(0, 0)
        self.collide_edge()
        self.track_player()
        self.shoot()

        self.acc += self.vel * self.FRICTION
        self.vel += self.acc
        self.pos += self.vel + (0.5 * self.acc)

        self.rect.midbottom = self.pos
