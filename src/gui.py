# Name: gui.py
# Purpose: Implements the GUI class (used for displaying graphics) and all GUI-related methods/attributes
# Version: 2.1
# Date: 5 June 2020
# Author(s): Khoa Hoang, Adrienne Lhuc Estrella
# Dependencies: pygame, sys, paths, and settings modules

import pygame as pg
import sys
from paths import *
from settings import *


class GUI:
    def __init__(self, game):
        '''
        Displays and manipulates the GUI of the game
        :param game: reference to hame instance
        '''
        self.game = game
        self.font_name = pg.font.match_font(FONT_NAME) # Used so all fonts in the game renders as the same


    def draw_text(self, text, size, color, pos=(0, 0), design = False, design_color=(0, 0, 0)):
        '''
        Used to display text onto the game screen
        :param text: the text you want to display on the screen (must be type string)
        :param size: the size of the string text
        :param color: the color of the string text
        :param pos: the position, must be a typle (x, y), of the rectantgle of the text.
        this position is the midtop of the text's rectangle, default to the top left of the screen
        :param design: creates a border around the text, True = border or False = no border, default to False
        :param design_color: the color of the border (must be a rgb value), default to black
        '''
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(midtop=pos)
        if design:
            pg.draw.rect(self.game.screen, design_color, (text_rect[0]-10, text_rect[1]-10, 
                            text_rect[2]+18, text_rect[3]+20))
        self.game.screen.blit(text_surface, text_rect)


    def draw_button(self, x, y, w, h, color, text_size, text_color, outline=None, text=""):
        buttonRect = pg.draw.rect(self.game.screen, color, (x, y, w, h), 0)
        if outline:
            pg.draw.rect(self.game.screen, outline, (buttonRect), 3)
        if text:
            pg.font.init()
            font = pg.font.Font(self.font_name, text_size)
            font.set_bold(True)
            text = font.render(text, 1, text_color)
            self.game.screen.blit(text, (x + (w / 2 - text.get_width() / 2),
                                         y + (h / 2 - text.get_height() / 2)))


    def button_input(self, mouse_pos, x, y, w, h):
        """
        The position parameter is the position of the mouse, use 'position = pg.mouse.get_pos()'
        in wait_for_click() to keep track of the position of the mouse. Also must create an event when
        the mouse clicks the button it creates an action.
        """
        # x, y, width, and height should be the same as the ones you used for the button
        return x < mouse_pos[0] < x + w and y < mouse_pos[1] < y + h


    def wait_for_click(self, menu):
        is_waiting = True
        while is_waiting:
            self.game.clock.tick(10)
            for event in pg.event.get():
                mouse_pos = pg.mouse.get_pos()
                if event.type == pg.QUIT:
                    is_waiting = False
                    self.game.is_playing = False
                    self.game.is_running = False
                    sys.exit(0)
                if event.type == pg.MOUSEBUTTONUP:
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
                    elif menu == "pause menu":
                        if self.button_input(mouse_pos, 527, SCREEN_HEIGHT*6/7, 110, 50): # RESUME BUTTON
                            is_waiting = False
                        elif self.button_input(mouse_pos, 665, SCREEN_HEIGHT*6/7, 110, 50): # QUIT BUTTON
                            is_waiting = False
                            self.game.is_playing = False
                            self.game.is_running = False
                            sys.exit()
                    elif menu == "game over menu":
                        if self.button_input(mouse_pos, 450, SCREEN_HEIGHT*6/7, 110, 50): # PLAY AGAIN BUTTON
                            is_waiting = False
                        elif self.button_input(mouse_pos, 580, SCREEN_HEIGHT*6/7, 110, 50): # MAIN MENU BUTTON
                            self.draw_start_menu()
                            is_waiting = False
                        elif self.button_input(mouse_pos, 710, SCREEN_HEIGHT*6/7, 110, 50): # QUIT BUTTON
                            is_waiting = False
                            self.game.is_playing = False
                            self.game.is_running = False
                            sys.exit()


    def draw_start_menu(self):
        self.game.screen.fill((255, 255, 255))
        background = pg.transform.scale(pg.image.load(background_start).convert_alpha(), (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.game.screen.blit(background, (0, 0))
        self.draw_text(SCREEN_TITLE, 52, (255, 255, 255), (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), True)
        self.draw_button(350, SCREEN_HEIGHT * 6 / 7, 110, 40, (0, 200, 0), 14, (255, 255, 255), (0, 0, 0), text="START")
        self.draw_button(500, SCREEN_HEIGHT * 6 / 7, 110, 40, (30, 60, 255), 14, (255, 255, 255), (0, 0, 0), text="SCORES")
        self.draw_button(650, SCREEN_HEIGHT * 6 / 7, 110, 40, (255, 100, 0), 14, (255, 255, 255), (0, 0, 0), text="ABOUT")
        self.draw_button(800, SCREEN_HEIGHT * 6 / 7, 110, 40, (255, 0, 30), 14, (255, 255, 255), (0, 0, 0), text="QUIT")
        self.draw_text("Use WASD to move!", 32, (0, 0, 0), (SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 / 4))
        pg.display.update()
        self.wait_for_click('start menu')


    def draw_game_over_menu(self):
        self.game.screen.fill((255, 255, 255))
        background = pg.transform.scale(pg.image.load(background_over).convert_alpha(), (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.game.screen.blit(background, (0, 0))
        self.draw_text("GAME OVER", 68, (255, 255, 255), (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), True, (0, 0, 0))
        self.draw_text("Score: {}".format(self.game.score), 22, (255, 255, 255),
                       (SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 / 4))
        self.draw_button(450, SCREEN_HEIGHT * 6 / 7, 110, 50, (0, 200, 0), 14, (255, 255, 255), (0, 0, 0), text="PLAY AGAIN")
        self.draw_button(580, SCREEN_HEIGHT * 6 / 7, 110, 50, (255, 200, 0), 14, (255, 255, 255), (0, 0 ,0), text="MAIN MENU")
        self.draw_button(710, SCREEN_HEIGHT * 6 / 7, 110, 50, (255, 0, 30), 14, (255, 255, 255), (0, 0, 0), text="QUIT")
        if self.game.score > self.game.high_score:
            self.game.high_score = self.game.score
            self.draw_text("NEW HIGH SCORE", 38, (255, 255, 255), (SCREEN_WIDTH / 2, 40), True, (0, 0, 0))
            with open(high_score_path, "w") as file:
                file.write(str(self.game.high_score))
        pg.display.update()
        self.wait_for_click('game over menu')


    def draw_pause_menu(self):
        with open(high_score_path, "r") as file:
            try:
                self.game.high_score = int(file.read())
            except ValueError:
                self.game.high_score = 0
        self.game.screen.fill((0, 0, 0))
        background = pg.transform.scale(pg.image.load(background_pause).convert_alpha(), (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.game.screen.blit(background, (0, 0))
        self.draw_text("PAUSED", 78, (255, 255, 255), (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 6), True, (0, 0, 0))
        self.draw_text(f"HIGH SCORE: {self.game.high_score}", 28, (255, 255, 255),
                       (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        self.draw_text(f"YOUR SCORE: {self.game.score}", 22, (255, 255, 255),
                       (SCREEN_WIDTH / 2, 530))
        self.draw_button(520, SCREEN_HEIGHT * 6 / 7, 110, 50, (255, 200, 0), 14, (255, 255, 255), (0, 0, 0), text="RESUME")
        self.draw_button(658, SCREEN_HEIGHT * 6 / 7, 110, 50, (255, 0, 30), 14, (255, 255, 255), (0, 0, 0), text="QUIT")
        pg.display.update()
        self.wait_for_click('pause menu')


    def draw_leaderboard_menu(self):
        with open(high_score_path, "r") as file:
            try:
                self.game.high_score = int(file.read())
            except ValueError:
                self.game.high_score = 0
        self.game.screen.fill((255, 255, 255))
        background = pg.transform.scale(pg.image.load(background_score).convert_alpha(), (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.game.screen.blit(background, (0, 0))
        self.draw_text("HIGH SCORE", 52, (255, 255, 255), (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), True, (0, 0, 0))
        self.draw_text("High score: {}".format(self.game.high_score), 22, (255, 255, 255),
                       (SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 / 4))
        self.draw_button(567, SCREEN_HEIGHT * 6 / 7, 140, 50, (0, 0, 0), 14, (255, 255, 255), text="BACK")
        pg.display.update()
        self.wait_for_click('leaderboard')


    def draw_about_menu(self):
        self.game.screen.fill((255, 255, 255))
        background = pg.transform.scale(pg.image.load(background_about).convert_alpha(), (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.game.screen.blit(background, (0, 0))
        self.draw_text("ABOUT", 52, (255, 255, 255), (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 7), True, (0, 0, 0))
        self.draw_text("Our game is a roguelike 2D platformer where the player tries to kill the AI. This "
                       "is a game where the player is the boss and the AI adapts to their patterns.", 19,
                       (0, 0, 0), (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3))
        self.draw_text("It will have pixel/sprite graphics and will be programmed primarily in Python. The "
                       "defining feature of this game entails that the AI learns your moves",
                       19,
                       (0, 0, 0), (SCREEN_WIDTH / 2, 263))
        self.draw_text("and eventually either you improve or let the AI get to you.Each time the AI improves,"
                       "we give the player a chance by improving the player’s statistics.", 19,
                       (0, 0, 0), (SCREEN_WIDTH / 2, 285))
        self.draw_text("Khoa Hoang", 25, (0, 0, 0), (200, SCREEN_HEIGHT / 2))
        self.draw_text("Matthew Innaurato", 25, (0, 0, 0), (500, SCREEN_HEIGHT / 2))
        self.draw_text("Pratham Kwatra", 25, (0, 0, 0), (750, SCREEN_HEIGHT / 2))
        self.draw_text("Adrienne Lhuc Estrella", 25, (0, 0, 0), (1050, SCREEN_HEIGHT / 2))
        self.draw_button(580, SCREEN_HEIGHT * 6 / 7, 110, 40, (0, 0, 0), 14, (255, 255, 255), text="BACK")
        adrienne = pg.transform.scale(pg.image.load(adrienne_path).convert(), (120, 160))
        self.game.screen.blit(adrienne, (990, 400))
        khoa = pg.transform.scale(pg.image.load(khoa_path).convert(), (120, 160))
        self.game.screen.blit(khoa, (140, 400))
        pg.display.update()
        self.wait_for_click('about menu')

    # Player's health bar
    def draw_health_bar(self):
        health = pg.transform.scale(pg.image.load(health_path).convert_alpha(), (22,22))
        self.game.screen.blit(health, (35, 40))
        pg.draw.rect(self.game.screen, (255, 0, 0), (60, 43, 100, 16))
        pg.draw.rect(self.game.screen, (0, 255, 0), (60, 43, 100 - (10 * (10 - self.game.player.health)), 16))

    # Player's ammo bar
    def draw_ammo_bar(self):
        ammo = pg.transform.scale(pg.image.load(ammo_path).convert_alpha(), (22,22))
        self.game.screen.blit(ammo, (35, 73))
        pg.draw.rect(self.game.screen, (255, 0, 0), (60, 74, 100, 16))
        pg.draw.rect(self.game.screen, (0, 255, 0), (60, 74, 100 - (10 * (10 - self.game.player.gun.ammo)), 16))

    # Boss's health bar
    def boss_health_bar(self):
        health = pg.transform.scale(pg.image.load(health_path).convert_alpha(), (22,22))
        self.game.screen.blit(health, (1110, 40))
        pg.draw.rect(self.game.screen, (255, 0, 0), (1135, 43, 100, 16))
        pg.draw.rect(self.game.screen, (0, 255, 0), (1135, 43, 100 - (10 * (10 - self.game.boss.health)), 16))
