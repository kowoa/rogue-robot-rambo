import pygame
import sys
from paths import *
from settings import *


class GUI:
    def __init__(self, game):
        self.game = game
        self.font_name = pygame.font.match_font(FONT_NAME)

    def draw_text(self, text, size, color, pos=(0, 0)):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(midtop=pos)
        self.game.screen.blit(text_surface, text_rect)

    def draw_button(self, x, y, w, h, color, text_size, text_color, outline=None, text=""):
        if outline:
            pygame.draw.rect(self.game.screen, outline, (x - 2, y - 2, w + 4, h + 4), 0)
        pygame.draw.rect(self.game.screen, color, (x, y, w, h), 0)
        if text:
            pygame.font.init()
            font = pygame.font.Font(self.font_name, text_size)
            text = font.render(text, 1, text_color)
            self.game.screen.blit(text, (x + (w / 2 - text.get_width() / 2),
                                         y + (h / 2 - text.get_height() / 2)))

    def button_input(self, mouse_pos, x, y, w, h):
        """
        The position parameter is the position of the mouse, use 'position = pygame.mouse.get_pos()'
        in wait_for_click() to keep track of the position of the mouse. Also must create an event when
        the mouse clicks the button it creates an action.
        """
        # x, y, width, and height should be the same as the ones you used for the button
        return x < mouse_pos[0] < x + w and y < mouse_pos[1] < y + h

    def wait_for_click(self, menu):
        is_waiting = True
        while is_waiting:
            self.game.clock.tick(10)
            for event in pygame.event.get():
                mouse_pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    is_waiting = False
                    self.game.is_playing = False
                    self.game.is_running = False
                    sys.exit(0)
                if event.type == pygame.MOUSEBUTTONUP:
                    if menu == "start menu":
                        if self.button_input(mouse_pos, 350, SCREEN_HEIGHT*6/7, 110, 40): # START BUTTON
                            is_waiting = False
                        elif self.button_input(mouse_pos, 500, SCREEN_HEIGHT*6/7, 110, 40): # SCORE BUTTON
                            self.draw_leaderboard_menu()
                            is_waiting = False
                        elif self.button_input(mouse_pos, 650, SCREEN_HEIGHT*6/7, 110, 40): # ABOUT BUTTON
                            self.draw_about_menu()
                            is_waiting = False
                        elif self.button_input(mouse_pos, 800, SCREEN_HEIGHT*6/7, 110, 40): # QUIT BUTTON
                            is_waiting = False
                            self.game.is_playing = False
                            self.game.is_running = False
                            sys.exit()
                    elif menu == "leaderboard":
                        if self.button_input(mouse_pos, 567, SCREEN_HEIGHT*6/7, 140, 50): # BACK BUTTON
                            self.draw_start_menu()
                            is_waiting = False
                    elif menu == "about menu":
                        if self.button_input(mouse_pos, 567, SCREEN_HEIGHT*6/7, 110, 40): # BACK BUTTON
                            self.draw_start_menu()
                            is_waiting = False
                    elif menu == "score menu":
                        if self.button_input(mouse_pos, 567, SCREEN_HEIGHT*6/7, 140, 50): # RESUME BUTTON
                            is_waiting = False
                    elif menu == "pause menu":
                        if self.button_input(mouse_pos, 527, SCREEN_HEIGHT*6/7, 110, 50): # RESUME BUTTON
                            is_waiting = False
                        elif self.button_input(mouse_pos, 665, SCREEN_HEIGHT*6/7, 110, 50): # QUIT BUTTON
                            is_waiting = False
                            self.game.is_playing = False
                            self.game.is_running = False
                            sys.exit()
                    elif menu == "game over menu":
                        if self.button_input(mouse_pos, 527, SCREEN_HEIGHT*6/7, 110, 50): # PLAY AGAIN BUTTON
                            is_waiting = False
                        elif self.button_input(mouse_pos, 665, SCREEN_HEIGHT*6/7, 110, 50): # QUIT BUTTON
                            is_waiting = False
                            self.game.is_playing = False
                            self.game.is_running = False
                            sys.exit()

    def draw_start_menu(self):
        self.game.screen.fill((0, 0, 0))
        self.draw_text(SCREEN_TITLE, 52, (255, 255, 255), (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        self.draw_button(350, SCREEN_HEIGHT * 6 / 7, 110, 40, (255, 255, 255), 14, (0, 0, 0), text="START")
        self.draw_button(500, SCREEN_HEIGHT * 6 / 7, 110, 40, (255, 255, 255), 14, (0, 0, 0), text="SCORES")
        self.draw_button(650, SCREEN_HEIGHT * 6 / 7, 110, 40, (255, 255, 255), 14, (0, 0, 0), text="ABOUT")
        self.draw_button(800, SCREEN_HEIGHT * 6 / 7, 110, 40, (255, 255, 255), 14, (0, 0, 0), text="QUIT")
        self.draw_text("Use WASD to move!", 22, (255, 255, 255), (SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 / 4))
        header = pygame.transform.scale(pygame.image.load(header_path).convert(), (400, 200))
        self.game.screen.blit(header, (440, SCREEN_HEIGHT / 6))
        pygame.display.update()
        self.wait_for_click('start menu')

    def draw_game_over_menu(self):
        self.game.screen.fill((0, 0, 0))
        self.draw_text("GAME OVER", 68, (255, 255, 255), (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        self.draw_text("Score: {}".format(self.game.score), 22, (255, 255, 255),
                       (SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 / 4))
        self.draw_button(527, SCREEN_HEIGHT * 6 / 7, 110, 50, (255, 255, 255), 14, (0, 0, 0), text="PLAY AGAIN")
        self.draw_button(665, SCREEN_HEIGHT * 6 / 7, 110, 50, (255, 255, 255), 14, (0, 0, 0), text="QUIT")
        if self.game.score > self.game.high_score:
            self.game.high_score = self.game.score
            self.draw_text("NEW HIGH SCORE", 38, (255, 255, 255), (SCREEN_WIDTH / 6, SCREEN_HEIGHT / 2))
            with open(high_score_path, "w") as file:
                file.write(str(self.game.high_score))
        pygame.display.update()
        self.wait_for_click('game over menu')

    def draw_pause_menu(self):
        with open(high_score_path, "r") as file:
            try:
                self.game.high_score = int(file.read())
            except ValueError:
                self.game.high_score = 0
        self.game.screen.fill((0, 0, 0))
        self.draw_text("PAUSED", 78, (255, 255, 255), (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 6))
        self.draw_text(f"HIGH SCORE: {self.game.high_score}", 28, (255, 255, 255),
                       (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        self.draw_text(f"YOUR SCORE: {self.game.score}", 22, (255, 255, 255),
                       (SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 / 4))
        self.draw_button(520, SCREEN_HEIGHT * 6 / 7, 110, 50, (255, 255, 255), 14, (0, 0, 0), text="RESUME")
        self.draw_button(658, SCREEN_HEIGHT * 6 / 7, 110, 50, (255, 255, 255), 14, (0, 0, 0), text="QUIT")
        pygame.display.update()
        self.wait_for_click('pause menu')

    def draw_score_menu(self):
        with open(high_score_path, "r") as file:
            try:
                self.game.high_score = int(file.read())
            except ValueError:
                self.game.high_score = 0
        self.game.screen.fill((0, 0, 0))
        self.draw_text("HIGH SCORE", 52, (255, 255, 255), (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        self.draw_text("High score: {}".format(self.game.high_score), 22, (255, 255, 255),
                       (SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 / 4))
        self.draw_button(567, SCREEN_HEIGHT * 6 / 7, 140, 50, (255, 255, 255), 14, (0, 0, 0), text="RESUME")
        pygame.display.update()
        self.wait_for_click('score menu')

    def draw_leaderboard_menu(self):
        with open(high_score_path, "r") as file:
            try:
                self.game.high_score = int(file.read())
            except ValueError:
                self.game.high_score = 0
        self.game.screen.fill((0, 0, 0))
        self.draw_text("HIGH SCORE", 52, (255, 255, 255), (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        self.draw_text("High score: {}".format(self.game.high_score), 22, (255, 255, 255),
                       (SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 / 4))
        self.draw_button(567, SCREEN_HEIGHT * 6 / 7, 140, 50, (255, 255, 255), 14, (0, 0, 0), text="BACK")
        pygame.display.update()
        self.wait_for_click('leaderboard')

    def draw_about_menu(self):
        self.game.screen.fill((0, 0, 0))
        self.draw_text("ABOUT", 52, (255, 255, 255), (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 7))
        self.draw_text("Our game is a roguelike 2D platformer where the player tries to kill the AI. This "
                       "is a game where the player is the boss and the AI adapts to their patterns. It will", 20,
                       (255, 255, 255), (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3))
        self.draw_text("have pixel/sprite graphics and will be programmed primarily in Python. The "
                       "defining feature of this game entails that the AI learns your moves and eventually either",
                       20,
                       (255, 255, 255), (SCREEN_WIDTH / 2, 263))
        self.draw_text("you improve or let the AI get to you.Each time the AI improves,"
                       "we give the player a chance by improving the player’s statistics.", 20,
                       (255, 255, 255), (SCREEN_WIDTH / 2, 285))
        self.draw_text("Khoa Hoang", 25, (255, 255, 255), (200, SCREEN_HEIGHT / 2))
        self.draw_text("Matthew Innaurato", 25, (255, 255, 255), (500, SCREEN_HEIGHT / 2))
        self.draw_text("Pratham Kwatra", 25, (255, 255, 255), (750, SCREEN_HEIGHT / 2))
        self.draw_text("Adrienne Lhuc Estrella", 25, (255, 255, 255), (1050, SCREEN_HEIGHT / 2))
        self.draw_button(567, SCREEN_HEIGHT * 6 / 7, 110, 40, (255, 255, 255), 14, (0, 0, 0), text="BACK")
        adrienne = pygame.transform.scale(pygame.image.load(adrienne_path).convert(), (120, 160))
        self.game.screen.blit(adrienne, (990, 400))
        pygame.display.update()
        self.wait_for_click('about menu')

    # TODO: Implement scoring system & collision detection with health bar
    def draw_health_bar(self):
        self.draw_text("Health: ", 22, (255, 255, 255), (50, 15))
        pygame.draw.rect(self.game.screen, (0, 255, 0), (85, 21.5, 80, 15))

    # TODO: Implement ammo sprite group with ammo bar
    def draw_ammo_bar(self):
        self.draw_text("Ammo: ", 22, (255, 255, 255), (50, 50))
        pygame.draw.rect(self.game.screen, (0, 255, 0), (85, 57, 80, 15))
