x = ''
y = ''
n = ''

def inputs():
    global x 
    global y 
    global n  
    x = input('x: ')
    y = input("y: ")
    n = input('raised to the power of: ')

    double_check = input(f'is ({float(x)} + {float(y)})^{int(n)} correct? y/n: ')
    if double_check == 'n':
        inputs()

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact


def matrix(n,k):
    nfact = factorial(n)
    kfact = factorial(k)
    nminkfact = factorial(n - k)

    math = nfact // (kfact*nminkfact)
    return math

while True:
    inputs()

    sum = 0
    for k in range(int(n)+1):
        matrx = matrix(int(n),k)
        xvalue = float(x)**(int(n)-k)
        yvalue = float(y)**k

        math = matrx * xvalue * yvalue

        sum += math

    print(sum)