import matplotlib.pyplot as plt
import matplotlib.animation as animation
from models import Point

def calculate_pascal_triangle_row(row_number: int) -> list[int]:
    """Calculate a row in Pascal's Triangle based on the given row number."""
    if row_number == 0:
        return [1]

    row = [1]
    prev_row = [1]
    for i in range(1, row_number + 1):
        stack = [1] * (i + 1)
        for j in range(1, i):
            stack[j] = prev_row[j - 1] + prev_row[j]
        row = stack
        prev_row = stack

    return row

def bezier_curve(points: list[Point], t: float) -> Point:
    """Calculate a point on the Bezier curve for a given t value."""
    if len(points) == 1:
        return points[0]

    n = len(points) - 1
    coefficients = calculate_pascal_triangle_row(n)
    x = 0
    y = 0
    for i in range(n + 1):
        coefficient = coefficients[i] * (1 - t) ** (n - i) * t ** i
        x += coefficient * points[i].x
        y += coefficient * points[i].y
    return Point(x, y)

def brute_force_bezier(points: list[Point], iterations: int) -> list[Point]:
    """Approximate the Bezier curve by brute-force iteration."""
    curve = []
    for i in range(iterations + 1):
        t = i / iterations
        point = bezier_curve(points, t)
        curve.append(point)
    return curve

def visualize_curves(curve_points, main_points):
    """Visualize the Bezier curve and main points using matplotlib."""
    fig, ax = plt.subplots()

    # Set plot limits based on the points
    max_x = max([point.x for point in curve_points + main_points])
    max_y = max([point.y for point in curve_points + main_points])
    ax.set_xlim(min([point.x for point in main_points]) - 2, max_x + 2)
    ax.set_ylim(min([point.y for point in main_points]) - 2, max_y + 2)

    # Initialize plot elements
    line_curve, = ax.plot([], [], label='Bezier Curve')
    scatter_main_points = ax.scatter([], [], color='red', label='Main Points')
    scatter_curve_points = ax.scatter([], [], color='blue', label='Curve Points')

    lines = [line_curve]
    lines_connect = []

    def init():
        # Add lines and connections to the plot
        for line in lines:
            ax.add_line(line)

        for i in range(len(main_points) - 1):
            line_connect = ax.plot([main_points[i].x, main_points[i+1].x],
                                   [main_points[i].y, main_points[i+1].y],
                                   color='purple', linestyle=':')[0]
            lines_connect.append(line_connect)

        return lines + [scatter_main_points, scatter_curve_points] + lines_connect

    def update(frame):
        # Update curve and point positions for animation
        x_curve = [point.x for point in curve_points[:frame + 1]]
        y_curve = [point.y for point in curve_points[:frame + 1]]
        line_curve.set_data(x_curve, y_curve)
        scatter_curve_points.set_offsets([(x, y) for x, y in zip(x_curve, y_curve)])

        x_main = [point.x for point in main_points]
        y_main = [point.y for point in main_points]
        scatter_main_points.set_offsets([(x, y) for x, y in zip(x_main, y_main)])

        return lines + [scatter_main_points, scatter_curve_points] + lines_connect

    # Create the animation
    ani = animation.FuncAnimation(fig, update, frames=len(curve_points), init_func=init, blit=False, repeat=False)

    # Plot labels and legend
    plt.title('Bezier Curve Visualization')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
    plt.legend()
    plt.show()
