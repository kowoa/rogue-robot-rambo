import pygame
from src.settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

        self.pos = pygame.Vector2(self.rect.center)
        self.vel = pygame.Vector2(0, 0)
        self.acc = pygame.Vector2(0, 0)

    def update(self):
        keys = pygame.key.get_pressed()
        self.acc = pygame.Vector2(0, 0)

        # Horizontal controls
        if keys[pygame.K_a]:
            self.acc.x += -PLAYER_ACC
        if keys[pygame.K_d]:
            self.acc.x += PLAYER_ACC

        self.acc += self.vel * PLAYER_FRICTION  # Apply friction
        self.vel += self.acc
        self.pos += self.vel + (0.5 * self.acc)  # Kinematic equation

        # Wrap around sides of screen
        if self.pos.x < 0:
            self.pos.x = SCREEN_WIDTH
        if self.pos.x > SCREEN_WIDTH:
            self.pos.x = 0

        self.rect.center = self.pos

    def reset(self):
        pass

