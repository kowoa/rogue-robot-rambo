import numpy as np

class Physics():

    # numpy.array([x, y])
    def __init__(self, mass=int, pos=np.array([0,0]), vel=np.array([0,0]), acc=np.array([0,0])):
        self.mass = mass
        self.pos = pos
        self.vel = vel
        self.acc = acc

    # Physics Methods
    def getForce(self):
        return self.mass * np.linalg.norm(self.acc)

    def applyForce(self, force):
        acc = (self.force // self.mass)

    def applyGravity(self):
        self.acc += 1

    # Frame-dependent methods
    # Update function for player. Utilized for all calculations per one frame
    def update(self):
        self.vel += self.acc
        self.pos += self.vel
