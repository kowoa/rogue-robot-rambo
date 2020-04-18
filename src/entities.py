import pygame
import pymunk
from src.utilities import convert_to_pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, space, image_path, pos=(0, 0)):
        """
        Initialize player with elements from pygame and pymunk
        :param space: pymunk.Space() object
        :param image_path: string path to image file
        :param pos: initial position of player in pygame coordinates
        """
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(center=pos)

        mass = 1
        moment = 100000  # Set to high number so that player does not rotate
        self.body = pymunk.Body(mass, moment)
        self.body.position = pos
        self.shape = pymunk.Poly.create_box(self.body, (self.rect.width, self.rect.height))
        self.shape.friction = 0.9
        space.add(self.body, self.shape)

        self.is_jumping = False

    def controls(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_w] and not self.is_jumping:
            self.is_jumping = True


    def update(self):
        pos = convert_to_pygame(self.body.position)
        self.rect.center = pos
        print("{}{}".format(self.rect.center, self.body.position))

class Platform(pygame.sprite.Sprite):
    def __init__(self, space, image_path, pos=(0, 0)):
