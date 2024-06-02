import numpy as np
import pygame
import sys

def create_board():
    board = np.zeros((3, 3))
    return board

def drop_piece(board, row, col, piece):
    board[int(row)][int(col)] = piece

def print_board(board):
    print(np.flip(board, 0))

def valid_place(board, row, col):
    if int(row) >= 0 and int(row) < 3 and int(col) >= 0 and int(col) < 3:
        return board[int(row)][int(col)] == 0
    return False

def winning_move(board, piece):
    # Check horizontal locations
    for r in range(3):
        if all([board[r][c] == piece for c in range(3)]):
            return True
    # Check vertical locations
    for c in range(3):
        if all([board[r][c] == piece for r in range(3)]):
            return True
    # Check positively sloped diagonals
    if all([board[i][i] == piece for i in range(3)]):
        return True
    # Check negatively sloped diagonals
    if all([board[i][2-i] == piece for i in range(3)]):
        return True
    return False

def draw_board(board):
    screen.fill(white)
    for c in range(3):
        for r in range(3):
            pygame.draw.rect(screen, blue, (c * square_size, r * square_size, square_size, square_size), 3)
            if board[r][c] == 1:
                pygame.draw.line(screen, red, (c * square_size + 15, r * square_size + 15), ((c + 1) * square_size - 15, (r + 1) * square_size - 15), 15)
                pygame.draw.line(screen, red, (c * square_size + 15, (r + 1) * square_size - 15), ((c + 1) * square_size - 15, r * square_size + 15), 15)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, yellow, (int(c * square_size + square_size / 2), int(r * square_size + square_size / 2)), radius, 15)
    pygame.display.update()

def calculate_best_move(board):
    lines = [
        [[0, 0], [0, 1], [0, 2]],  # First horizontal
        [[1, 0], [1, 1], [1, 2]],  # Second horizontal
        [[2, 0], [2, 1], [2, 2]],  # Third horizontal
        [[0, 0], [1, 0], [2, 0]],  # First vertical
        [[0, 1], [1, 1], [2, 1]],  # Second vertical
        [[0, 2], [1, 2], [2, 2]],  # Third vertical
        [[0, 0], [1, 1], [2, 2]],  # Diagonal from top-left to bottom-right
        [[0, 2], [1, 1], [2, 0]]   # Diagonal from top-right to bottom-left
    ]

    for piece in [2, 1]:  # Check for AI win first, then player block
        for line in lines:
            values = [board[r][c] for r, c in line]
            if values.count(piece) == 2 and values.count(0) == 1:
                empty_pos = line[values.index(0)]
                return empty_pos

    # No immediate win or block, take the first available spot (simple strategy)
    for r in range(3):
        for c in range(3):
            if board[r][c] == 0:
                return [r, c]

# Initialize the game board
board = create_board()
game_over = False
turn = 1

# Initialize Pygame
pygame.init()

# Screen settings
square_size = 200
width = 3 * square_size
height = 3 * square_size
size = (width, height)
radius = int(square_size / 2 - 15)

# Colors
red = (200, 0, 0)
blue = (0, 0, 200)
yellow = (200, 200, 0)
white = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tic-Tac-Toe")

# Draw the initial board
draw_board(board)

# Game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and turn == 1:
            posx, posy = event.pos
            col = posx // square_size
            row = posy // square_size

            if valid_place(board, row, col):
                drop_piece(board, row, col, 1)
                if winning_move(board, 1):
                    print("Player 1 wins!")
                    game_over = True
                turn = 2
                draw_board(board)
    
    if turn == 2 and not game_over:
        pygame.time.wait(500)
        row, col = calculate_best_move(board)
        drop_piece(board, row, col, 2)
        if winning_move(board, 2):
            print("Player 2 wins!")
            game_over = True
        turn = 1
        draw_board(board)
    
    if game_over:
        pygame.time.wait(3000)
        pygame.quit()
        sys.exit()
