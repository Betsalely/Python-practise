import math
import random




print('as of right now you can only do basic function like times, add, subtract, divide and square and the numbers have to be under 100. seperate two digits numbers with a hyphen like twnety-one')

while True:
    
    listOfInputNumbers = []
    listOfOperations = []



    inputs = input('Type in you word math problem (no punctuation): ')

    list_input = inputs.split(" ")
    list_input = [i.lower() for i in list_input]
    numbers_l = [
    'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 
    'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty-one', 'twenty-two', 
    'twenty-three', 'twenty-four', 'twenty-five', 'twenty-six', 'twenty-seven', 'twenty-eight', 'twenty-nine', 
    'thirty', 'thirty-one', 'thirty-two', 'thirty-three', 'thirty-four', 'thirty-five', 'thirty-six', 'thirty-seven', 
    'thirty-eight', 'thirty-nine', 'forty', 'forty-one', 'forty-two', 'forty-three', 'forty-four', 'forty-five', 
    'forty-six', 'forty-seven', 'forty-eight', 'forty-nine', 'fifty', 'fifty-one', 'fifty-two', 'fifty-three', 
    'fifty-four', 'fifty-five', 'fifty-six', 'fifty-seven', 'fifty-eight', 'fifty-nine', 'sixty', 'sixty-one', 
    'sixty-two', 'sixty-three', 'sixty-four', 'sixty-five', 'sixty-six', 'sixty-seven', 'sixty-eight', 'sixty-nine', 
    'seventy', 'seventy-one', 'seventy-two', 'seventy-three', 'seventy-four', 'seventy-five', 'seventy-six', 
    'seventy-seven', 'seventy-eight', 'seventy-nine', 'eighty', 'eighty-one', 'eighty-two', 'eighty-three', 
    'eighty-four', 'eighty-five', 'eighty-six', 'eighty-seven', 'eighty-eight', 'eighty-nine', 'ninety', 
    'ninety-one', 'ninety-two', 'ninety-three', 'ninety-four', 'ninety-five', 'ninety-six', 'ninety-seven', 
    'ninety-eight', 'ninety-nine'
]

    numbers_n = list(range(100))

    operations_square = ['squared']
    operations_plus = ['add', 'plus', 'sum', 'total', 'more', 'started', 'ended', "another"]
    operations_minus = ['subtract', 'take', 'away', 'minus', 'lose', 'lost', 'gave', 'gives']
    operations_times = ['times', 'multiply', 'product', 'multiplied', 'each']
    operations_divide = ['divide', 'divided', 'split']
   
    

    
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
        
        

           
    

    print("Numbers: ", listOfInputNumbers)
    print("Operations: ", listOfOperations)

        
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
