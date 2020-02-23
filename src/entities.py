import pygame
from src.constants import *

playerSprites = pygame.sprite.Group()
bulletSprites = pygame.sprite.Group()

class Player(pygame.sprite.Sprite):
    # Takes gun sprite parameter
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("resources/sprites/newBoss.png")
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH / 2
        self.rect.y = SCREEN_HEIGHT / 2

    def move(self, dt):
        pressed = pygame.key.get_pressed()
        # dt is current FPS; movement updates every FPS/dividend frames; change dividend to change base movement speed
        move = dt / 5

        # Handles player movement (WASD)
        if pressed[pygame.K_w]:
            if self.rect.y > -move: self.rect.move_ip(0, -move)
            if self.rect.y <= -move: self.rect.move_ip(0, move)
        if pressed[pygame.K_a]:
            if self.rect.x > -move: self.rect.move_ip(-move, 0)
            if self.rect.x <= -move: self.rect.move_ip(move, 0)
        if pressed[pygame.K_s]:
            if self.rect.y < SCREEN_HEIGHT - self.rect.height + move: self.rect.move_ip(0, move)
            if self.rect.y >= SCREEN_HEIGHT - self.rect.height + move: self.rect.move_ip(0, -move)
        if pressed[pygame.K_d]:
            if self.rect.x < SCREEN_WIDTH - self.rect.width + move: self.rect.move_ip(move, 0)
            if self.rect.x >= SCREEN_WIDTH - self.rect.width + move: self.rect.move_ip(-move, 0)

class Gun(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("resources/sprites/desert_hawk.png")
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        # Position relative to player (NOT the actual coordinate position of gun); used as direction
        self.pos = pygame.Vector2(1, 1)

        self.rightImage = self.image
        self.leftImage = pygame.transform.flip(self.image, 1, 0)

        self.shootDelay = 200
        self.lastShotTime = pygame.time.get_ticks()

    def shoot(self):
        pressed = pygame.key.get_pressed()
        currentTime = pygame.time.get_ticks()
        if pressed[pygame.K_SPACE] and currentTime - self.lastShotTime > self.shootDelay:
            bullet = Bullet(self.rect.x, self.rect.y, self.pos)
            bulletSprites.add(bullet)
            self.lastShotTime = currentTime


    def move(self, dt, playerX, playerY):
        pressed = pygame.key.get_pressed()
        # dt is current FPS; movement updates every FPS/dividend frames; change dividend to change base movement speed
        move = dt / 5

        # Moves gun with player (WASD)
        if not pressed[pygame.K_UP] and not pressed[pygame.K_LEFT] and not pressed[pygame.K_DOWN] and not pressed[pygame.K_RIGHT]:
            if pressed[pygame.K_w]:
                self.rect.move_ip(0, -move)
                self.pos += (0, -1)
            if pressed[pygame.K_a]:
                self.rect.move_ip(-move, 0)
                self.pos += (-1, 0)
                self.image = self.leftImage
            if pressed[pygame.K_s]:
                self.rect.move_ip(0, move)
                self.pos += (0, 1)
            if pressed[pygame.K_d]:
                self.rect.move_ip(move, 0)
                self.pos += (1, 0)
                self.image = self.rightImage

        # Moves gun when aiming (Arrow keys)
        if pressed[pygame.K_UP]:
            self.pos += (0, -1)
        if pressed[pygame.K_LEFT]:
            self.pos += (-1, 0)
            if not pressed[pygame.K_RIGHT]:
                self.image = self.leftImage
        if pressed[pygame.K_DOWN]:
            self.pos += (0, 1)
        if pressed[pygame.K_RIGHT]:
            self.pos += (1, 0)
            if not pressed[pygame.K_LEFT]:
                self.image = self.rightImage

        # Normalization ensures consistent movement
        pygame.Vector2.normalize_ip(self.pos)

        self.shoot()

        # Adjust num in (self.pos[i] * num) for distance from player
        self.rect.x = playerX + (self.pos[0] * 50)
        self.rect.y = playerY + (self.pos[1] * 50)


class Bullet(pygame.sprite.Sprite):
    # Reminder that Python passes by object reference; when 'direction' changes in class Gun(),
    # the value in class Bullet() changes as well

    # Constructor take parameters initial x and y position to spawn and direction to shoot (used in Gun.shoot())
    def __init__(self, initX, initY, direction):
        super().__init__()
        self.image = pygame.image.load("resources/sprites/newBoss.png")
        self.rect = self.image.get_rect()
        self.rect.x = initX
        self.rect.y = initY
        # Force pass by value by making two separate variables to store X and Y direction
        self.dirX = direction[0]
        self.dirY = direction[1]


    def move(self, dt):
        move = dt / 5
        velX = self.dirX * move
        velY = self.dirY * move

        self.rect.move_ip(velX, velY)