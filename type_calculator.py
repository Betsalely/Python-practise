# import math
# import random




# print('as of right now you can only do basic function like times, add, subtract, divide and square and the numbers have to be under 100. seperate two digits numbers with a hyphen like twnety-one')

# while True:
    
#     listOfInputNumbers = []
#     listOfOperations = []



#     inputs = input('Type in you word math problem (no punctuation): ')

#     list_input = inputs.split(" ")
#     list_input = [i.lower() for i in list_input]
#     numbers_l = [
#     'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 
#     'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty-one', 'twenty-two', 
#     'twenty-three', 'twenty-four', 'twenty-five', 'twenty-six', 'twenty-seven', 'twenty-eight', 'twenty-nine', 
#     'thirty', 'thirty-one', 'thirty-two', 'thirty-three', 'thirty-four', 'thirty-five', 'thirty-six', 'thirty-seven', 
#     'thirty-eight', 'thirty-nine', 'forty', 'forty-one', 'forty-two', 'forty-three', 'forty-four', 'forty-five', 
#     'forty-six', 'forty-seven', 'forty-eight', 'forty-nine', 'fifty', 'fifty-one', 'fifty-two', 'fifty-three', 
#     'fifty-four', 'fifty-five', 'fifty-six', 'fifty-seven', 'fifty-eight', 'fifty-nine', 'sixty', 'sixty-one', 
#     'sixty-two', 'sixty-three', 'sixty-four', 'sixty-five', 'sixty-six', 'sixty-seven', 'sixty-eight', 'sixty-nine', 
#     'seventy', 'seventy-one', 'seventy-two', 'seventy-three', 'seventy-four', 'seventy-five', 'seventy-six', 
#     'seventy-seven', 'seventy-eight', 'seventy-nine', 'eighty', 'eighty-one', 'eighty-two', 'eighty-three', 
#     'eighty-four', 'eighty-five', 'eighty-six', 'eighty-seven', 'eighty-eight', 'eighty-nine', 'ninety', 
#     'ninety-one', 'ninety-two', 'ninety-three', 'ninety-four', 'ninety-five', 'ninety-six', 'ninety-seven', 
#     'ninety-eight', 'ninety-nine'
# ]

#     numbers_n = list(range(100))

#     operations_square = ['squared']
#     operations_plus = ['add', 'plus', 'sum', 'total', 'more', 'started', 'ended', "another"]
#     operations_minus = ['subtract', 'take', 'away', 'minus', 'lose', 'lost', 'gave', 'gives']
#     operations_times = ['times', 'multiply', 'product', 'multiplied', 'each']
#     operations_divide = ['divide', 'divided', 'split']
   
    

    
#     for word in list_input:
#         if word in numbers_l:
#             listOfInputNumbers.append(numbers_l.index(word))
#         elif word in operations_plus:
#             listOfOperations.append('+')
#         elif word in operations_minus:
#             listOfOperations.append('-')
#         elif word in operations_times:
#             listOfOperations.append('*')
#         elif word in operations_divide:
#             listOfOperations.append('/')
#         elif word in operations_square:
#             listOfOperations.append('**')
        
        

           
    

#     print("Numbers: ", listOfInputNumbers)
#     print("Operations: ", listOfOperations)

        
#     if len(listOfInputNumbers) == len(listOfOperations) + 1:
#         sum = listOfInputNumbers[0]  # Start with the first number

#         for i in range(len(listOfOperations)):
#             if listOfOperations[i] == '+':
#                 sum += listOfInputNumbers[i + 1]
#             elif listOfOperations[i] == '-':
#                 sum -= listOfInputNumbers[i + 1]
#             elif listOfOperations[i] == '*':
#                 sum *= listOfInputNumbers[i + 1]
#             elif listOfOperations[i] == '/':
#                 if listOfInputNumbers[i + 1] != 0:
#                     sum /= listOfInputNumbers[i + 1]


#                 else:
#                     sum = 'Error: Division by zero'
#                     break


#             elif listOfOperations[i] == '**':
#                 sum **= listOfInputNumbers[i + 1]

#         print("The result is:", sum)
#     else:
#         print('This equation does not make sense. The ratio of numbers to operators should be n+1:n.')
import pygame
import numpy as np


#this is how many columns and rows there in our grid/screen
col_count = 13
row_count = 18

#we are declaring the RGB values for the colours before we use them.

#for the sky
blue = (0, 0, 200)
#for the floor amd maybe the columns
red = (200, 0, 0)
#also for the floor
black = (0, 0, 0)

#player
yellow = (200, 200, 0)

#this is how big our squares are. we could make them samller but i think bigger squares are great 
#for our end users. the rest if the code is just for the peremeters of the screen
square_size = 40
width = col_count * square_size
height = row_count * square_size
size = (width, height)


#player y position (x position doesnt change
current_pos = 7

#starts pygame, sets up the csreen and the name for out app/game.
pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.display.set_caption("Pygame Board")
def create_board():
    board = np.zeros((row_count, col_count))
    return board

def draw_board(board):
    #thius is for the background of the boaard.
    for row in range(row_count):
        for col in range(col_count):
            pygame.draw.rect(screen, blue, (col * square_size, row * square_size, square_size, square_size))
            pygame.draw.rect(screen, black, (col * square_size, row * square_size, square_size, square_size), 1)
    pygame.display.update()


def draw_floor(floor_pattern):
    for col in range(col_count):
        pygame.draw.rect(screen, ((col*18),0,0), (col * square_size, (row_count - 1) * square_size, square_size, square_size))
        color = floor_pattern[col]
        pygame.draw.rect(screen, color, (col * square_size, (row_count - 1) * square_size, square_size, square_size))
        pygame.draw.rect(screen, black, (col * square_size, (row_count - 1) * square_size, square_size, square_size), 1)

def move_floor(floor_pattern):
    screen.fill(black)  
    draw_board(board)   # Redraw the board

    # restarts floor pattern
    floor_pattern = floor_pattern[1:] + floor_pattern[:1]

    draw_floor(floor_pattern)
    pygame.display.update()
    return floor_pattern

#checks if the player can go up
def possible_up():
    return current_pos > 0

#creates a player and moves it up or down. += means down and vice versa because of how the board is drawn
def draw_player(current_pos, direction):
    if direction == 'UP':
        if possible_up():
            current_pos -= 1

    else:
        if current_pos < row_count - 2: 
            current_pos += 1

    #empty screen
    screen.fill(black)
    draw_board(board)
    draw_floor(floor_pattern)

    #actual player
    pygame.draw.rect(screen, yellow, (6 * square_size, current_pos * square_size, square_size, square_size))
    pygame.draw.rect(screen, black,  (6 * square_size, current_pos * square_size, square_size, square_size), 1)
    pygame.display.update()

    return current_pos

#for floor gradient
floor_pattern = [((col * 18) % 256, 0, 0) for col in range(col_count)]


board = create_board()
draw_board(board)
draw_floor(floor_pattern)

#main game loop
while True:
    upper = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
        elif event.type == pygame.KEYDOWN:
            #space bar pressed
            if event.key == pygame.K_SPACE:
                current_pos = draw_player(current_pos, "UP")
                upper = True


    floor_pattern = move_floor(floor_pattern)
    #moves it down if spavce is not pressed
    if not upper:
        current_pos = draw_player(current_pos, "DOWN")

    #so time passes
    clock.tick(5)