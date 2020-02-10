import pygame
import controls
from src.player import *

def main():


    player = Player(1, np.array([100, 100]), np.array([0,0]), np.array([0,0]))

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
    weaponImg = pygame.image.load('resources/sprites/gun.png')
    weaponImg = pygame.transform.scale(weaponImg, (32,32))

    # Initialize game clock for tracking FPS and timers
    clock = pygame.time.Clock()

    # Display FPS later in game loop
    FPS = 30
    FPSFont = pygame.font.SysFont("monospace", 26)

    # Display timer later in game loop
    timerFont = pygame.font.SysFont("monospace", 26)

    # Display pause menu later in game loop
    pauseFont = pygame.font.SysFont("monospace", 46)

    # Display start screen before game loop
    titleFont = pygame.font.SysFont("monospace", 96)

    # Use this font for smaller, generic messages
    genFont = pygame.font.SysFont("monospace", 24)

    # Returns difference between current time and earlier time entered as parameter
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

    # Display start menu
    screen.fill((0, 0, 0))
    startMenu = titleFont.render("PLAY THIS GAME!", True, (255, 255, 255))
    screen.blit(startMenu, (500, 320))
    startMenu = genFont.render("Press any button to continue...", True, (255, 255, 255))
    screen.blit(startMenu, (500, 200))
    pygame.display.update()

    # Wait for user input before starting game
    # TODO: Configure this for more options such as showing scoreboard
    waiting = True
    while waiting:
        clock.tick(10)
        for event in pygame.event.get():
            # Warning: Capslock counts as keydown
            if event.type == pygame.KEYDOWN:
                waiting = False

    # GAME LOOP
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
        FPSText = FPSFont.render("FPS: {:.2f}".format(clock.get_fps()), False, (0, 0, 0))
        screen.blit(FPSText, (0, 0))

        startTime = 0
        timerText = timerFont.render("Time elapsed: {:.2f}".format(getTimeElapsed(startTime) / 1000), False, (0, 0, 0))
        screen.blit(timerText, (0, 20))

        player.doKeyState()
        player.updatePhysics()

        screen.blit(playerImg, (player.pos[0], player.pos[1]))
        screen.blit(weaponImg, (player.pos[0], player.pos[1]))
        # WARNING: update() function below does not work for python3.7 on MacOS Catalina unless using anaconda3
        pygame.display.update()


if __name__ == "__main__":
    main()
else:
    print("You ran the program from the wrong module. Please run \'main.py\'.")
