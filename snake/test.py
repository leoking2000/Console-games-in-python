# this is for learning purposes
from snake.gamelogic import *
import pygame

green = (0,255,0)
red = (255,0,0)
black = (0, 0, 0)
display_width = 600
display_height = 600
FPS = 10
block_size = 10

pygame.init()
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Snake-Game") #add icon?
clock = pygame.time.Clock() # game clock

gameRunning = True
player = Cell(display_width // 2, display_height // 2, speed=block_size)

while gameRunning:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_UP or event.key == pygame.K_w :
                player.go_up()
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s :
                player.go_down()
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d :
                player.go_right()
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player.go_left()
        elif event.type == pygame.QUIT:
            gameRunning = False

    if  player.x >= display_width or player.x < 0 or player.y >= display_height or player.y < 0 :
        gameRunning = False

    player.update()
    gameDisplay.fill(black)
    pygame.draw.rect(gameDisplay, red, [player.x, player.y, block_size, block_size])
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
quit()
