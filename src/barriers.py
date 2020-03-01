import pygame
from src.constants import *

barrierSprites = pygame.sprite.Group()

class Obstacles(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('resources/sprites/blockade2.png')
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH / 2
        self.rect.y = SCREEN_HEIGHT / 2
        
'''    
    def walls(self):
        super().walls()
        self.image = pygame.Surface((1190,360))
        self.image.fill((255,255,0))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
'''