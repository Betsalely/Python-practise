import numpy as np
import pygame
import sys
import math

blue = (0,0,200)
black = (0,0,0)
red = (200, 0, 0)
yellow = (200, 200, 0)

row_count = 6
col_count = 7

def create_board():
    board = np.zeros((row_count,col_count))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board,col):
    return board[row_count-1][col] == 0

def get_next_open_row(board,col):
    for r in range(row_count):
        if board[r][col] == 0:
            return r
        
def print_board(board):
    print(np.flip(board,0))

def winning_move(board, piece):

    #horizontal
    for c in range(col_count-3):
        for r in range(row_count):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    
    #vertical
    for c in range(col_count):
        for r in range(row_count-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
    
    #positive slope dia
    for c in range(col_count-3):
        for r in range(row_count-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
    
    #negative slope dia
    for c in range(col_count-3):
        for r in range(3, row_count):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True
            

def draw_board(board):
    for c in range(col_count):
        for r in range(row_count):
            pygame.draw.rect(screen, blue, (c*squareSize, r*squareSize+squareSize, squareSize, squareSize))
            pygame.draw.circle(screen, black, (int(c*squareSize+squareSize/2),int( r*squareSize+squareSize+squareSize/2)), RADIUS )
            
    for c in range(col_count):
        for r in range(row_count):
            if board[r][c] == 1:
                pygame.draw.circle(screen, red, (int(c*squareSize+squareSize/2), height - int( r*squareSize+squareSize/2)), RADIUS )
            elif board[r][c] == 2: 
                pygame.draw.circle(screen, yellow, (int(c*squareSize+squareSize/2), height - int( r*squareSize+squareSize/2)), RADIUS )


    pygame.display.update()

    

board = create_board()
print_board(board)
game_over = False
turn = 1

pygame.init()

squareSize = 100
width = col_count * squareSize
height = (row_count + 1 * squareSize)*6.6

size = (width, height)

RADIUS = int(squareSize/2-5)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont('monospace', 75)





while not game_over:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, black, (0,0, width , squareSize))

            posx = event.pos[0]

            if turn > 0:
                pygame.draw.circle(screen, red, (posx, int(squareSize/2)), RADIUS )
            elif turn < 0:
                pygame.draw.circle(screen, yellow, (posx, int(squareSize/2)), RADIUS )
            pygame.display.update()



        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, black, (0,0, width , squareSize))
            #Player 1
            if turn > 0:
                positionX = event.pos[0]
                col = int(math.floor(positionX/squareSize))
                
                if col < 7 and col > -1:

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 1)

                        if winning_move(board, 1):
                            label = myfont.render("PLAYER 1 WIN", 1, red)
                            screen.blit(label, (40,10))
                            
                            game_over = True

                else:
                    print('that is not a valid number')
                    turn*=-1
            

            # #player 2
            else:
                positionX = event.pos[0]
                col = int(math.floor(positionX/squareSize))
                
                if col < 7 and col > -1:

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 2)

                        if winning_move(board, 2):
                            label = myfont.render("PLAYER 2 WIN", 1, yellow)
                            screen.blit(label, (40,10))
                        
                            game_over = True
                            

                        

                else:
                    print('that is not a valid number')
                    turn*=-1

        
            print_board(board)
            draw_board(board)
        



            turn *= -1
            if game_over:
                pygame.time.wait(5000)
            
    

    