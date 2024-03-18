import matplotlib.pyplot as plt
import matplotlib.animation as animation
from models import Point

def mid_point(controlPoint1: Point, controlPoint2: Point) -> Point:
    mid = Point((controlPoint1.x + controlPoint2.x) / 2, (controlPoint1.y + controlPoint2.y) / 2)
    return mid

def populate_bezier_points(cp: list[Point], current_iteration: int, iterations: int, bezier_points: list[Point]) -> None:
    if current_iteration < iterations:
        left_cp = []
        right_cp = []
        mids = cp.copy()
        
        while len(mids) > 1:
            temp_mids = []
            left_cp.append(mids[0])
            right_cp.insert(0, mids[-1])  
            for i in range(len(mids) - 1):
                mid = mid_point(mids[i], mids[i + 1])
                temp_mids.append(mid)
                
            mids = temp_mids.copy()
            
        left_cp.append(mids[0])
        right_cp.insert(0, mids[0])
        
        populate_bezier_points(left_cp, current_iteration + 1, iterations, bezier_points)
        bezier_points.append(mids[0]) 
        populate_bezier_points(right_cp, current_iteration + 1, iterations, bezier_points)
            

def find_bezier_curve(cp:list[Point], iterations: int) -> list[Point]:
    if(len(cp) < 3):
        return cp
    bezier_points = []
    bezier_points.append(cp[0])
    populate_bezier_points(cp, 0, iterations, bezier_points)
    bezier_points.append(cp[-1])
    return bezier_points

def generate_bezier_dnc(control_points: list[Point], iterations: int) -> list[list[Point]]:
    """Generate Bezier curve points based on control points and iterations."""
    result = []

    for i in range(iterations):
        result.append(find_bezier_curve(control_points, i+1))

    return result


def visualize_curves_dnc(curve_points_list, main_points):
    """Visualize Bezier curves and main points."""
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

        for idx, curve_points in enumerate(curve_points_list[:frame+1]):
            x_curve = [point.x for point in curve_points]
            y_curve = [point.y for point in curve_points]
            ax.plot(x_curve, y_curve, color=f'C{idx}', label=f'Curve {idx+1}')

            for point in curve_points:
                ax.scatter(point.x, point.y, color=f'C{idx}', s=20)  # Adjust the size as needed

        scatter_main_points.set_offsets([(point.x, point.y) for point in main_points])

        return [scatter_main_points] + lines_connect

    ani = animation.FuncAnimation(fig, update, frames=len(curve_points_list), init_func=init,
                                  blit=False, repeat=False, interval=300)

    plt.title('Bezier Curve Visualization')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
    plt.legend()
    plt.show()

