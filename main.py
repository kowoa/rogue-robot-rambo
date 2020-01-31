import pygame
import tracker

def main():
    # Initialize pygame
    pygame.init()

    # Create screen with 1280x720 resolution
    screen = pygame.display.set_mode((1280, 720))

    # Title and icon
    pygame.display.set_caption("Boss Battle")
    # TODO: replace icon image
    icon = pygame.image.load("oubliette.png")
    pygame.display.set_icon(icon)

    # Display player
    # TODO: replace player image
    playerImg = pygame.image.load("terror.png")
    playerImg = pygame.transform.scale(playerImg, (128, 128))
    playerX = 640
    playerY = 360
    def displayPlayer():
        screen.blit(playerImg, (playerX, playerY))

    clock = pygame.time.Clock()
    # Display FPS later in game loop
    FPS = 30
    FPSFont = pygame.font.SysFont("monospace", 26)

    # Display timer later in game loop
    timerFont = pygame.font.SysFont("monospace", 26)

    # Game loop
    isRunning = True
    while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False

        # RGB background
        screen.fill((255, 255, 0))

        displayPlayer()

        # If there is any jittering, replace this with 'clock.tick_busy_loop(FPS)'
        clock.tick(FPS)
        FPSText = FPSFont.render("FPS: {:.2f}".format(clock.get_fps()), False, (0, 0, 0))
        screen.blit(FPSText, (0, 0))

        timerText = timerFont.render("Time elapsed: {:.2f}".format(tracker.getTimeElapsed()), False, (0, 0, 0))
        screen.blit(timerText, (0, 20))

        # WARNING: update() function below does not work for python3.7 on MacOS Catalina unless using anaconda3
        pygame.display.update()

if __name__ == "__main__":
    main()
else:
    print("You ran the program from the wrong module. Please run \'main.py\'.")