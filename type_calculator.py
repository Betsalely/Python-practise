import math
import random




print('as of right now you can only do basic function like times, add, subtract, divide and square and the numbers have to be under 12')

while True:
    
    listOfInputNumbers = []
    listOfOperations = []



    inputs = input('Type in you word math problem: ')

    list_input = inputs.split(" ")

    numbers_l = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
    numbers_n = [0,1,2,3,4,5,6,7,8,9,10,11,12]
    operations_square = ['squared']
    operations_plus = ['add', 'plus', 'sum', 'total']
    operations_minus = ['subtract', 'take away', 'minus']
    operations_times = ['times', 'multiply', 'product']
    operations_divide = ['divide']
   
    

    
    for word in list_input:
        if word in numbers_l:
            listOfInputNumbers.append(numbers_l.index(word))
        elif word in operations_plus:
            listOfOperations.append('+')
        elif word in operations_minus:
            listOfOperations.append('-')
        elif word in operations_times:
            listOfOperations.append('*')
        elif word in operations_divide:
            listOfOperations.append('/')
        elif word in operations_square:
            listOfOperations.append('**')
        
        

           
    

    # print("Numbers: ", listOfInputNumbers)
    # print("Operations: ", listOfOperations)

        
    if len(listOfInputNumbers) == len(listOfOperations) + 1:
        sum = listOfInputNumbers[0]  # Start with the first number

        for i in range(len(listOfOperations)):
            if listOfOperations[i] == '+':
                sum += listOfInputNumbers[i + 1]
            elif listOfOperations[i] == '-':
                sum -= listOfInputNumbers[i + 1]
            elif listOfOperations[i] == '*':
                sum *= listOfInputNumbers[i + 1]
            elif listOfOperations[i] == '/':
                if listOfInputNumbers[i + 1] != 0:
                    sum /= listOfInputNumbers[i + 1]


                else:
                    sum = 'Error: Division by zero'
                    break


            elif listOfOperations[i] == '**':
                sum **= listOfInputNumbers[i + 1]

        print("The result is:", sum)
    else:
        print('This equation does not make sense. The ratio of numbers to operators should be n+1:n.')
