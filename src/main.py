from models import Point
from brute_force import BruteForceBezier
from divide_and_conquer import DNCBezier 

# Input Method Validation 
method = None
while method not in [1, 2, 3]:
    try:
        print("Method available:")
        print("1. Brute Force\n2. Divide and Conquer\n3. Exit\n")
        method = int(input("Choose method: "))
        if method not in [1, 2, 3]:
            print("Number not in range. Please choose 1, 2, or 3.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if method == 3:
    print("Program exited.\n")
    exit()

# Number of Points Validation
n = None
while True:
    try:
        n = int(input("Number of points: "))
        break 
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Points Input Validation
print("Input your points in the format 'x,y'. Example: 1,2\n")
points_input = []
for i in range(n):
    while True:
        point_input = input(f"P{i+1}: ").split(",")
        if len(point_input) == 2:
            try:
                x = float(point_input[0])
                y = float(point_input[1])
                points_input.append(Point(x, y))
                break  
            except ValueError:
                print("Invalid input. Please enter two numbers separated by a comma.")
        else:
            print("Invalid input format. Please enter two numbers separated by a comma.")

iterations = int(input("Iterations: "))

if method == 1:
    bruteforce = BruteForceBezier(points_input, iterations)  
    
    calculate = bruteforce.create_bezier_curve()
    bruteforce.visualize_curves()
    
elif method == 2:
    dnc = DNCBezier(points_input, iterations)
    calculate= dnc.calculate_dnc_bezier_points(iterations)
    dnc.visualize_curves_dnc() 
