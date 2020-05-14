""" RUN GAME FROM THIS MODULE """
# TRY TO AVOID PUTTING GAME LOGIC HERE; USE OTHER MODULES
import sys
import pygame as pg
from paths import *        # File paths
from settings import *     # Constants
from player import *       # Player
from boss import *         # Boss
from platforms import *    # Platforms
from backgrounds import *  # Backgrounds
from music import *        # Music
from gui import *          # GUI and menus
from bullets import *      # Bullet


class Game:
    def __init__(self):
        pg.init()
        icon = pg.image.load(icon_path)
        pg.display.set_icon(icon)
        pg.display.set_caption(SCREEN_TITLE)
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pg.time.Clock()
        self.events = pg.event.get()

        self.is_running = True  # Used to keep program running
        self.is_playing = True  # Used to track whether player is playing

        # Sprite groups
        self.all_sprites = pg.sprite.Group()   # All
        self.plat_sprites = pg.sprite.Group()  # Platforms
        self.char_sprites = pg.sprite.Group()  # Characters
        self.fx_sprites = pg.sprite.Group()    # Effects
        self.bull_sprites = pg.sprite.Group()  # Bullets
        self.gun_sprites = pg.sprite.Group()   # Guns

        # Character sprites
        self.player = Player(self)
        self.boss = Boss(self)

        # Score
        self.score = 0
        self.high_score = 0

        # Background
        self.background = GlacialBackground(self)

        # Music
        #self.music = Music()

        # GUI
        self.gui = GUI(self)

    def init_platforms(self):
        Platform(self, -100, SCREEN_HEIGHT - 48, SCREEN_WIDTH + 200, 48)  # Ground
        # Generate 4 more platforms
        for i in range(0, 4):
            plat_width = randint(SCREEN_WIDTH / 4, SCREEN_WIDTH / 2)
            plat_pos_x = randint(0, SCREEN_WIDTH - plat_width)
            plat_pos_y = i*(SCREEN_HEIGHT//4) + 50
            # New platform created and automatically added to sprite groups
            Platform(self, plat_pos_x, plat_pos_y, plat_width, 32)

    def run(self):
        with open(high_score_path, "w") as file:
            file.write("0")
        self.gui.draw_start_menu()
        self.init_platforms()
        # Game loop for running
        while self.is_running:
            # Inner loop for playing
            while self.is_playing:
                # Main drivers
                self.handle_events()
                self.update()
                self.draw()
                self.clock.tick(MAX_FPS)
            # Player died; reset game
            self.reset()
        pg.quit()
        sys.exit(0)

    def handle_events(self):
        self.events = pg.event.get()
        for event in self.events:
            # Exiting
            if event.type == pg.QUIT:
                self.is_playing = False
                self.is_running = False
            # Bring up menus
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_h:
                    self.gui.draw_score_menu()
                elif event.key == pygame.K_p:
                    self.gui.draw_pause_menu()

    def update(self):
        self.background.update()
        self.all_sprites.update()
        #self.music.update()

    def draw(self):
        # Background
        self.background.draw()
        # Sprites
        self.plat_sprites.draw(self.screen)
        self.char_sprites.draw(self.screen)
        self.gun_sprites.draw(self.screen)
        self.fx_sprites.draw(self.screen)
        self.bull_sprites.draw(self.screen)
        # GUI
        self.gui.draw_text("Score: {}".format(self.score), 22, (255, 255, 255), (SCREEN_WIDTH/2, 15))
        self.gui.draw_health_bar()
        self.gui.draw_ammo_bar()

        """ UNCOMMENT THIS TO SHOW INVISIBLE FUTURE PLAYER"""
        """
        self.screen.blit(self.player.ft_image,
                         (self.player.ft_pos.x - self.player.ft_rect.w/2,
                          self.player.ft_pos.y - self.player.ft_rect.h/2))
        """

        # Update screen
        pg.display.update()

    def reset(self):
        self.is_playing = True
        for sprite in self.all_sprites:
            sprite.kill()
        self.player = Player(self)  # TODO: Make reset() method for Player
        self.boss = Boss(self)  # TODO: Make reset() method for Boss
        self.score = 0
        self.init_platforms()


def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    main()