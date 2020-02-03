#This module will contain the pause functionality of the game
import pygame

blue = (0,0,200)
white = (255,255,255)
def pause():
    paused = True
    
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        # **Screen does not fill in white or place message onto screen. Instead exits the program.**
        screen.fill(white)
        message_to_screen("Paused",
                          blue,
                          -100,
                          size = "large"
        )
        message_to_screen("Press C to Continue or Q to Quit",
                          blue,
                          25,
        )
        pygame.display.update()
        clock.tick(60)