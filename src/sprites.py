import pygame
from settings import *
from file_paths import *
from utilities import *


class PlayerFX(pygame.sprite.Sprite):
    def __init__(self, player, frames):
        super().__init__()
        self.player = player
        self.image = frames[0]
        self.rect = self.image.get_rect(midbottom=player.pos)
        self.frames = frames
        self.last_frame_update = 0
        self.current_frame = 0

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_frame_update > 100:
            self.last_frame_update = current_time
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
            if self.current_frame >= len(self.frames) - 1:
                self.kill()


class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game

        # Initialize sprite sheets and frame lists
        self.idle_frames_r = []
        self.idle_frames_l = []
        self.walk_frames_r = []
        self.walk_frames_l = []
        self.jump_frames_r = []
        self.jump_frames_l = []
        self.fall_frames_r = []
        self.fall_frames_l = []
        self.land_frames_r = []
        self.land_frames_l = []
        # FX sprite frame lists
        self.jump_fx_frames = []
        self.land_fx_frames = []
        self.load_sprite_sheets()

        # Initialize pygame elements
        self.image = self.idle_frames_r[0]
        self.rect = self.image.get_rect(midbottom=(SCREEN_WIDTH/2, SCREEN_HEIGHT - 60))

        # Initialize vectors for realistic movement
        self.pos = pygame.Vector2(self.rect.center)
        self.vel = pygame.Vector2(0, 0)
        self.acc = pygame.Vector2(0, GRAVITY_ACC)
        self.friction = -0.12  # Make sure friction is ALWAYS negative

        # These variables are used for jumping mechanics and sprite animations
        self.is_jumping = False
        self.can_jump = False
        self.is_falling = False
        self.is_landing = False
        self.can_land = False  # Used to regulate landing animation
        self.is_walking = False
        self.is_facing_right = True
        self.last_jump_time = pygame.time.get_ticks()
        self.current_frame = 0  # Used for looping animations
        self.current_jump_frame = 0  # Used for jumping animation
        self.current_land_frame = 0  # Used for landing animation
        self.last_frame_update = 0

        # Keep track of score and stats here
        self.score = 0

        # Constants
        self.BASE_ACC = 0.5
        self.JUMP_VEL = -20
        self.JUMP_DELAY = 500

    def load_sprite_sheets(self):
        # Idle
        sheet = SpriteSheet(player_idle_path)
        for i in range(0, 8):  # Add all frames of sprite sheet into a list (8 sprites in this case)
            self.idle_frames_r.append(sheet.get_sprite(i * 32, 0, 32, 28))
        for frame in self.idle_frames_r:
            self.idle_frames_l.append(pygame.transform.flip(frame, True, False))

        # Walk
        sheet = SpriteSheet(player_walk_path)
        for i in range(0, 8):
            self.walk_frames_r.append(sheet.get_sprite(i * 32, 0, 32, 32))
        for frame in self.walk_frames_r:
            self.walk_frames_l.append(pygame.transform.flip(frame, True, False))

        # Jump
        sheet = SpriteSheet(player_jump_path)
        for i in range(0, 6):
            self.jump_frames_r.append(sheet.get_sprite(i * 28, 0, 28, 28))
        for frame in self.jump_frames_r:
            self.jump_frames_l.append(pygame.transform.flip(frame, True, False))

        # Fall
        sheet = SpriteSheet(player_fall_path)
        for i in range(0, 2):
            self.fall_frames_r.append(sheet.get_sprite(i * 32, 0, 32, 28))
        for frame in self.fall_frames_r:
            self.fall_frames_l.append(pygame.transform.flip(frame, True, False))

        # Land
        sheet = SpriteSheet(player_land_no_dust_path)
        for i in range(0, 4):
            self.land_frames_r.append(sheet.get_sprite(i * 44, 0, 44, 32))
        for frame in self.land_frames_r:
            self.land_frames_l.append(pygame.transform.flip(frame, True, False))

        # Jump FX
        sheet = SpriteSheet(player_jump_fx_path)
        for i in range(0, 6):
            self.jump_fx_frames.append(sheet.get_sprite(i * 28, 0, 28, 28))
        # Land FX
        sheet = SpriteSheet(player_land_fx_path)
        for i in range(0, 4):
            self.land_fx_frames.append(sheet.get_sprite(i * 44, 0, 44, 32))

    def animate(self):
        current_time = pygame.time.get_ticks()
        # I know this looks messy and has duplicate code, but keep this conditional nested to adjust animation speed:
        # >> if current_time - self.last_frame_update > 100
        if current_time - self.last_frame_update > 100:
            self.last_frame_update = current_time
            # Land (DO NOT TOUCH THIS; I GOT IT WORKING BY DIVINE INTERVENTION)
            if self.is_landing and self.is_facing_right:
                if self.current_land_frame < len(self.land_frames_r):
                    self.current_land_frame = (self.current_land_frame + 1) % len(self.land_frames_r)
                self.image = self.land_frames_r[self.current_land_frame]
            elif self.is_landing and not self.is_facing_right:
                if self.current_land_frame < len(self.land_frames_l):
                    self.current_land_frame = (self.current_land_frame + 1) % len(self.land_frames_l)
                self.image = self.land_frames_l[self.current_land_frame]
            if self.current_land_frame >= len(self.land_frames_r) - 1:
                self.is_landing = False
                self.current_land_frame = 0
            # Idle
            if not self.is_walking and not self.is_jumping and self.is_facing_right \
                    and not self.is_landing and not self.is_falling:
                self.current_frame = (self.current_frame + 1) % len(self.idle_frames_r)  # Make the frames loopy loop
                self.image = self.idle_frames_r[self.current_frame]
            elif not self.is_walking and not self.is_jumping and not self.is_facing_right \
                    and not self.is_landing and not self.is_falling:
                self.current_frame = (self.current_frame + 1) % len(self.idle_frames_l)
                self.image = self.idle_frames_l[self.current_frame]
            # Walk
            if self.is_walking and not self.is_jumping and self.is_facing_right \
                    and not self.is_landing and not self.is_falling:
                self.current_frame = (self.current_frame + 1) % len(self.walk_frames_r)
                self.image = self.walk_frames_r[self.current_frame]
            elif self.is_walking and not self.is_jumping and not self.is_facing_right \
                    and not self.is_landing and not self.is_falling:
                self.current_frame = (self.current_frame + 1) % len(self.walk_frames_l)
                self.image = self.walk_frames_l[self.current_frame]
            # Jump
            if self.is_jumping and not self.is_falling and self.is_facing_right and not self.is_landing:
                if self.current_jump_frame < len(self.jump_frames_r):
                    self.current_jump_frame = (self.current_jump_frame + 1) % len(self.jump_frames_r)
                self.image = self.jump_frames_r[self.current_jump_frame]
            elif self.is_jumping and not self.is_falling and not self.is_facing_right and not self.is_landing:
                if self.current_jump_frame < len(self.jump_frames_l):
                    self.current_jump_frame = (self.current_jump_frame + 1) % len(self.jump_frames_l)
                self.image = self.jump_frames_l[self.current_jump_frame]
            elif not self.is_jumping:
                self.current_jump_frame = 0
            # Fall
            if self.is_falling and self.is_facing_right and not self.is_landing:
                self.current_frame = (self.current_frame + 1) % len(self.fall_frames_r)
                self.image = self.fall_frames_r[self.current_frame]
            elif self.is_falling and not self.is_facing_right and not self.is_landing:
                self.current_frame = (self.current_frame + 1) % len(self.fall_frames_l)
                self.image = self.fall_frames_l[self.current_frame]

        # Adjust sprite height so that sprite doesn't clip into platform
        bottom = self.rect.bottom
        self.rect = self.image.get_rect()
        self.rect.bottom = bottom

    def apply_platform_collisions(self):
        # Check and apply collisions with platforms
        self.rect.y += 1
        collisions = pygame.sprite.spritecollide(self, self.game.platform_sprites, False)
        self.rect.y -= 1
        # Only applies collision if player is falling, adjusts to ensure the floating doesn't float at edges
        if self.vel.y > 0 and collisions and collisions[0].rect.left - 10 < self.pos.x < collisions[0].rect.right + 10:
            if self.pos.y < collisions[0].rect.bottom:  # This makes it so player doesn't teleport up platforms
                self.pos.y = collisions[0].rect.top
                self.vel.y = 0

                # Change friction depending on platform
                if collisions:
                    self.friction = collisions[0].friction  # Set player friction equal to platform friction
                else:
                    self.friction = -0.12  # If player is in air, set back to base friction

                # Allow jumping
                if not self.is_jumping:
                    self.can_jump = True

                self.is_jumping = False
                self.is_falling = False
                if self.can_land:
                    self.can_land = False
                    self.is_landing = True
                    # Trigger land fx
                    land_fx = PlayerFX(self, self.land_fx_frames)
                    self.game.all_sprites.add(land_fx)
                    self.game.fx_sprites.add(land_fx)

    def update(self):
        keys = pygame.key.get_pressed()
        self.acc = pygame.Vector2(0, GRAVITY_ACC)
        self.apply_platform_collisions()
        current_time = pygame.time.get_ticks()

        self.animate()

        # Jump Controls
        if self.can_jump and keys[pygame.K_w] and current_time - self.last_jump_time >= self.JUMP_DELAY:
            self.vel.y = self.JUMP_VEL
            self.is_jumping = True
            self.last_jump_time = current_time
            # Trigger jump fx
            jump_fx = PlayerFX(self, self.jump_fx_frames)
            self.game.all_sprites.add(jump_fx)
            self.game.fx_sprites.add(jump_fx)
            self.can_jump = False

        # Falling animation condition
        if self.vel.y > 0:
            self.is_falling = True
            self.can_land = True

        # Horizontal controls
        if keys[pygame.K_a]:
            self.acc.x += -self.BASE_ACC
            self.is_facing_right = False
            self.is_walking = True
        if keys[pygame.K_d]:
            self.acc.x += self.BASE_ACC
            self.is_facing_right = True
            self.is_walking = True
        if not keys[pygame.K_a] and not keys[pygame.K_d]:
            self.is_walking = False

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

