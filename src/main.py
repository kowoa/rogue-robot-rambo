import pygame
from src.file_paths import *
from src.settings import *
from src.sprites import *


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_icon(pygame.image.load(icon_path))
        pygame.display.set_caption(SCREEN_TITLE)

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.is_playing = True

        self.all_sprites = pygame.sprite.Group()
        self.player = Player()

    def start(self):
        """ Start new game """
        self.all_sprites.empty()
        self.player.reset()

        self.all_sprites.add(self.player)

        self.run()

    def run(self):
        """ GAME LOOP """
        while self.is_playing:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(MAX_FPS)

    # Methods below are all contained within game loop

    def update(self):
        """ Update sprites"""
        self.all_sprites.update()

    def handle_events(self):
        """ Handle pygame events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_playing = False
                self.is_running = False

    def draw(self):
        """ Draw everything """
        self.screen.fill((0, 0, 0))
        self.all_sprites.draw(self.screen)
        pygame.display.update()


def main():
    game = Game()
    while game.is_running:
        game.start()
    pygame.quit()


if __name__ == "__main__":
    main()