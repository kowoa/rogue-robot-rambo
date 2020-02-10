import pygame

class Weapon(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = 8

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
    
    def shoot(self):
        bullets = []

        for bullet in bullets:
            if bullet.x < 500 and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

        if len(bullets) > 5:
            bullets.append(Weapon(weaponImg.x, weaponImg.y, 6, (0,0,0)))
        