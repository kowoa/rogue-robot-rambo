from os import path
import pygame
import pymunk
from src.utilities import SCREEN_WIDTH, SCREEN_HEIGHT
from src.entities import Player


def main():
    pygame.init()
    # Set up pygame elements
    parent_dir = path.abspath("..")
    icon = pygame.image.load(parent_dir + "/resources/icons/robot.png")
    pygame.display.set_icon(icon)
    pygame.display.set_caption("ROGUE ROBOT RAMBO")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    max_fps = 60
    dt = 1/max_fps

    # Set up pymunk elements
    space = pymunk.Space()
    space.gravity = (0, -100)

    # Set up player
    player = Player(space, parent_dir + "/resources/sprites/player.png", (0, SCREEN_HEIGHT))
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    # Game loop,
    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        screen.fill((255, 255, 255))

        space.step(dt)

        all_sprites.update()

        all_sprites.draw(screen)

        pygame.display.update()
        clock.tick(max_fps)

    pygame.quit()


if __name__ == "__main__":
    main()