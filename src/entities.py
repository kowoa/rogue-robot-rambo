import pygame
from src.constants import *

class Player(pygame.sprite.Sprite):
    # Takes gun sprite parameter
    def __init__(self, gun):
        super().__init__()
        self.image = pygame.image.load("resources/sprites/newBoss.png")
        self.rect = self.image.get_rect()

    def update(self, dt, (gunPosX, gunPosY)):
        pressed = pygame.key.get_pressed()
        # dt is current FPS; movement updates every FPS/dividend frames; change dividend to change base movement speed
        move = dt / 5

        # Handles playing movement (WASD)
        if pressed[pygame.K_w]:
            if self.rect.y > -move: self.rect.move_ip(0, -move)
            if self.rect.y <= -move: self.rect.move_ip(0, move)
        if pressed[pygame.K_a]:
            if self.rect.x > -move: self.rect.move_ip(-move, 0)
            if self.rect.x <= -move: self.rect.move_ip(move, 0)
        if pressed[pygame.K_s]:
            if self.rect.y < SCREEN_HEIGHT - self.rect.height + move: self.rect.move_ip(0, move)
            if self.rect.y >= SCREEN_HEIGHT - self.rect.height + move: self.rect.move_ip(0, -move)
        if pressed[pygame.K_d]:
            if self.rect.x < SCREEN_WIDTH - self.rect.width + move: self.rect.move_ip(move, 0)
            if self.rect.x >= SCREEN_WIDTH - self.rect.width + move: self.rect.move_ip(-move, 0)

        return gun

class Gun(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("resources/sprites/desert_hawk.png")
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()

    def update(self, dt):
        pressed = pygame.key.get_pressed()
        # dt is current FPS; movement updates every FPS/dividend frames; change dividend to change base movement speed
        move = dt / 5

        # Handles playing movement (WASD)
        if pressed[pygame.K_w]:
            if self.rect.y > -move: self.rect.move_ip(0, -move)
            if self.rect.y <= -move: self.rect.move_ip(0, move)
        if pressed[pygame.K_a]:
            if self.rect.x > -move: self.rect.move_ip(-move, 0)
            if self.rect.x <= -move: self.rect.move_ip(move, 0)
        if pressed[pygame.K_s]:
            if self.rect.y < SCREEN_HEIGHT - self.rect.height + move: self.rect.move_ip(0, move)
            if self.rect.y >= SCREEN_HEIGHT - self.rect.height + move: self.rect.move_ip(0, -move)
        if pressed[pygame.K_d]:
            if self.rect.x < SCREEN_WIDTH - self.rect.width + move: self.rect.move_ip(move, 0)
            if self.rect.x >= SCREEN_WIDTH - self.rect.width + move: self.rect.move_ip(-move, 0)
'''
        if pressed[pygame.K_UP]:
            self.rect.x = pos[0]
            self.rect.y = pos[1] - 20'''


'''
class Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/sprites/bulletStrip.png')
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.right = x
        self.rect.center = y
        self.speedx = 15

    def update(self):
        self.rect.x += self.speedx
        if self.rect.bottom < width:
            self.kill()'''