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

    def wait_for_click(self, screen):
        is_waiting = True
        while is_waiting:
            self.game.clock.tick(10)
            for event in pygame.event.get():
                # Warning: caplock counts as keydown
                mousePos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    is_waiting = False
                    self.game.is_playing = False
                    self.game.is_running = False
                if event.type == pygame.MOUSEBUTTONUP:
                    if screen == 'start menu':
                        if self.interactive_button(mousePos, 350, SCREEN_HEIGHT*6/7, 110, 40): # START BUTTON
                            is_waiting = False
                        elif self.interactive_button(mousePos, 500, SCREEN_HEIGHT*6/7, 110, 40): # SCORE BUTTON
                            self.draw_leaderboard_menu()
                        elif self.interactive_button(mousePos, 650, SCREEN_HEIGHT*6/7, 110, 40): # ABOUT BUTTON
                            self.draw_about_menu()
                        elif self.interactive_button(mousePos, 800, SCREEN_HEIGHT*6/7, 110, 40): # QUIT BUTTON
                            is_waiting = False
                            self.game.is_playing = False
                            self.game.is_running = False
                    elif screen == 'leaderboard':
                        if self.interactive_button(mousePos, 567, SCREEN_HEIGHT*6/7, 140, 50): # BACK BUTTON
                            self.draw_start_menu()
                    elif screen == 'score menu':
                        if self.interactive_button(mousePos, 567, SCREEN_HEIGHT*6/7, 140, 50): # RESUME BUTTON
                            is_waiting = False
                    elif screen == 'game over menu':
                        if self.interactive_button(mousePos, 527, SCREEN_HEIGHT*6/7, 110, 50): # PLAY AGAIN BUTTON
                            is_waiting = False
                        elif self.interactive_button(mousePos, 665, SCREEN_HEIGHT*6/7, 110, 50): # END BUTTON
                            is_waiting = False
                            self.game.is_playing = False
                            self.game.is_running = False

    # Use this method to display a button on the position of the scren for your liking
    # Enter a rgb color for outline, color, and text color parameter
    def create_button(self, x, y, width, height, color, text_size, text_color, outline = None, text = ''):
        if outline:
            pygame.draw.rect(self.game.screen, outline, (x - 2, y - 2, width + 4, height + 4), 0)
        
        pygame.draw.rect(self.game.screen, color, (x, y, width, height), 0)

        if text != '':
            pygame.font.init()
            font = pygame.font.Font(self.font_name, text_size)
            text = font.render(text, 1, text_color)
            self.game.screen.blit(text, (x + (width / 2 - text.get_width() / 2), y + 
                                        (height / 2 - text.get_height() / 2)))

    # Use method to be an interactive button
    '''The position parameter is the positon of the mouse, use 'position = pygame.mouse.get_pos()' 
        in wait_for_click() to keep track of the position of the mouse. Also must create an event when
        the mouse clicks the button it creates an action.'''
    def interactive_button(self, position, x, y, width, height):
        # x, y, width, and height should be the same as the ones you used for the button 
        if position[0] > x and position[0] < x + width:
            if position[1] > y and position[1] < y + height:
                return True
        return False

    def draw_start_menu(self):
        self.game.screen.fill((0, 0, 0))
        self.draw_text(SCREEN_TITLE, 48, (255, 255, 255), (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        self.create_button(350, SCREEN_HEIGHT*6/7, 110, 40, (255,255,255), 14, (0,0,0), text = "START")
        self.create_button(500, SCREEN_HEIGHT*6/7, 110, 40, (255,255,255), 14, (0,0,0), text = "SCORES")
        self.create_button(650, SCREEN_HEIGHT*6/7, 110, 40, (255,255,255), 14, (0,0,0), text = "ABOUT")
        self.create_button(800, SCREEN_HEIGHT*6/7, 110, 40, (255,255,255), 14, (0,0,0), text = "QUIT")
        self.draw_text("Use WASD to move!", 22, (255, 255, 255), (SCREEN_WIDTH/2, SCREEN_HEIGHT*3/4))
        header = pygame.transform.scale(pygame.image.load(header_path).convert(), (400, 200))
        self.game.screen.blit(header, (440, SCREEN_HEIGHT / 6))
        pygame.display.update()
        self.wait_for_click('start menu')

    def draw_game_over_menu(self):
        self.game.screen.fill((0, 0, 0))
        self.draw_text("GAME OVER", 48, (255, 255, 255), (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        self.draw_text("Score: {}".format(self.game.player.score), 22, (255, 255, 255),
                       (SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 / 4))
        self.create_button(527, SCREEN_HEIGHT*6/7, 110, 50, (255,255,255), 14, (0,0,0), text = "PLAY AGAIN")
        self.create_button(665, SCREEN_HEIGHT*6/7, 110, 50, (255,255,255), 14, (0,0,0), text = "QUIT")
        if self.game.player.score > self.game.high_score:
            self.game.high_score = self.game.player.score
            self.draw_text("NEW HIGH SCORE", 36, (255, 255, 255), (SCREEN_WIDTH / 2, 10))
            with open(high_score_path, "w") as file:
                file.write(str(self.game.high_score))
        pygame.display.update()
        self.wait_for_click('game over menu')

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
        self.create_button(567, SCREEN_HEIGHT*6/7, 140, 50, (255,255,255), 14, (0,0,0), text = "RESUME")
        pygame.display.update()
        self.wait_for_click('score menu')

    def draw_leaderboard_menu(self):
        with open(high_score_path, "r") as file:
            try:
                self.game.high_score = int(file.read())
            except ValueError:
                self.game.high_score = 0
        self.game.screen.fill((0, 0, 0))
        self.draw_text("HIGH SCORE", 48, (255, 255, 255), (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        self.draw_text("High score: {}".format(self.game.high_score), 22, (255, 255, 255),
                       (SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 / 4))
        self.create_button(567, SCREEN_HEIGHT*6/7, 140, 50, (255,255,255), 14, (0,0,0), text = "BACK")
        pygame.display.update()
        self.wait_for_click('leaderboard')
    
    def draw_about_menu(self):
        pass