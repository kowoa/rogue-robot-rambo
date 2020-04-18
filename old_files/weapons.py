import pygame
import pymunk
from old_files.utilities import convert_coordinates


class Pistol(pygame.sprite.Sprite):
    def __init__(self, space, pos=(0, 0)):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill((0, 128, 0))
        self.rect = self.image.get_rect(center=pos)

        mass = 1
        moment = pymunk.moment_for_box(mass, (self.rect.width, self.rect.height))
        self.body = pymunk.Body(mass, moment)
        self.body.position = convert_coordinates(pos)
        self.shape = pymunk.Poly.create_box(self.body, (self.rect.width, self.rect.height))
        self.shape.friction = 0.2
        space.add(self.body, self.shape)

    def update(self):
        self.rect.center = convert_coordinates(self.body.position)