import pygame
import numpy as np


col_count = 13
row_count = 18

blue = (0, 0, 200)
red = (200, 0, 0)
black = (0, 0, 0)

square_size = 40
width = col_count * square_size
height = row_count * square_size
size = (width, height)


pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption("Pygame Board")

def create_board():
    board = np.zeros((row_count, col_count))
    return board

def draw_board(board):
    # screen.fill(black) 
    for row in range(row_count):
        for col in range(col_count):
            pygame.draw.rect(screen, blue, (col * square_size, row * square_size, square_size, square_size))
            pygame.draw.rect(screen, black, (col * square_size, row * square_size, square_size, square_size), 1)
    pygame.display.update()

def create_floor():
    for col in range(col_count):
        pygame.draw.rect(screen, ((col*18),0,0), (col * square_size, (row_count - 1) * square_size, square_size, square_size))
        pygame.draw.rect(screen, black, (col * square_size, (row_count - 1) * square_size, square_size, square_size), 1)
    pygame.display.update()

board = create_board()
draw_board(board)
create_floor() 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

     

    clock.tick(30)

pygame.quit()
