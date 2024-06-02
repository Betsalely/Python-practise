import numpy as np
# import pygame



def create_board():
    board = np.zeros((3,3))    
    return board


def drop_piece(game, row, col, piece):
    game[2-int(col)][int(row)] = piece
    print_board(game)


def print_board(game):
    print(game)


def valid_place(board, row,col):
    if (2-int(col)) > -1 and (2-int(col)) < 3 and int(row) > -1 and int(row) < 3:
        if board[2-int(col)][int(row)] == 0:
            return True
        else: 
            return False
    else: 
        return False
    
def winning_move(board, piece):
    #horizontal
    if board[0][0] == piece and board[0][1] == piece and board[0][2] == piece or board[1][0] == piece and board[1][1] == piece and board[1][2] == piece or board[2][0] == piece and board[2][1] == piece and board[2][2] == piece:
        return True
    
    #vertical
    elif board[0][0] == piece and board[1][0] == piece and board[2][0] == piece or board[0][1] == piece and board[1][1] == piece and board[2][1] == piece or board[0][2] == piece and board[1][2] == piece and board[2][2] == piece:
        return True
    
    #diagonal
    elif board[0][0] == piece and board[1][1] == piece and board[2][2] == piece or board[0][2] == piece and board[1][1] == piece and board[2][0] == piece:
        return True





board = create_board()
game_over = False
turn = 1

print_board(board)


while not game_over:
    user_input = input('choose position like "1,2" or "3,0": ')
    user_input.split(',')
    col = user_input[0]
    row = user_input[2]




    if len(user_input) == 3:
        #Player 1

        if valid_place(board,row, col):

            if turn > 0:
                drop_piece(board, row, col, 1)

                if winning_move(board, 1):
                    
                    print('player 1 wins')
                    game_over = True
                    break
            
        

            #player 2
            else:

    
                drop_piece(board, row, col, 2)

                if winning_move(board, 2):
                    
                    print('player 2 wins')
                    game_over = True
                    break
        

        else:
            print('invalid space, try again')
            turn *= -1

                    



 





        turn *= -1




