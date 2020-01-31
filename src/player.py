from src.physics import *

class Player:

    pos = Vector2D()
    vel = Vector2D()
    mass = 0.0
    acc = Vector2D()
    force = Vector2D()

    def __init__(self, pos = Vector2D([0,0]), vel = Vector2D(), mass = 0.0, acc = Vector2D()):
        self.pos = pos
        self.vel = vel
        self.mass = mass
        self.acc = acc

    def applyForce(self, force):
        self.force = force
        self.vel += self.force.acc
        self.pos += self.vel