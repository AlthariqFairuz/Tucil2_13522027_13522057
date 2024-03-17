import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from models import Point
from divide_and_conquer import create_bezier
from brute_force import brute_force_bezier
import time
def visualize_curves(real_curve, curve_1, curve_2):
    # Create a figure and axis for plotting
    fig, ax = plt.subplots()

    # Set the limits for the plot based on the maximum x and y values of all curves
    max_x = max([point.x for point in real_curve + curve_1 + curve_2])
    max_y = max([point.y for point in real_curve + curve_1 + curve_2])
    ax.set_xlim(min([point.x for point in real_curve]) - 2, max_x + 2)
    ax.set_ylim(min([point.y for point in real_curve]) - 2, max_y + 2)

    # Initialize empty lines, scatter plots, and line plots
    line_real, = ax.plot([], [], label='Real Curve')
    scatter_curve_1 = ax.scatter([], [], color='red', label='Curve 1')
    scatter_curve_2 = ax.scatter([], [], color='blue', label='Curve 2')
    scatter_real = ax.scatter([], [], color='green', label='Real Curve Points')

    lines = [line_real]
    line_curve_1, = ax.plot([], [], color='red', linestyle='--', label='Curve 1 Line')
    line_curve_2, = ax.plot([], [], color='blue', linestyle='--', label='Curve 2 Line')

    # Initialization function for the animation
    def init():
        for line in lines:
            ax.add_line(line)
        # Return the elements to be updated in the animation
        return lines + [scatter_curve_1, scatter_curve_2, line_curve_1, line_curve_2, scatter_real]

    # Update function for each frame of the animation
    def update(frame):
        # Update data for the real curve and scatter plot
        x_real = [point.x for point in real_curve[:frame + 1]]
        y_real = [point.y for point in real_curve[:frame + 1]]
        line_real.set_data(x_real, y_real)
        scatter_real.set_offsets([(x, y) for x, y in zip(x_real, y_real)])

        # Update data and plot for Curve 1 if frame is within range
        if frame < len(curve_1):
            x_curve_1 = [point.x for point in curve_1[:frame + 1]]
            y_curve_1 = [point.y for point in curve_1[:frame + 1]]
            scatter_curve_1.set_offsets([(x, y) for x, y in zip(x_curve_1, y_curve_1)])
            line_curve_1.set_data(x_curve_1, y_curve_1)

            # Remove the previous line and draw a new line connecting Curve 1 to Real Curve
            if hasattr(update, 'line_connect_1'):
                update.line_connect_1.remove()
            update.line_connect_1 = ax.plot([curve_1[frame].x, real_curve[frame].x],
                                             [curve_1[frame].y, real_curve[frame].y],
                                             color='purple', linestyle=':')[0]

        # Update data and plot for Curve 2 if frame is within range
        if frame < len(curve_2):
            x_curve_2 = [point.x for point in curve_2[:frame + 1]]
            y_curve_2 = [point.y for point in curve_2[:frame + 1]]
            scatter_curve_2.set_offsets([(x, y) for x, y in zip(x_curve_2, y_curve_2)])
            line_curve_2.set_data(x_curve_2, y_curve_2)

            # Remove the previous line and draw a new line connecting Curve 2 to Real Curve
            if hasattr(update, 'line_connect_2'):
                update.line_connect_2.remove()
            update.line_connect_2 = ax.plot([curve_2[frame].x, real_curve[frame].x],
                                             [curve_2[frame].y, real_curve[frame].y],
                                             color='orange', linestyle=':')[0]

        # Return the elements to be updated in the animation
        return lines + [scatter_curve_1, scatter_curve_2, line_curve_1, line_curve_2, scatter_real]

    # Create the animation using FuncAnimation
    ani = FuncAnimation(fig, update, frames=max(len(real_curve), len(curve_1), len(curve_2)),
                        init_func=init, blit=False, repeat=False)

    # Set plot title, labels, grid, and legend
    plt.title('Bezier Curves Animation')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
    plt.legend()
    plt.show()
    
def run_multithreaded_create_bezier(controlPoint1, controlPoint2, controlPoint3, iterations):
    curve = create_bezier(controlPoint1, controlPoint2, controlPoint3, iterations)
    # For this case, only real_curve is used for visualization
    real_curve = curve
    curve_1, curve_2 = [], []  # Not used
    visualize_curves(real_curve, curve_1, curve_2)

print("Method available:")
print("1. Brute Force\n2. Divide and Conquer\n3. Exit\n")
method = int(input("Choose method: "))

while method not in [1, 2, 3]:
    print("Invalid method")
    method = int(input("Choose method: "))

if method == 3:
    print("Program exited.\n")
    exit()

print("Input your points")

a = input("P0: ").split(",")
P0 = Point(float(a[0]), float(a[1]))

b = input("P1: ").split(",")
P1 = Point(float(b[0]), float(b[1]))

c = input("P2: ").split(",")
P2 = Point(float(c[0]), float(c[1]))
iterations = int(input("Iterations: "))
start = time.time()

if method == 1:
    real_curve, curve_1, curve_2 = brute_force_bezier(P0, P1, P2, iterations)
    visualize_curves(real_curve, curve_1, curve_2)
    
elif method == 2:
    # Panggil fungsi create_bezier dengan multithreading
    run_multithreaded_create_bezier(P0, P1, P2, iterations)

end = time.time()
print("Duration: ", end - start)

# Visualize the animation of three Bezier curves