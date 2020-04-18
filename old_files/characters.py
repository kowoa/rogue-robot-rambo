import pygame
import pymunk
from old_files.utilities import convert_coordinates


class Player(pygame.sprite.Sprite):
    def __init__(self, space, pos=(0, 0)):
        super().__init__()
        self.image = pygame.Surface((64, 64))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(center=pos)

        mass = 1
        moment = 100000
        self.body = pymunk.Body(mass, moment)
        self.body.position = convert_coordinates(pos)
        self.shape = pymunk.Poly.create_box(self.body, (self.rect.width, self.rect.height))
        space.add(self.body, self.shape)

        self.is_jumping = False
        self.base_move_force = 500
        self.base_jump_impulse = 200

    def control(self):
        key_pressed = pygame.key.get_pressed()
        move_force = (0, 0)

        # Jumping
        if key_pressed[pygame.K_w]:
            self.body.apply_impulse_at_local_point((0, self.base_jump_impulse))

        # Moving - key pressed
        if key_pressed[pygame.K_a]:
            move_force += (-self.base_move_force, 0)
        if key_pressed[pygame.K_s]:
            pass
        if key_pressed[pygame.K_d]:
            move_force += (self.base_move_force, 0)

        self.body.apply_force_at_local_point(pymunk.Vec2d(100, 0), (0, 0))

    def update(self):
        self.control()
        self.rect.center = convert_coordinates(self.body.position)
