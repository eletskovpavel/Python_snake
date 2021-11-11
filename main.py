#import
import pygame
from random import randrange

#Constants
WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = (900,500)
OBJECT_SIZE = 10

#Varibles and inits
pygame.init()

screen = pygame.display.set_mode(WINDOW_SIZE)
positionX = randrange(0,WINDOW_WIDTH,OBJECT_SIZE)
positionY = randrange(0,WINDOW_HEIGHT,OBJECT_SIZE)
bodySnake = [(positionX,positionY)]
lengthSnake = 1
dx , dy = 0,0
fps = 15
apple = randrange(0,WINDOW_WIDTH,OBJECT_SIZE),randrange(0,WINDOW_HEIGHT,OBJECT_SIZE)

#traffic dictionary
trafficDict = {"W": (0, -1), "S": (0,1), "A": (-1,0), "D": (1,0)}

while True:
    #update screen
    pygame.display.flip() 
    #Paint screen black
    screen.fill(pygame.Color('black')) 
    for i,j in bodySnake:
        pygame.draw.rect(screen, pygame.Color('green'), (i, j, OBJECT_SIZE, OBJECT_SIZE))
    #create apple
    pygame.draw.rect(screen, pygame.Color('red'), (*apple, OBJECT_SIZE, OBJECT_SIZE))
    #changing snake's coordinats
    positionX += dx * OBJECT_SIZE
    positionY += dy * OBJECT_SIZE
    bodySnake.append((positionX,positionY))
    bodySnake = bodySnake[-lengthSnake:]
    #eating apples
    if bodySnake [-1] == apple:
        apple = randrange(0,WINDOW_WIDTH,OBJECT_SIZE),randrange(0,WINDOW_HEIGHT,OBJECT_SIZE)
        lengthSnake += 1
        fps += 1
    #things for keyboard
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and (dx,dy) != trafficDict['S']:
        dx,dy = trafficDict['W']    
    if key[pygame.K_s] and (dx,dy) != trafficDict['W']:
        dx,dy = trafficDict['S'] 
    if key[pygame.K_a] and (dx,dy) != trafficDict['D']:
        dx,dy = trafficDict['A'] 
    if key[pygame.K_d] and (dx,dy) != trafficDict['A']:
        dx,dy = trafficDict['D'] 
    #This is for closing programm
    if positionX < 0 or positionX > WINDOW_WIDTH or positionY < 0 or positionY > WINDOW_HEIGHT:
            break
    if len(bodySnake) != len(set(bodySnake)):
        break
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    #fps control
    clock = pygame.time.Clock()
    clock.tick(fps)
