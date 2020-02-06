from pygame.math import *
from abc import ABC, abstractmethod

class Physics(ABC):

    @abstractmethod
    def applyForce(self):
        pass

    @abstractmethod
    def applyGravity(self):
        pass