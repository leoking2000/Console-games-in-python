# this is for learning purposes
from snake.gamelogic import *
import pygame

green = (0,255,0)
red = (255,0,0)

pygame.init()
gameDisplay = pygame.display.set_mode((600,600))
pygame.display.set_caption("Snake-Game") #add icon?
# game clock
clock = pygame.time.Clock()

gameRunning = True
speed = 10
player = Cell(100, 100, speedX=speed)


while gameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_UP or event.key == pygame.K_w :
                player.speedY = -speed
                player.speedX = 0
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s :
                player.speedY = speed
                player.speedX = 0
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d :
                player.speedX = speed
                player.speedY = 0
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player.speedX = -speed
                player.speedY = 0

    player.update()

    gameDisplay.fill((0, 0, 0))

    pygame.draw.rect(gameDisplay, red, [player.x, player.y, 10, 10])

    pygame.display.update()
    clock.tick(10)

pygame.quit()
quit()
