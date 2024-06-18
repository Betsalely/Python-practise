import pygame
import numpy as np
import random
import colorsys

# Initialize Pygame
pygame.init()

# Constants
row_count = 12
col_count = 15
square_size = 50
width = col_count * square_size
height = row_count * square_size
size = (width, height)

# Colors
red = (200, 0, 0)
blue = (0, 0, 200)
yellow = (200, 200, 0)
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 200, 0)

# Initialize screen
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Snake initialization
snake_pos = [(5, 5), (5, 4), (5, 3)]  # List of tuples (row, col)
snake_dir = 'RIGHT'
food_pos = (random.randint(0, row_count-1), random.randint(0, col_count-1))
score = 0
hue = 0

def draw_board():
    screen.fill(green)
    for c in range(col_count):
        for r in range(row_count):
            pygame.draw.rect(screen, black, (c * square_size, r * square_size, square_size, square_size), 1)

def draw_snake():
    for pos in snake_pos:
        # Draw white outline
        outline_rect = pygame.Rect(pos[1] * square_size, pos[0] * square_size, square_size, square_size)
        pygame.draw.rect(screen, white, outline_rect)

        # Draw the snake's body
        body_rect = pygame.Rect(pos[1] * square_size + 3, pos[0] * square_size + 3, square_size - 6, square_size - 6)
        pygame.draw.rect(screen, blue, body_rect)

def draw_food():
    global hue
    hue = (hue + 0.01) % 1.0  # Increment the hue value
    rainbow_color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    rainbow_color = tuple(int(i * 255) for i in rainbow_color)
    pygame.draw.rect(screen, rainbow_color, (food_pos[1] * square_size, food_pos[0] * square_size, square_size, square_size))

def draw_score(score):
    score_text = font.render(f"Score: {score}", True, white)
    screen.blit(score_text, (10, 10))


def move_snake():
    global food_pos, score
    head_x, head_y = snake_pos[0]
    if snake_dir == 'UP':
        new_head = (head_x - 1, head_y)
    elif snake_dir == 'DOWN':
        new_head = (head_x + 1, head_y)
    elif snake_dir == 'LEFT':
        new_head = (head_x, head_y - 1)
    elif snake_dir == 'RIGHT':
        new_head = (head_x, head_y + 1)
    
    snake_pos.insert(0, new_head)

    if new_head == food_pos:
        score += 1
        food_pos = (random.randint(0, row_count-1), random.randint(0, col_count-1))
    else:
        snake_pos.pop()

def check_collisions():
    head = snake_pos[0]
    if (head[0] < 0 or head[0] >= row_count or
        head[1] < 0 or head[1] >= col_count or
        head in snake_pos[1:]):
        return True
    return False

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != 'DOWN':
                snake_dir = 'UP'
            elif event.key == pygame.K_DOWN and snake_dir != 'UP':
                snake_dir = 'DOWN'
            elif event.key == pygame.K_LEFT and snake_dir != 'RIGHT':
                snake_dir = 'LEFT'
            elif event.key == pygame.K_RIGHT and snake_dir != 'LEFT':
                snake_dir = 'RIGHT'

    move_snake()
    if check_collisions():
        running = False

    draw_board()
    draw_snake()
    draw_food()
    draw_score(score)
    pygame.display.update()
    clock.tick(5)  # Control the speed of the snake

pygame.quit()
print(f"Game Over! Your score was: {score}")
