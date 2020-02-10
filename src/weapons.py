import pygame

width = 1280
height = 720

class Gun(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/sprites/desert_hawk.png')
        self.image = pygame.transform.scale(self.image, (32,32))
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (170, 130)
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0

        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speedx = -5
        elif keystate[pygame.K_d]:
            self.speedx = 5
        elif keystate[pygame.K_w]:
            self.speedy = -5
        elif keystate[pygame.K_s]:
            self.speedy = 5

        self.rect.x += self.speedx
        self.rect.y += self.speedy
    
    def shoot(self):
        bullet = Bullets(self.rect.right, self.rect.center)
        weaponSprites.add(bullet)

class Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/sprites/bulletStrip.png')
        self.image = pygame.transform.scale(self.image, (32,32))
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.right = x
        self.rect.center = y
        self.speedx = 15

    def update(self):
        self.rect.x += self.speedx
        if self.rect.bottom < width:
            self.kill()