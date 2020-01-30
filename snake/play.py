from snake.gamelogic import *
import pygame

green = (0,255,0)
red = (255,0,0)
black = (0, 0, 0)

display_width = 600
display_height = 600
FPS = 5

block_size = 10

pygame.init()
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Snake-Game") #add icon?
clock = pygame.time.Clock() # game clock

font = pygame.font.SysFont(None, 25)
def message_to_display(msg, collor):
    text = font.render(msg, True, collor)
    gameDisplay.blit(text, [display_width // 2 - 100, display_height // 2])
    pygame.display.update()


def main():
    snake = Snake(display_width // 2, display_height // 2, block_size, red,\
                  display_width, display_height)
    apple = Apple(block_size, green, display_width, display_height)
    gameRunning = True
    gameOver = False

    while gameRunning:

        while gameOver:
            gameDisplay.fill(black)
            message_to_display("GAME OVER\nPlay again(y/n)",green)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        gameOver = False
                        snake.reset()
                        apple.update()
                    elif event.key == pygame.K_n:
                        gameRunning = False
                        gameOver = False

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_UP or event.key == pygame.K_w :
                    snake.go_up()
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s :
                    snake.go_down()
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d :
                    snake.go_right()
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    snake.go_left()
            elif event.type == pygame.QUIT:
                gameRunning = False

        if  snake.outside_the_boundaries(): gameOver = True
        snake.update()
        if snake.found_Apple(apple): snake.eat_aplle(apple)

        gameDisplay.fill(black)
        apple.draw(gameDisplay)
        snake.draw(gameDisplay)
        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()
    quit()

if __name__ == "__main__":
    main()
