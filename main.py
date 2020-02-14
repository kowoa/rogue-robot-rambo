from random import randint
from src.player import *
from src.constants import *


def main():
    pygame.init()

    dt = 0

    icon = pygame.image.load(SCREEN_ICON)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player()
    sprites = pygame.sprite.Group(player)
    #background = screen.copy()
    #background.fill((30, 30, 30))
    #for _ in range (1000):
    #    x, y = randint(0, 1000), randint(0, 1000)
    #    pygame.draw.rect(background, pygame.Color("green"), (x, y, 2, 2))


    background = pygame.image.load("resources/backgrounds/background1.png")
    pygame.display.set_caption(SCREEN_TITLE)
    pygame.display.set_icon(icon)



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
            pauseMenu = FONT_LARGE.render("Paused", True, (0, 0, 200))
            screen.blit(pauseMenu, (500, 320))

            optionsMenu = FONT_MEDIUM.render("Press C to Continue or Q to Quit", True, (0, 0, 200))
            screen.blit(optionsMenu, (200, 440))

            pygame.display.update()
            clock.tick(FPS)

    # Display start menu
    screen.fill((0, 0, 0))
    startMenu = FONT_LARGE.render("PLAY THIS GAME!", True, (255, 255, 255))
    screen.blit(startMenu, (500, 320))
    startMenu = FONT_SMALL.render("Press any button to continue...", True, (255, 255, 255))
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
    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            # Calls pause function when the key P is pressed.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause()

        screen.blit(background, (0, 0))
        sprites.update(events, dt)
        sprites.draw(screen)

        # If there is any jittering, replace this with 'clock.tick_busy_loop(FPS)'
        dt = clock.tick(FPS)
        FPSText = FONT_SMALL.render("FPS: {:.2f}".format(clock.get_fps()), False, (0, 0, 0))
        screen.blit(FPSText, (0, 0))

        startTime = 0
        timerText = FONT_SMALL.render("Time elapsed: {:.2f}".format(getTimeElapsed(startTime) / 1000), False, (0, 0, 0))
        screen.blit(timerText, (0, 20))

        #pymunk.space.Space.step(1/FPS)
        # WARNING: update() function below does not work for python3.7 on MacOS Catalina unless using anaconda3
        pygame.display.update()

if __name__ == "__main__":
    main()
else:
    print("You ran the program from the wrong module. Please run \'main.py\'.")
