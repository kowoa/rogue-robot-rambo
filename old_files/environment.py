import pygame
import pymunk
from old_files.utilities import convert_coordinates


class Platform(pygame.sprite.Sprite):
    def __init__(self, space, pos=(0, 0), size=(64, 64)):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=pos)

        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.body.position = convert_coordinates(pos)
        self.shape = pymunk.Poly.create_box(self.body, (self.rect.width, self.rect.height))
        self.shape.friction = 0.8
        space.add(self.body, self.shape)

class Border():
    pass