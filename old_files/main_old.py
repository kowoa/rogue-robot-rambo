from old_files.characters import *
from src.constants import *
from os import path


def main():
    pygame.init()

    icon = pygame.image.load(SCREEN_ICON)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    score_dir = path.dirname(__file__)

    player = Player()
    gun = Gun()
    enemy = Enemy()
    
##    platform = Platform(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)

    charSprites.add(player, enemy)
    itemSprites.add(gun)

##    platformSprites.add(platform)

    # TODO: Replace background with something low resolution to improve FPS
    background = pygame.image.load("resources/backgrounds/background1.png")
    background = background.convert()
    pygame.mixer.music.load("resources/music/background_music.mp3")
    pygame.mixer.music.play(-1)
    pygame.display.set_caption(SCREEN_TITLE)
    pygame.display.set_icon(icon)

    # Returns difference between current time and earlier time entered as parameter
    def getTimeElapsed(startTime):
        return pygame.time.get_ticks() - startTime
    
    # Returns and keeps track of the user's highscore 
    def loadScore():
        with open(path.join(score_dir, SCORE_FILE), 'r') as f:
            try:
                curr_score = f.readlines()
                curr_score = [x.rstrip() for x in curr_score]
                curr_score = curr_score[-1]
                return curr_score
            except:
                curr_score = 0
                
            f.close()

    # Displays the scoreboard
    def score():
        scoring = True
        # Loop for scoreboard
        while scoring:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()    
                    quit()
                # Option to continue in scoreboard
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        scoring = False
            # Reads the user's previous scores
            with open(path.join(score_dir, SCORE_FILE), 'r') as f:
                prev_scores = f.readlines()
                prev_scores = [x.rstrip() for x in prev_scores]
                temp_scores = []
                for num in prev_scores:
                    temp_scores.append(int(num))
                temp_scores.sort(reverse = True)
                highscore = str(temp_scores[0])
                second = str(temp_scores[1])
                third = str(temp_scores[2])
                fourth = str(temp_scores[3])
                fifth = str(temp_scores[4])

                f.close()

            screen.fill((105, 105, 105))
            scoreBoard = FONT_XLARGE.render("Scoreboard", True,  (255, 0, 0))
            screen.blit(scoreBoard, (500, 60))

            scoreNumber = FONT_LARGE.render('You scored ' + str(loadScore()) + ' points', True, (0, 0, 150))
            screen.blit(scoreNumber, (390, 200))

            scoreHeadings = FONT_MEDIUM.render('Rank     Score', True, (0,0,0))
            screen.blit(scoreHeadings, (580, 320))

            scoreHigh = FONT_SMALL.render('1.                ' + highscore, True, (255, 255, 255))
            screen.blit(scoreHigh, (580, 380))
            scoreSecond = FONT_SMALL.render('2.                ' + second, True, (255, 255, 255))
            screen.blit(scoreSecond, (580, 425))
            scoreThird = FONT_SMALL.render('3.                ' + third, True, (255, 255, 255))
            screen.blit(scoreThird, (580, 470))
            scoreFourth = FONT_SMALL.render('4.                ' + fourth, True, (255, 255, 255))
            screen.blit(scoreFourth, (580, 515))
            scoreFifth = FONT_SMALL.render('5.                ' + fifth, True, (255, 255, 255))
            screen.blit(scoreFifth, (580, 560))

            scoreExit = FONT_SMALL.render('Press C to continue game', True, (255, 255, 255))
            screen.blit(scoreExit, (580, 605))
            
            pygame.display.update()
            clock.tick(FPS)

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
            screen.blit(pauseMenu, (520, 260))

            optionsMenu = FONT_MEDIUM.render("Press C to Continue or Q to Quit", True, (0, 0, 200))
            screen.blit(optionsMenu, (280, 360))

            pygame.display.update()
            clock.tick(FPS)

    # Display start menu
    screen.fill((0, 0, 0))
    
    startMenu = FONT_LARGE.render("PLAY THIS GAME!", True, (255, 255, 255))
    screen.blit(startMenu, (500, 320))
    startMenu = FONT_SMALL.render("Press any button to continue...", True, (255, 255, 255))
    screen.blit(startMenu, (500, 200))
    sco_re= 0 
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
                elif event.key == pygame.K_m:
                    score()

        # Time step for movement and physics
        dt = clock.tick_busy_loop(FPS)
        
        screen.fill((255, 255, 255))
        screen.blit(background, (0, 0))

        player.update(dt)
        gun.update(dt, player.rect.x, player.rect.y)
        enemy.update(dt)
        bulletSpritesPlayer.update(dt)
        
        if pygame.sprite.spritecollide(player, bulletSpritesPlayer, True):
            sco_re += 1
##        if pygame.sprite.spritecollide(enemy, bulletSpritesPlayer, True):
##            score += 2

        charSprites.draw(screen)
        itemSprites.draw(screen)

        bulletSpritesPlayer.draw(screen)

##        platformSprites.draw(screen)

        FPSText = FONT_SMALL.render("FPS: {:.2f}".format(clock.get_fps()), False, (0, 0, 0))
        screen.blit(FPSText, (0, 0))

        startTime = 0
        timerText = FONT_SMALL.render("Time elapsed: {:.2f}".format(getTimeElapsed(startTime) / 1000), False, (0, 0, 0))
        screen.blit(timerText, (0, 20))

        scoreText = FONT_SMALL.render("Score: " + str(sco_re), False, (0,0,0))
        screen.blit(scoreText, (1120, 0))

        # WARNING: update() function below does not work for python3.7 on MacOS Catalina unless using anaconda3
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
else:
    print("You ran the program from the wrong module. Please run \'main.py\'.")