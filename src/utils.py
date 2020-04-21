import pygame


# NOTE: For .gif files, use an gif to sprite sheet converter (ex: ezgif.com)
class SpriteSheet:
    def __init__(self, image_name):
        """ Takes string argument of file path to sprite sheet"""
        self.image = pygame.image.load(image_name).convert()

    def get_sprite(self, x, y, width, height):
        # Grab a sprite out of a larger sprite sheet
        sprite = pygame.Surface((width, height))
        sprite.blit(self.image, (0, 0), (x, y, width, height))
        sprite = pygame.transform.scale(sprite, (width*2, height*2))
        sprite.set_colorkey((0, 0, 0))
        return sprite
