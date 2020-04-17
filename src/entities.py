import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self, image_path, x=0, y=0):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

class Player(Entity):
    def __init__(self, image_path, x=0, y=0):
        super().__init__(image_path, x, y)
    
    def update(self):
        pass

class Boss(Entity):
    def __init__(self, image_path, x=0, y=0):
        super().__init__(image_path, x, y)

    def update(self):
        pass

