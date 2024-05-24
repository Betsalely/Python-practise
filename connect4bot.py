import numpy as np
import pygame
import sys
import math
import random

blue = (0, 0, 200)
black = (0, 0, 0)
red = (200, 0, 0)
yellow = (200, 200, 0)

row_count = 6
col_count = 7

def create_board():
    board = np.zeros((row_count, col_count))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[row_count-1][col] == 0

def get_next_open_row(board, col):
    for r in range(row_count):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board, 0))

def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(col_count-3):
        for r in range(row_count):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check vertical locations for win
    for c in range(col_count):
        for r in range(row_count-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check positively sloped diagonals
    for c in range(col_count-3):
        for r in range(row_count-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check negatively sloped diagonals
    for c in range(col_count-3):
        for r in range(3, row_count):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

def evaluate_window(window, piece):
    score = 0
    opp_piece = 1 if piece == 2 else 2

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(0) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(0) == 2:
        score += 2

    if window.count(opp_piece) == 3 and window.count(0) == 1:
        score -= 4

    return score

def score_position(board, piece):
    score = 0

    # Center column preference
    center_array = [int(i) for i in list(board[:, col_count//2])]
    center_count = center_array.count(piece)
    score += center_count * 3

    # Horizontal score
    for r in range(row_count):
        row_array = [int(i) for i in list(board[r, :])]
        for c in range(col_count-3):
            window = row_array[c:c+4]
            score += evaluate_window(window, piece)

    # Vertical score
    for c in range(col_count):
        col_array = [int(i) for i in list(board[:, c])]
        for r in range(row_count-3):
            window = col_array[r:r+4]
            score += evaluate_window(window, piece)

    # Positive diagonal score
    for r in range(row_count-3):
        for c in range(col_count-3):
            window = [board[r+i][c+i] for i in range(4)]
            score += evaluate_window(window, piece)

    # Negative diagonal score
    for r in range(row_count-3):
        for c in range(col_count-3):
            window = [board[r+3-i][c+i] for i in range(4)]
            score += evaluate_window(window, piece)

    return score

def is_terminal_node(board):
    return winning_move(board, 1) or winning_move(board, 2) or len(get_valid_locations(board)) == 0

def minimax(board, depth, alpha, beta, maximizingPlayer):
    valid_locations = get_valid_locations(board)
    is_terminal = is_terminal_node(board)
    if depth == 0 or is_terminal:
        if is_terminal:
            if winning_move(board, 2):
                return (None, 100000000000000)
            elif winning_move(board, 1):
                return (None, -10000000000000)
            else: # No more valid moves
                return (None, 0)
        else: # Depth is zero
            return (None, score_position(board, 2))
    if maximizingPlayer:
        value = -math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, 2)
            new_score = minimax(b_copy, depth-1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value
    else: # Minimizing player
        value = math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, 1)
            new_score = minimax(b_copy, depth-1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value

def get_valid_locations(board):
    valid_locations = []
    for col in range(col_count):
        if is_valid_location(board, col):
            valid_locations.append(col)
    return valid_locations

def draw_board(board):
    for c in range(col_count):
        for r in range(row_count):
            pygame.draw.rect(screen, blue, (c*squareSize, r*squareSize+squareSize, squareSize, squareSize))
            pygame.draw.circle(screen, black, (int(c*squareSize+squareSize/2), int(r*squareSize+squareSize+squareSize/2)), RADIUS)
    
    for c in range(col_count):
        for r in range(row_count):
            if board[r][c] == 1:
                pygame.draw.circle(screen, red, (int(c*squareSize+squareSize/2), height - int(r*squareSize+squareSize/2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, yellow, (int(c*squareSize+squareSize/2), height - int(r*squareSize+squareSize/2)), RADIUS)

    pygame.display.update()

board = create_board()
print_board(board)
game_over = False
turn = 1

pygame.init()

squareSize = 100
width = col_count * squareSize
height = (row_count + 1) * squareSize

size = (width, height)

RADIUS = int(squareSize / 2 - 5)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont('monospace', 75)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, black, (0, 0, width, squareSize))
            posx = event.pos[0]
            if turn == 1:
                pygame.draw.circle(screen, red, (posx, int(squareSize / 2)), RADIUS)
            pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, black, (0, 0, width, squareSize))
            # Player 1
            if turn == 1:
                posx = event.pos[0]
                col = int(math.floor(posx / squareSize))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)

                    if winning_move(board, 1):
                        label = myfont.render("PLAYER 1 WINS!", 1, red)
                        screen.blit(label, (40, 10))
                        game_over = True

                    turn = 2
                    print_board(board)
                    draw_board(board)

    # AI Turn
    if turn == 2 and not game_over:
        col, minimax_score = minimax(board, 4, -math.inf, math.inf, True)

        if is_valid_location(board, col):
            pygame.time.wait(500)
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)

            if winning_move(board, 2):
                label = myfont.render("PLAYER 2 WINS!", 1, yellow)
                screen.blit(label, (40, 10))
                game_over = True

            print_board(board)
            draw_board(board)

            turn = 1

    if game_over:
        pygame.time.wait(5000)
