# This module will contain the timer and scoring system

import pygame

startTime = pygame.time.get_ticks()
def getTimeElapsed():
    return pygame.time.get_ticks() - startTime


numKills = 0
# TODO: Change this formula for calculating score
score = getTimeElapsed() + (numKills * 100)
def getScore():
    return score
