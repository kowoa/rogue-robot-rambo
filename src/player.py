from src.physics import *


class Player:
    pos = Vector2D()
    vel = Vector2D()
    mass = 0.0
    acc = Vector2D()

    def __init__(self, mass=0.0, pos=Vector2D([0, 0]), vel=Vector2D(), acc=Vector2D()):
        self.pos = pos
        self.vel = vel
        self.mass = mass
        self.acc = acc

    def update(self):
        #if self.acc.pos[0]
        self.vel += self.acc
        self.pos += self.vel

    # def applyForce(self, force):
