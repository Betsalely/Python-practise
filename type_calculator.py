import math
import random




print('as of right now you can only do basic function like times, add, subtract, divide and square and the numbers have to be under 12')

while True:
    
    listOfInputNumbers = []


    inputs = input('Type in you word math problem: ')

    list_input = inputs.split(" ")

    numbers_l = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
    numbers_n = [1,2,3,4,5,6,7,8,9,10,11,12]

    operations_square = ['squared', 'times itself']
    operations_plus = ['add', 'plus', 'sum', 'total']
    operations_minus = ['subtract', 'take away', 'minus']
    operations_times = ['times', 'multiply', 'product']
    operations_divide = ['divide']
    
    
    for word in list_input:
        for num in numbers_l:
           if num == word:
            x = numbers_l.index(num)

            listOfInputNumbers.append(x+1)
    

    print(listOfInputNumbers)