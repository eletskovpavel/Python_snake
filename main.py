#import
import pygame
from random import randrange

#Constants
WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = (300,300)
OBJECT_SIZE = 10

#Varibles and inits
pygame.init()

screen = pygame.display.set_mode(WINDOW_SIZE)
startPositionX = randrange(0,WINDOW_WIDTH,OBJECT_SIZE)
startPositionY = randrange(0,WINDOW_HEIGHT,OBJECT_SIZE)
bodySnake = [(startPositionX,startPositionY)]
lengthSnake = 1

while True:
    #update screen
    pygame.display.flip() 
    #Paint screen black
    screen.fill(pygame.Color('black')) 
    for i,j in bodySnake:
        pygame.draw.rect(screen, pygame.Color('green'), (i, j, OBJECT_SIZE, OBJECT_SIZE))
    if startPositionX < 0 or startPositionX > WINDOW_WIDTH or startPositionY < 0 or startPositionY > WINDOW_HEIGHT:
        break
    #This is for closing programm
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
