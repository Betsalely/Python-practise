# import sympy as sp

# def differentiate_curve(equation_str, variable_str='x'):

#     variable = sp.symbols(variable_str)

#     equation = sp.sympify(equation_str)

#     derivative = sp.diff(equation, variable)
    
#     return derivative

# def gradient(equation, x_value):
#     print(f"Gradient at x = {x_value}: {equation}")

# while True:
#     curve_equation = input('Curve equation: ')
#     tangent_point = input('Tangent point (separate with a comma and a space): ')
#     tangent_point = tangent_point.split(',')

#     x_value = float(tangent_point[0].strip())
    
#     derivative = differentiate_curve(curve_equation)

#     derivative_function = sp.lambdify(sp.symbols('x'), derivative)

#     equation_value = derivative_function(x_value)
    

    
#     # print(f"Derivative: {derivative}")

#     gradient(equation_value, x_value)


#     print('\n')

import math

list_of_gradients = []

def tangent_calculation(x,y,x1,y1):
    gradientY1 = float(y - y1)
    gradientX1 = float(x - x1)
    gradient = float(gradientY1/gradientX1)
    return gradient

def safe_eval(equation, x):
    allowed_names = {"x": x, "math": math}
    code = compile(equation, "<string>", "eval")
    for name in code.co_names:
        if name not in allowed_names:
            raise NameError(f"Use of {name} is not allowed")
    return eval(code, {"__builtins__": {}}, allowed_names)

equation = input('Enter equation : ').strip()
if equation.lower().startswith('y ='):
    equation = equation[3:].strip()
else:
    print("Please enter an equation in the form 'y = ...'")
    exit()

while True:

        try:
            x_input = input('Enter x coordinate (or type "exit" to quit): ')
            # x_input = str(i)
            if x_input.lower() == "exit":
                break
            x = int(x_input)
            y = safe_eval(equation, x)

            x1 = float(x+0.01)
            y1 = safe_eval(equation, x1)

            gradient_of_tangent = tangent_calculation(x,y,x1,y1)
            print(gradient_of_tangent)
            list_of_gradients.append(gradient_of_tangent)

            x2 = float(x-0.01)
            y2 = safe_eval(equation, x2)

            gradient_of_tangent = tangent_calculation(x,y,x1,y1)
            print(gradient_of_tangent)
            list_of_gradients.append(gradient_of_tangent)
        except ValueError:
            print("Invalid input. Please enter a valid integer for x.")
        except NameError as e:
            print(f"Error in equation: {e}")
        except Exception as e:
            print(f"Error evaluating equation for x = {x}: {e}")
    


print(list_of_gradients)
list_of_differences = []
# for i in range(len(list_of_gradients)-1):
#     dif = abs(list_of_gradients[i] - list_of_gradients[i+1])
#     list_of_differences.append(dif)

# print(list_of_differences)