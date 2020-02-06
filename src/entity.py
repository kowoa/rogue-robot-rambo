from pygame.math import *
from src.physics import *


class Entity():

    # Takes physics object as parameter
    def __init__(self, physics=Physics()):
        self.physics = physics