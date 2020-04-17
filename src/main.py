from os import path
import pygame
import pymunk
from entities import Player

def main():
    pygame.init()
    parent_dir = path.abspath("..")
    icon = pygame.image.load(parent_dir + "/resources/icons/robot.png")
    pygame.display.set_icon(icon)
    pygame.display.set_caption("ROGUE ROBOT RAMBO")
    screen = pygame.display.set_mode((400, 400))
    clock = pygame.time.Clock()

    space = pymunk.Space()


    player = Player(parent_dir + "/resources/sprites/player.png", 10, 10)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)


    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        screen.fill((255, 255, 255))
        all_sprites.draw(screen)

        clock.tick(60)
        pygame.display.update()

    pygame.quit()
























if __name__ == "__main__":
    main()