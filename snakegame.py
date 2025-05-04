import pygame
import random
 
# Initialize pygame
pygame.init()
 
# Create game window
width = 600
height = 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")
 
# Colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
 
# Snake settings
snake_block = 10
snake_speed = 15
 
clock = pygame.time.Clock()
 
# Use Arial instead of Comic Sans (safer for macOS)
font = pygame.font.SysFont("arial", 35)
def show_score(score):
    value = font.render(f"Score: {score}", True, white)
    win.blit(value, [10, 10])
 
# Draw the snake
def draw_snake(snake_block, snake_list):
    for block in snake_list:
        pygame.draw.rect(win, white, [block[0], block[1], snake_block, snake_block])
 
# Game loop
def gameLoop():
    game_over = False
 
    x = width / 2
    y = height / 2
    x_change = 0
    y_change = 0
 
    snake_list = []
    snake_length = 1
 
    food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
 
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0
 
        x += x_change
        y += y_change
 
        if x >= width or x < 0 or y >= height or y < 0:
            game_over = True
 
        win.fill((30, 144, 255))  # Dodger Blue
        pygame.draw.rect(win, green, [food_x, food_y, snake_block, snake_block])
 
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
 
        for block in snake_list[:-1]:
            if block == snake_head:
                game_over = True
 
        draw_snake(snake_block, snake_list)
        pygame.display.update()
 
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            snake_length += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
# Run the game
gameLoop()