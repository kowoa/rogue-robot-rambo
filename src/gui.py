import pygame
from settings import *
from file_paths import *


class GUI:
    def __init__(self, game):
        self.game = game
        self.font_name = pygame.font.match_font(FONT_NAME)

    def draw_text(self, text, size, color, pos=(0, 0)):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(midtop=pos)
        self.game.screen.blit(text_surface, text_rect)

    def wait_for_key(self):
        is_waiting = True
        while is_waiting:
            self.game.clock.tick(10)
            for event in pygame.event.get():
                # Warning: caplock counts as keydown
                if event.type == pygame.QUIT:
                    is_waiting = False
                    self.game.is_running = False
                if event.type == pygame.KEYUP:
                    is_waiting = False

    def draw_start_menu(self):
        self.game.screen.fill((0, 0, 0))
        self.draw_text(SCREEN_TITLE, 48, (255, 255, 255), (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        self.draw_text("Use WASD to move!", 22, (255, 255, 255), (SCREEN_WIDTH/2, SCREEN_HEIGHT*3/4))
        self.draw_text("Press any button to play, Press H to show high score", 16, (255, 255, 255), (SCREEN_WIDTH/2, SCREEN_HEIGHT*7/8))
        pygame.display.update()
        self.wait_for_key()

    def draw_game_over_menu(self):
        self.game.screen.fill((0, 0, 0))
        self.draw_text("GAME OVER", 48, (255, 255, 255), (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        self.draw_text("Score: {}".format(self.game.player.score), 22, (255, 255, 255), (SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 / 4))
        self.draw_text("Press any button to play again", 16, (255, 255, 255), (SCREEN_WIDTH / 2, SCREEN_HEIGHT * 7 / 8))
        if self.game.player.score > self.game.high_score:
            self.game.high_score = self.game.player.score
            self.draw_text("NEW HIGH SCORE", 36, (255, 255, 255), (SCREEN_WIDTH/2, 10))
            with open(high_score_path, "w") as file:
                file.write(str(self.game.high_score))
        pygame.display.update()
        self.wait_for_key()

    def draw_score_menu(self):
        with open(high_score_path, "r") as file:
            try:
                self.game.high_score = int(file.read())
            except ValueError:
                self.game.high_score = 0
        self.game.screen.fill((0, 0, 0))
        self.draw_text("HIGH SCORE", 48, (255, 255, 255), (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        self.draw_text("High score: {}".format(self.game.high_score), 22, (255, 255, 255),
                       (SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 / 4))
        self.draw_text("Press any button to continue", 16, (255, 255, 255), (SCREEN_WIDTH / 2, SCREEN_HEIGHT * 7 / 8))
        pygame.display.update()
        self.wait_for_key()



