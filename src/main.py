from models import Point
from divide_and_conquer import generate_bezier_dnc, visualize_curves_dnc
from brute_force import brute_force_bezier, visualize_curves
import timeit

print("Method available:")
print("1. Brute Force\n2. Divide and Conquer\n3. Exit\n")
method = int(input("Choose method: "))

while method not in [1, 2, 3]:
    print("Invalid method")
    method = int(input("Choose method: "))

if method == 3:
    print("Program exited.\n")
    exit()

n = int(input("Number of points: "))

print("Input your points")

# Get input points from the user
points_input = []
for i in range(n):
    point_input = input(f"P{i+1}: ").split(",")
    points_input.append(Point(float(point_input[0]), float(point_input[1])))

iterations = int(input("Iterations: "))

if method == 1:
    stmt = lambda: brute_force_bezier(points_input, iterations)
    duration = timeit.timeit(stmt, number=1) * 1000  # Convert to milliseconds
    curve = stmt()  # Execute the method for visualization
    visualize_curves(curve, points_input)
elif method == 2:
    stmt = lambda: generate_bezier_dnc(points_input, iterations)
    duration = timeit.timeit(stmt, number=1) * 1000  # Convert to milliseconds
    curve_points_list = stmt()  # Execute the method for visualization
    visualize_curves_dnc(curve_points_list, points_input)

print(f"Duration: {duration:.2f} milliseconds")
