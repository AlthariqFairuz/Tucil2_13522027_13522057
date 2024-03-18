import timeit
from models import Point
from brute_force import BruteForceBezier  # Tambahkan import ini untuk BruteForceBezier
from divide_and_conquer import DNCBezier  # Tambahkan import ini untuk DNCBezier
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
    bruteforce = BruteForceBezier(points_input, iterations)  # Tambahkan ini
    
    stmt = lambda: bruteforce.create_bezier_curve()
    duration = timeit.timeit(stmt, number=1) * 1000  # Convert to milliseconds
    curve = stmt()
    bruteforce.visualize_curves()
elif method == 2:
    dnc = DNCBezier(points_input, iterations)
    stmt = lambda: dnc.calculate_dnc_bezier_points()  # Ubah pemanggilan ini
    duration = timeit.timeit(stmt, number=1) * 1000
    curves = stmt()
    dnc.visualize_curves_dnc()  # Tambahkan pemanggilan fungsi visualize_curves_dnc

print(f"Duration: {duration:.2f} milliseconds")
