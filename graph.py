import matplotlib.pyplot as plt



coordinates = 100

while True:
    x1 = list(range(1, coordinates+1))
    y1 = []

    equation = input('equation: ')

    # Check if the input is correctly formatted as "y = equation"
    if equation.lower().startswith('y ='):
        equation = equation[3:].strip()  # Remove 'y =' and any leading/trailing spaces

        for x in x1:
            try:
                # Safely evaluate the equation by replacing 'x' with the current value of x
                y = eval(equation, {"__builtins__": None}, {"x": x, "math": __import__("math")})
        
                y1.append(y)
            except Exception as e:
                print(f"Error evaluating equation for x = {x}: {e}")
                y1.append(None)  # Append None or some placeholder for error cases

        # Check if y1 has the same number of elements as x1
        if len(y1) == len(x1):
            # Plot the results if there were no errors
            plt.plot(x1, y1, marker='o', markersize=0.5)
            plt.title('Graph of the equation')
            plt.xlabel('x')
            plt.ylabel('y')
            plt.xlim(1, coordinates+ round(int(coordinates/10)))

            if eval(equation, {"__builtins__": None}, {"x": coordinates, "math": __import__("math")}) < coordinates:
                plt.ylim(1, coordinates+ round(int(coordinates/10)))
            else:
                plt.ylim(1, eval(equation, {"__builtins__": None}, {"x": coordinates, "math": __import__("math")}) + round(int(coordinates/10)))

            plt.grid(True)
            plt.show()
        else:
            print("Error: y1 does not have the same number of elements as x1.")
    else:
        print("Error: The equation must start with 'y ='.")
