import pygame
from random import randint
from file_paths import *
from settings import *
from player import *
from environment import *
from gui import *
# NOTE: In PyCharm, there will be red highlights in import statements
# Resolve by right-clicking on src/ folder and Mark Directory as -> Sources Root


class Game:
    def __init__(self):
        pygame.init()
        icon = pygame.image.load(icon_path)
        pygame.display.set_icon(icon)
        pygame.display.set_caption(SCREEN_TITLE)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.is_running = True
        self.is_playing = True

        self.all_sprites = pygame.sprite.Group()
        self.platform_sprites = pygame.sprite.Group()
        self.fx_sprites = pygame.sprite.Group()
        self.player = Player(self)
        self.high_score = 0

        self.gui = GUI(self)

        self.glacial_background = GlacialBackground(self)

    def run(self):
        self.start()
        """ GAME LOOP """
        while self.is_playing:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(MAX_FPS)

    # Methods below are all contained within game loop

    def start(self):
        """ Start new game """
        self.is_playing = True
        self.all_sprites.empty()
        self.player.reset()

        for plat_args in PLATFORM_LIST:
            plat = Platform(*plat_args)
            self.all_sprites.add(plat)
            self.platform_sprites.add(plat)

        self.all_sprites.add(self.player)

    def handle_events(self):
        """ Handle pygame events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_playing = False
                self.is_running = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_h:
                    self.gui.draw_score_menu()

    def update(self):
        """ Update sprites"""
        # If player reaches top quarter of screen, scroll screen up
        if self.player.rect.top <= SCREEN_HEIGHT / 4:
            # Move player down
            self.player.pos.y += abs(self.player.vel.y)
            # Move platforms down
            for platform in self.platform_sprites:
                platform.rect.y += abs(self.player.vel.y)
                if platform.rect.top >= SCREEN_HEIGHT:
                    platform.kill()
                    self.player.score += 10
            # Move fx sprites down
            for fx in self.fx_sprites:
                fx.rect.y += abs(self.player.vel.y)
            # Update background
            # TODO: Make backgound change slightly every time screen scrolls up to simulate climbing feeling


        # Spawn new platforms to keep similar number of platforms
        while len(self.platform_sprites) < 6:
            platform_width = randint(500, 1000)
            platform = Platform((randint(0, SCREEN_WIDTH - platform_width), randint(-40, -30)),
                                (platform_width, 20))
            self.platform_sprites.add(platform)
            self.all_sprites.add(platform)
        # If player falls below bottom of screen, player dies
        if self.player.rect.top > SCREEN_HEIGHT:
            # Camera scrolls down suddenly
            for sprite in self.all_sprites:
                sprite.rect.y -= max(self.player.vel.y, 10)
                if sprite.rect.bottom < 0:
                    sprite.kill()
        if len(self.platform_sprites) == 0:
            self.is_playing = False
            self.gui.draw_game_over_menu()

        self.all_sprites.update()

    def draw(self):
        """ Draw updated screen """
        self.screen.fill((0, 0, 128))
        for layer in self.glacial_background.layers:
            self.screen.blit(layer, (0, 0))
        print(len(self.glacial_background.layers))

        self.gui.draw_text("Score: {}".format(self.player.score), 22, (255, 255, 255), (SCREEN_WIDTH/2, 15))

        self.all_sprites.draw(self.screen)
        pygame.display.update()


def main():
    game = Game()
    game.gui.draw_start_menu()
    while game.is_running:
        game.run()
    pygame.quit()


if __name__ == "__main__":
    main()
