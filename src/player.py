from src.entity import *
import pygame

class Player(Entity):
    def __init__(self, mass, pos, vel, acc):
        Entity.__init__(self, mass, pos, vel, acc)


    def doKeyState(self):
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_UP] or keystate[pygame.K_w]:
            self.vel[1] = -5
            #self.shoot()
        elif keystate[pygame.K_DOWN] or keystate[pygame.K_s]:
            self.vel[1] = 5
            #self.shoot()

        elif keystate[pygame.K_LEFT] or keystate[pygame.K_a]:
            self.vel[0] = -5
            #self.shoot()
        elif keystate[pygame.K_RIGHT] or keystate[pygame.K_d]:
            self.vel[0] = 5
            #self.shoot()
        else:
            self.acc = np.array([0,0])