from brute_force import brute_force_bezier
from models import Point
import matplotlib.pyplot as plt

print("Method available:")
print("1. Brute Force\n2. Divide and Conquer\n3. Exit\n")
method = int(input("Choose method: "))

while (method != 1 and method != 2 and method != 3):
    print("Invalid method")
    method = int(input("Choose method: "))

if (method == 1):
    print("Input your points")

    a = input("P0: ").split(",")
    P0 = Point(float(a[0]), float(a[1]))

    b = input("P1: ").split(",")
    P1 = Point(float(b[0]), float(b[1]))

    c = input("P2: ").split(",")
    P2 = Point(float(c[0]), float(c[1]))

    iterations = int(input("Iterations: "))

    curve = brute_force_bezier(P0, P1, P2, iterations)
    x, y = zip(*curve)

    plt.plot(x, y)
    plt.show()

elif (method == 2) :
    pass

elif (method == 3):
    print("Program exited.\n")
    exit()