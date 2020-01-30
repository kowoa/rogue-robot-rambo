import pygame

def main():
    # Initialize pygame
    pygame.init()

    # Create screen
    screen = pygame.display.set_mode((1280, 720))

    # Title and icon
    pygame.display.set_caption("Boss Battle")
    icon = pygame.image.load("oubliette.png")
    pygame.display.set_icon(icon)

    # Game loop
    isRunning = True
    while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False

        # RGB background
        screen.fill((255, 255, 255))
        pygame.display.update()

if __name__ == "__main__":
    main()
else:
    print("You ran the program from the wrong module. Please run \'main.py\'.")