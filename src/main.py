import pygame
from random import randint
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
        self.platform_sprites = pygame.sprite.Group()
        self.player = Player(self)

    def start(self):
        """ Start new game """
        self.all_sprites.empty()
        self.player.reset()

        for plat_args in PLATFORM_LIST:
            plat = Platform(*plat_args)
            self.all_sprites.add(plat)
            self.platform_sprites.add(plat)
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
        # If player reaches top quarter of screen, scroll screen up
        if self.player.rect.top <= SCREEN_HEIGHT / 4:
            self.player.pos.y += abs(self.player.vel.y)
            for platform in self.platform_sprites:
                platform.rect.y += abs(self.player.vel.y)
                if platform.rect.top >= SCREEN_HEIGHT + self.player.rect.height:
                    platform.kill()
        # Spawn new platforms to keep similar number of platforms
        while len(self.platform_sprites) < 6:
            platform_width = randint(50, 100)
            platform = Platform((randint(0, SCREEN_WIDTH - platform_width), randint(-75, -30)),
                                (platform_width, 20))
            self.platform_sprites.add(platform)
            self.all_sprites.add(platform)

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