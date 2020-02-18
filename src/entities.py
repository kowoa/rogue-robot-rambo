import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("resources/sprites/newBoss.png")
        self.rect = self.image.get_rect()
        self.pos = pygame.Vector2((100, 200))

    def update(self, events, dt):
        pressed = pygame.key.get_pressed()
        move = pygame.Vector2((0, 0))
        if pressed[pygame.K_w]: move += (0, -1)
        if pressed[pygame.K_a]: move += (-1, 0)
        if pressed[pygame.K_s]: move += (0, 1)
        if pressed[pygame.K_d]: move += (1, 0)
        if move.length() > 0: move.normalize_ip()
        self.pos += move * (dt/5)
        self.rect.center = self.pos

class Bullets(pygame.sprite.Sprite):
    def __init__(self):
