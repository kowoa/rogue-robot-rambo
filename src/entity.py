from pygame.math import *
from src.physics import *


class Entity(Physics):

    def __init__(self, mass=0, pos=Vector2(0, 0), vel=Vector2(0, 0), acc=Vector2(0, 0)):
        self.mass = mass
        self.pos = pos
        self.vel = vel
        self.acc = acc

    # Physics Methods
    def applyForce(self, force):
        acc = (self.force // self.mass)

    def applyGravity(self):
        self.acc += 1


    # Frame-dependent methods
    # Update function for player. Utilized for all calculations per one frame
    def update(self):
        self.vel += self.acc
        self.pos += self.vel

