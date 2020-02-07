from pygame.math import *
from src.physics import *


class Entity():

    # Takes physics object as parameter
    def __init__(self, mass, pos, vel, acc):
        self.mass = mass
        self.pos = pos
        self.vel = vel
        self.acc = acc
        self.physics = Physics(mass, pos, vel, acc)