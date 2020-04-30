import pygame
from file_paths import *
from settings import *


class Platform(pygame.sprite.Sprite):
    def __init__(self, pos=(0, 0), size=(16, 16), friction=-0.12):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(topleft=pos)

        self.friction = friction

    def load_images(self):
        pass

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


class BackgroundMusic:
    def __init__(self):
        pygame.mixer.music.load(blazer_rail_path)  # Placeholder
        pygame.mixer.music.play(-1)

    def update(self):
        # FUTURE: update music depend on conditions and contexts
        pygame.mixer.music.fadeout(500)

    def reset(self):
        pygame.mixer.music.play(-1)

