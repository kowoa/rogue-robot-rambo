import pygame
from src.player import *
from src.physics import *

def main():

    pygame.init()
    # Initialize display, icon, background
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Boss Battle")
    icon = pygame.image.load("resources/sprites/oubliette.png")
    pygame.display.set_icon(icon)
    background = pygame.image.load("resources/backgrounds/background1.png")

    # Initialize player object
    playerImg = pygame.image.load("resources/sprites/boss.png")
    playerImg = pygame.transform.scale(playerImg, (32, 32))

    # Initialize game clock for tracking FPS and timers
    clock = pygame.time.Clock()

    # Display FPS later in game loop
    FPS = 30
    FPSFont = pygame.font.SysFont("monospace", 26)

    # Display timer later in game loop
    timerFont = pygame.font.SysFont("monospace", 26)

    # Display pause menu later in game loop
    pauseFont = pygame.font.SysFont("monospace", 46)

    # Returns difference between current time and earlier time entered as parameter
    startTime = pygame.time.get_ticks()
    def getTimeElapsed(startTime):
        return pygame.time.get_ticks() - startTime

    # Display and undisplay pause menu
    def pause():
        paused = True

        # Loop for pause function
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                # Option to continue or quit in pause menu
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        paused = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()
            # Displays Pause menu
            screen.fill((255, 255, 255))
            pauseMenu = pauseFont.render("Paused", True, (0, 0, 200))
            screen.blit(pauseMenu, (500, 320))

            optionsMenu = pauseFont.render("Press C to Continue or Q to Quit", True, (0, 0, 200))
            screen.blit(optionsMenu, (200, 440))

            pygame.display.update()
            clock.tick(FPS)

    # Game loop
    isRunning = True
    while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
            # Calls pause function when the key P is pressed.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause()

        screen.blit(background, (0, 0))

        # If there is any jittering, replace this with 'clock.tick_busy_loop(FPS)'
        clock.tick(FPS)
        FPSText = FPSFont.render("FPS: {:.2f}".format(clock.get_fps()), True, (0, 0, 0))
        screen.blit(FPSText, (0, 0))

        timerText = timerFont.render("Time elapsed: {:.2f}".format(getTimeElapsed() / 1000), True, (0, 0, 0))
        screen.blit(timerText, (0, 20))

        # WARNING: update() function below does not work for python3.7 on MacOS Catalina unless using anaconda3
        pygame.display.update()


if __name__ == "__main__":
    main()
else:
    print("You ran the program from the wrong module. Please run \'main.py\'.")