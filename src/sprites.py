import pygame
from settings import *
from file_paths import *
from utils import *


class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game

        # Initialize sprite sheets and frame lists
        self.idle_frames = []
        self.walk_frames_l = []
        self.walk_frames_r = []
        self.jump_frames = []
        self.load_sprite_sheets()

        # Initialize pygame elements
        self.image = self.idle_frames[0]
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT - 40))

        # Initialize vectors for realistic movement
        self.pos = pygame.Vector2(self.rect.center)
        self.vel = pygame.Vector2(0, 0)
        self.acc = pygame.Vector2(0, 0)
        self.friction = -0.12  # Make sure friction is ALWAYS negative

        # These variables are used for jumping and sprite animations
        self.is_jumping = True
        self.last_jump_time = pygame.time.get_ticks()
        self.is_walking = False
        self.current_frame = 0
        self.last_frame_update = 0

        # Keep track of score and stats here
        self.score = 0

        # Constants
        self.BASE_ACC = 0.5
        self.JUMP_VEL = -18
        self.JUMP_DELAY = 500

    def load_sprite_sheets(self):
        idle_sheet = SpriteSheet(player_idle_path)
        for i in range(0, 8):  # Add all frames of sprite sheet into a list (8 sprites in this case)
            self.idle_frames.append(idle_sheet.get_sprite(i * 32, 0, 32, 28))
        walk_sheet = SpriteSheet(player_walk_path)
        for i in range(0, 8):
            self.walk_frames_r.append(walk_sheet.get_sprite(i * 32, 0, 32, 32))
        for frame in self.walk_frames_r:
            self.walk_frames_l.append(pygame.transform.flip(frame, True, False))
        jump_sheet = SpriteSheet(player_jump_path)
        for i in range(0, 6):
            self.jump_frames.append(jump_sheet.get_sprite(i * 28, 0, 28, 28))

    def animate(self):
        current_time = pygame.time.get_ticks()
        if not self.is_jumping and not self.is_walking:
            if current_time - self.last_frame_update > 100:
                self.last_frame_update = current_time
                self.current_frame = (self.current_frame + 1) % len(self.idle_frames)
                self.image = self.idle_frames[self.current_frame]

    def check_collisions(self):
        # Check and apply collisions with platforms
        self.rect.y += 1
        collisions = pygame.sprite.spritecollide(self, self.game.platform_sprites, False)
        self.rect.y -= 1
        if self.vel.y > 0 and collisions:  # Only applies collision if player is falling
            self.pos.y = collisions[0].rect.top
            self.vel.y = 0
        return collisions

    def update(self):
        keys = pygame.key.get_pressed()
        self.acc = pygame.Vector2(0, GRAVITY_ACC)
        collisions = self.check_collisions()
        current_time = pygame.time.get_ticks()

        self.animate()

        # Change friction depending on platform
        if collisions:
            self.friction = collisions[0].friction  # Set player friction equal to platform friction
        else:
            self.friction = -0.12  # If player is in air, set back to base friction

        # Jump controls
        if collisions and keys[pygame.K_w] and not self.is_jumping \
                and self.vel.y >= 0 and current_time - self.last_jump_time >= self.JUMP_DELAY:
            # Get rid of "collisions and" to allow player to jump in the air (may be smoother gameplay)
            self.vel.y = self.JUMP_VEL
            self.is_jumping = True
            self.last_jump_time = current_time
        elif collisions:
            self.is_jumping = False

        # Horizontal controls
        if keys[pygame.K_a]:
            self.acc.x += -self.BASE_ACC
        if keys[pygame.K_d]:
            self.acc.x += self.BASE_ACC

        self.acc.x += self.vel.x * self.friction  # Apply friction
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
        # Use this method to reset player's stats and stuff for new game
        self.__init__(self.game)  # placeholder


class Platform(pygame.sprite.Sprite):
    def __init__(self, pos=(0, 0), size=(16, 16), friction=-0.12):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(topleft=pos)

        self.friction = friction

