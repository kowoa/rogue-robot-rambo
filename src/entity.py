from pygame.math import *
import numpy as np

# Entity has physics
class Entity():

    # Takes int mass and numpy arrays [x,y] pos, vel, and acc
    def __init__(self, size = int(), mass=int(), pos=np.array([0, 0]), vel=np.array([0, 0]), acc=np.array([0, 0])):
        self.size = size
        self.mass = mass
        self.pos = pos
        self.vel = vel
        self.acc = acc


    def detectBounds(self):
        if self.pos[0] < 0:
            self.pos[0] = 0
        if self.pos[0] > 1280-32:
            self.pos[0] = 1280-32
        if self.pos[1] < 0:
            self.pos[1] = 0
        if self.pos[1] > 720-32:
            self.pos[1] = 720-32



    # Physics Methods
    def getForce(self):
        return self.mass * np.linalg.norm(self.acc)

    def applyForce(self, force):
        self.acc = (self.force // self.mass)

    def updateMovement(self):
        self.detectBounds()
        self.vel += self.acc
        self.pos += self.vel