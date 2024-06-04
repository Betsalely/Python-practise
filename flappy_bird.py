import pygame
import numpy as np

col_count = 25
row_count = 18

blue = (0, 0, 200)
red = (200, 0, 0)
black = (0, 0, 0)
yellow = (200, 200, 0)

square_size = 40
width = col_count * square_size
height = row_count * square_size
size = (width, height)

current_pos = 7

pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption("Pygame Board")

def create_board():
    board = np.zeros((row_count, col_count))
    return board

def draw_board(board):
    for row in range(row_count):
        for col in range(col_count):
            pygame.draw.rect(screen, blue, (col * square_size, row * square_size, square_size, square_size))
            pygame.draw.rect(screen, black, (col * square_size, row * square_size, square_size, square_size), 1)

def draw_floor(floor_pattern):
    for col in range(col_count):
        color = floor_pattern[col]
        pygame.draw.rect(screen, color, (col * square_size, (row_count - 1) * square_size, square_size, square_size))
        pygame.draw.rect(screen, black, (col * square_size, (row_count - 1) * square_size, square_size, square_size), 1)

def move_floor(floor_pattern, column_pos, gap_start):
    screen.fill(black)  # Clear the screen before redrawing
    draw_board(board)   # Redraw the board
    
    # Move floor pattern and column position to the left
    floor_pattern = floor_pattern[1:] + floor_pattern[:1]
    column_pos = (column_pos - 1) % col_count
    
    draw_floor(floor_pattern)
    draw_pipes(column_pos, gap_start)
    pygame.display.update()
    return floor_pattern, column_pos

def possible_up():
    return current_pos > 0

def draw_player(current_pos, direction):
    if direction == 'UP':
        if possible_up():
            current_pos -= 1
    else:
        if current_pos < row_count - 2: 
            current_pos += 1

    screen.fill(black)

    draw_board(board)
    draw_floor(floor_pattern)
    draw_pipes(column_pos, gap_start)
    
    pygame.draw.rect(screen, yellow, (6 * square_size, current_pos * square_size, square_size, square_size))
    pygame.draw.rect(screen, black,  (6 * square_size, current_pos * square_size, square_size, square_size), 1)
    pygame.display.update()

    return current_pos

def draw_pipes(column_pos, gap_start):
    for row in range(row_count - 1):
        if row < gap_start or row >= gap_start + 4:
            pygame.draw.rect(screen, red, (column_pos * square_size, row * square_size, square_size, square_size))
            pygame.draw.rect(screen, black, (column_pos * square_size, row * square_size, square_size, square_size), 1)

gap_start = np.random.randint(0, row_count - 5)  # Randomly initialize the gap start position
floor_pattern = [((col * 18) % 256, 0, 0) for col in range(col_count)]
column_pos = col_count - 1  # Start column at the rightmost position

board = create_board()
draw_board(board)
draw_floor(floor_pattern)
draw_pipes(column_pos, gap_start)

running = True
while running:
    upper = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                current_pos = draw_player(current_pos, "UP")
                upper = True

    floor_pattern, column_pos = move_floor(floor_pattern, column_pos, gap_start)
    if column_pos == col_count-1:  
        gap_start = np.random.randint(0, row_count - 5)  # Randomize the gap start position

    if not upper:
        current_pos = draw_player(current_pos, "DOWN")

        if current_pos == row_count-2:
            break

     

    clock.tick(5)





clock.tick(1)
pygame.quit()
