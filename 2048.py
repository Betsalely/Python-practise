import random
import numpy as np
import pygame

# Constants
row_count = 4
col_count = 4
square_size = 100
width = col_count * square_size
height = row_count * square_size
size = (width, height)
RADIUS = int(square_size/2-5)

# Colors
blue = (0, 0, 200)
yellow = (200, 200, 0)
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 200, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# Function to create the initial game board
def create_board():
    board = np.zeros((row_count, col_count))
    # Add two random tiles with values of 2
    for _ in range(2):
        add_new_tile(board)
    return board

# Function to add a new random tile with a value of 2
def add_new_tile(board):
    empty_cells = [(r, c) for r in range(row_count) for c in range(col_count) if board[r][c] == 0]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = 2

# Function to draw the game board on the screen
def draw_board(board):
    screen.fill(green)
    for r in range(row_count):
        for c in range(col_count):
            value = int(board[r][c])
            color = white if value != 0 else black
            pygame.draw.rect(screen, color, (c*square_size, r*square_size, square_size, square_size))
            if value != 0:
                font = pygame.font.Font(None, 36)
                text = font.render(str(value), True, black)
                text_rect = text.get_rect(center=(c*square_size+square_size//2, r*square_size+square_size//2))
                screen.blit(text, text_rect)
    pygame.display.update()

# Function to move tiles in a specific direction
def move_tiles(board, direction):
    if direction == 'UP':
        for c in range(col_count):
            for r in range(1, row_count):
                if board[r][c] != 0:
                    for i in range(r, 0, -1):
                        if board[i-1][c] == 0:
                            board[i-1][c] = board[i][c]
                            board[i][c] = 0
                        elif board[i-1][c] == board[i][c]:
                            board[i-1][c] *= 2
                            board[i][c] = 0
                            break
    elif direction == 'DOWN':
        for c in range(col_count):
            for r in range(row_count-2, -1, -1):
                if board[r][c] != 0:
                    for i in range(r, row_count-1):
                        if board[i+1][c] == 0:
                            board[i+1][c] = board[i][c]
                            board[i][c] = 0
                        elif board[i+1][c] == board[i][c]:
                            board[i+1][c] *= 2
                            board[i][c] = 0
                            break
    elif direction == 'LEFT':
        for r in range(row_count):
            for c in range(1, col_count):
                if board[r][c] != 0:
                    for j in range(c, 0, -1):
                        if board[r][j-1] == 0:
                            board[r][j-1] = board[r][j]
                            board[r][j] = 0
                        elif board[r][j-1] == board[r][j]:
                            board[r][j-1] *= 2
                            board[r][j] = 0
                            break
    elif direction == 'RIGHT':
        for r in range(row_count):
            for c in range(col_count-2, -1, -1):
                if board[r][c] != 0:
                    for j in range(c, col_count-1):
                        if board[r][j+1] == 0:
                            board[r][j+1] = board[r][j]
                            board[r][j] = 0
                        elif board[r][j+1] == board[r][j]:
                            board[r][j+1] *= 2
                            board[r][j] = 0
                            break

# Function to check if the game is over
def is_game_over(board):
    for r in range(row_count):
        for c in range(col_count):
            if board[r][c] == 0:
                return False
            if r+1 < row_count and board[r][c] == board[r+1][c]:
                return False
            if c+1 < col_count and board[r][c] == board[r][c+1]:
                return False
    return True

# Main game loop
board = create_board()
draw_board(board)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_tiles(board, 'UP')
            elif event.key == pygame.K_DOWN:
                move_tiles(board, 'DOWN')
            elif event.key == pygame.K_LEFT:
                move_tiles(board, 'LEFT')
            elif event.key == pygame.K_RIGHT:
                move_tiles(board, 'RIGHT')
            add_new_tile(board)
            draw_board(board)
            if is_game_over(board):
                print("Game Over!")
                running = False
    clock.tick(60)

pygame.quit()

