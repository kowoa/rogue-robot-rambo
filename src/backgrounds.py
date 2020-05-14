import pygame
from paths import *
from settings import *


class GlacialBackground:
    def __init__(self, game):
        self.game = game
        self.layers = []
        self.load_images()

    def load_images(self):
        image = pygame.image.load(glacial_sky_path).convert_alpha()
        self.layers.append(image)
        image = pygame.image.load(glacial_mountains_path).convert_alpha()
        self.layers.append(image)
        image = pygame.image.load(glacial_clouds_bg_path).convert_alpha()
        self.layers.append(image)
        image = pygame.image.load(glacial_clouds_lonely_path).convert_alpha()
        self.layers.append(image)
        image = pygame.image.load(glacial_clouds_mg_3_path).convert_alpha()
        self.layers.append(image)
        image = pygame.image.load(glacial_clouds_mg_2_path).convert_alpha()
        self.layers.append(image)
        image = pygame.image.load(glacial_clouds_mg_1_path).convert_alpha()
        self.layers.append(image)
        for i in range(0, len(self.layers)):
            self.layers[i] = pygame.transform.scale(self.layers[i], (SCREEN_WIDTH, SCREEN_HEIGHT))

    def update(self):
        pass

    def draw(self):
        for layer in self.layers:
            self.game.screen.blit(layer, (0, 0))


class GrassyBackground:
    def __init__(self, game):
        self.game = game
        self.layers = []
        self.load_images()

    def load_images(self):
        image = pygame.image.load(grassy_sky_path).convert_alpha()
        self.layers.append(image)
        image = pygame.image.load(grassy_far_mountains_path).convert_alpha()
        self.layers.append(image)
        image = pygame.image.load(grassy_mountains_path).convert_alpha()
        self.layers.append(image)
        image = pygame.image.load(grassy_clouds_mid_path).convert_alpha()
        self.layers.append(image)
        image = pygame.image.load(grassy_hill_path).convert_alpha()
        self.layers.append(image)
        image = pygame.image.load(grassy_clouds_front_path).convert_alpha()
        self.layers.append(image)
        for i in range(0, len(self.layers)):
            self.layers[i] = pygame.transform.scale(self.layers[i], (SCREEN_WIDTH, SCREEN_HEIGHT))

    def update(self):
        pass



