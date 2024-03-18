import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from typing import List
from models import Point

def mid_point(controlPoint1: Point, controlPoint2: Point) -> Point:
    mid = Point((controlPoint1.x + controlPoint2.x) / 2, (controlPoint1.y + controlPoint2.y) / 2)
    return mid

def populate_bezier_points(controlPoint1: Point, controlPoint2: Point, controlPoint3: Point, current_iteration: int, iterations: int, bezier_points: List[Point]) -> None:
    if current_iteration < iterations:
        mid_point1 = mid_point(controlPoint1, controlPoint2)
        mid_point2 = mid_point(controlPoint2, controlPoint3)
        mid_point3 = mid_point(mid_point1, mid_point2)

        current_iteration += 1
        populate_bezier_points(controlPoint1, mid_point1, mid_point3, current_iteration, iterations, bezier_points)
        bezier_points.append(mid_point3)
        populate_bezier_points(mid_point3, mid_point2, controlPoint3, current_iteration, iterations, bezier_points)

def create_bezier(controlPoint1: Point, controlPoint2: Point, controlPoint3: Point, iterations: int) -> List[Point]:
    bezier_points = []
    bezier_points.append(controlPoint1)
    populate_bezier_points(controlPoint1, controlPoint2, controlPoint3, 0, iterations, bezier_points)
    bezier_points.append(controlPoint3)

    return bezier_points
def visualize_curves_dnc(curve_points_list: List[List[Point]], main_points: List[Point], iterations_list: List[int]):
    """Visualize Bezier curves and main points with different iterations."""
    fig, ax = plt.subplots()

    # Set axis limits with a margin
    max_x = max(point.x for point in main_points)
    max_y = max(point.y for point in main_points)
    min_x = min(point.x for point in main_points)
    min_y = min(point.y for point in main_points)
    x_margin = (max_x - min_x) * 0.1
    y_margin = (max_y - min_y) * 0.1
    ax.set_xlim(min_x - x_margin, max_x + x_margin)
    ax.set_ylim(min_y - y_margin, max_y + y_margin)

    scatter_main_points = ax.scatter([], [], color='red', label='Main Points')
    lines_connect = []

    def init():
        """Initialize the plot."""
        scatter_main_points.set_offsets([(point.x, point.y) for point in main_points])
        for line in lines_connect:
            ax.add_line(line)
        return [scatter_main_points] + lines_connect

    def update(frame):
        """Update the plot for each frame."""
        for line in lines_connect:
            line.remove()
        lines_connect.clear()

        for i in range(len(main_points) - 1):
            line_connect = ax.plot([main_points[i].x, main_points[i + 1].x],
                                   [main_points[i].y, main_points[i + 1].y],
                                   color='purple', linestyle=':')[0]
            lines_connect.append(line_connect)

        curve_points = curve_points_list[frame]
        x_curve = [point.x for point in curve_points]
        y_curve = [point.y for point in curve_points]
        color = f'C{frame % 10}'  # Select a different color for each iteration
        ax.plot(x_curve, y_curve, color=color, label=f'Bezier Curve (Iterations: {iterations_list[frame]})')

        scatter_main_points.set_offsets([(point.x, point.y) for point in main_points])

        return [scatter_main_points] + lines_connect

    ani = FuncAnimation(fig, update, frames=len(curve_points_list), init_func=init,
                        blit=False, repeat=False, interval=500)

    plt.title('Bezier Curve Visualization with Different Iterations')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
    plt.legend()
    plt.show()

# Misalkan kita memiliki data seperti ini:
point1 = Point(0, 0)
point2 = Point(10, 10)
point3 = Point(20, 0)

# Definisikan iterasi yang berbeda
iterations_list = [1,2, 3]

# Inisialisasi list untuk menyimpan hasil kurva Bezier pada setiap iterasi
curve_points_list = []

# Generate kurva Bezier untuk setiap iterasi
for iterations in iterations_list:
    curve = create_bezier(point1, point2, point3, iterations)
    curve_points_list.append(curve)

# Titik-titik utama yang ingin kita visualisasikan
main_points = [point1, point2, point3]

# Visualisasikan kurva dan titik-titik utama dengan animasi
visualize_curves_dnc(curve_points_list, main_points, iterations_list)