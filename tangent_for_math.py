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


import sympy as sp

def approximate_gradient(equation_str, variable_str='x', h=1e-5):
    variable = sp.symbols(variable_str)
    equation = sp.sympify(equation_str)

    def secant_slope(x_value, h):
        # Define the function from the equation
        function = sp.lambdify(variable, equation)
        
        # Compute the function values at x_value and x_value + h
        f_x = function(x_value)
        f_x_h = function(x_value + h)
        
        # Compute the slope of the secant line
        slope = (f_x_h - f_x) / h
        return slope

    return secant_slope

def gradient(equation_value, x_value):
    print(f"Gradient at x = {x_value}: {equation_value}")

while True:
    curve_equation = input('Curve equation: ')
    tangent_point = input('Tangent point (separate with a comma and a space): ')
    tangent_point = tangent_point.split(',')

    x_value = float(tangent_point[0].strip())
    
    secant_slope_function = approximate_gradient(curve_equation)
    
    equation_value = secant_slope_function(x_value, 10**-5)
    
    gradient(equation_value, x_value)
    print('\n')
