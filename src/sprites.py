import pygame
from src.settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pygame.Surface((32, 32))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT - 40))

        self.pos = pygame.Vector2(self.rect.center)
        self.vel = pygame.Vector2(0, 0)
        self.acc = pygame.Vector2(0, 0)

        self.can_jump = True
        self.last_jump_time = pygame.time.get_ticks()

    def check_collisions(self):
        # Check and apply collisions with platforms
        test_value = 10 # Increase this value to increase strictness of collision
        self.rect.y -= test_value
        self.rect.x += test_value
        r_collisions = pygame.sprite.spritecollide(self, self.game.platform_sprites, False)
        self.rect.x -= 2*test_value
        l_collisions = pygame.sprite.spritecollide(self, self.game.platform_sprites, False)
        self.rect.x += test_value
        if r_collisions or l_collisions:
            self.pos.x -= self.vel.x
            self.vel.x = 0
        self.rect.y += 2*test_value
        b_collisions = pygame.sprite.spritecollide(self, self.game.platform_sprites, False)
        self.rect.y -= test_value
        if self.vel.y > 0:  # Only applies collision if playing is falling
            if b_collisions:
                self.pos.y = b_collisions[0].rect.top
                self.vel.y = 0

        return b_collisions

    def update(self):
        keys = pygame.key.get_pressed()
        self.acc = pygame.Vector2(0, GRAVITY_ACC)
        collisions = self.check_collisions()

        # Jump controls
        if collisions and keys[pygame.K_w] and self.can_jump:  # Get rid of "collisions and" on this line to allow
            # player to jump in the air (may be smoother gameplay)
            self.vel.y = PLAYER_JUMP_VEL
            self.can_jump = False
        if collisions:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_jump_time >= PLAYER_JUMP_DELAY:
                self.can_jump = True
                self.last_jump_time = current_time

        # Horizontal controls
        if keys[pygame.K_a]:
            self.acc.x += -PLAYER_ACC
        if keys[pygame.K_d]:
            self.acc.x += PLAYER_ACC

        self.acc.x += self.vel.x * PLAYER_FRICTION  # Apply friction
        self.vel += self.acc
        self.pos += self.vel + (0.5 * self.acc)  # Kinematic equation

        # Wrap around sides of screen
        if self.pos.x < 0:
            self.pos.x = SCREEN_WIDTH
        if self.pos.x > SCREEN_WIDTH:
            self.pos.x = 0

        # Calculated position will always represent midbottom of player sprite
        self.rect.midbottom = self.pos

    def reset(self):
        pass


class Platform(pygame.sprite.Sprite):
    def __init__(self, pos=(0, 0), size=(16, 16)):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(topleft=pos)

