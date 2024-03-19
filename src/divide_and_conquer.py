import matplotlib.pyplot as plt
import matplotlib.animation as animation
from models import Point
import timeit

class DNCBezier:
    def __init__(self, points:list[Point], iterations:int):
        self.curve_points = []
        self.points = points
        self.iterations = iterations

    def midpoint(self, point1: Point, point2: Point) -> Point:
        """Calculate the midpoint between two points."""
        return Point((point1.x + point2.x) / 2, (point1.y + point2.y) / 2)

    def populate_bezier_points(self, cp: list[Point],iterations ,current_iteration: int, bezier_points: list[Point]) -> None:
        """Populate Bezier points based on control points and current iteration."""
        if current_iteration < iterations:
            left_cp = []
            right_cp = []
            mids = cp.copy()

            # Calculate midpoints until there is only one midpoint left
            while len(mids) > 1:
                # Append new control point on left and right bezier latest points
                left_cp.append(mids[0])
                right_cp.insert(0, mids[-1])
                
                # Calculate midpoints for each pair of control points
                mids = [self.midpoint(mids[i], mids[i + 1]) for i in range(len(mids) - 1)]

            left_cp.append(mids[0])
            right_cp.insert(0, mids[0])
            
            # Recursively populate bezier points for left and right control points
            self.populate_bezier_points(left_cp,iterations, current_iteration + 1, bezier_points)
            bezier_points.extend(mids)
            self.populate_bezier_points(right_cp, iterations,current_iteration + 1, bezier_points)

    # Calculate Bezier points based on control points and iterations
    def calculate_dnc_bezier_points(self, iterations) -> list[Point]:
        # If there are less than 3 control points, return the control points
        if len(self.points) < 3:
            return self.points

        # Initialize the list of bezier points with the first control point
        bezier_points = [self.points[0]]
        self.populate_bezier_points(self.points,iterations, 0, bezier_points)
        bezier_points.append(self.points[-1])
        self.curve_points = bezier_points
        
        return bezier_points

    def generate_bezier_dnc(self, control_points: list[Point], iterations: int) -> list[list[Point]]:
        """Generate Bezier curve points based on control points and iterations."""
        result = []

        for i in range(iterations):
            result.append(self.calculate_dnc_bezier_points(i+1))

        return result

    def visualize_curves_dnc(self):
        """Visualize Bezier curves and main points."""
        curve_points_list = self.generate_bezier_dnc(self.points, self.iterations)
        main_points = self.points

        fig, ax = plt.subplots()

        # Set axis limits with a margin
        max_x = max(point.x for point in main_points)
        max_y = max(point.y for point in main_points)
        min_x = min(point.x for point in main_points)
        min_y = min(point.y for point in main_points)
        x_margin = (max_x - min_x) * 0.2  
        y_margin = (max_y - min_y) * 0.2 
        ax.set_xlim(min_x - x_margin, max_x + x_margin)
        ax.set_ylim(min_y - y_margin, max_y + y_margin+2)

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
                    ax.scatter(point.x, point.y, color=f'C{idx}', s=20) 

            scatter_main_points.set_offsets([(point.x, point.y) for point in main_points])

            return [scatter_main_points] + lines_connect

        ani = animation.FuncAnimation(fig, update, frames=len(curve_points_list), init_func=init,
                                      blit=False, repeat=False, interval=300)
        
        execution_time = timeit.timeit(lambda: self.calculate_dnc_bezier_points(self.iterations), number=1) * 1000  # dalam milidetik

        info_text = f'Number of Points: {len(self.curve_points)}\nExecution Time: {round(execution_time, 3)} milliseconds'
        print(info_text)
        for i, cv in enumerate(self.curve_points):
            print(f'Curve point {i+1}: {cv.x}, {cv.y}')
        ax.text(0.5, 0.9, info_text, transform=ax.transAxes, fontsize=10, verticalalignment='top', ha='center', bbox=dict(facecolor='white', alpha=0.5, pad=10))

        # Mengatur warna latar belakang menjadi putih dan menonaktifkan grid
        ax.set_facecolor('white')
        ax.grid(False)

        plt.title('Bezier Curve DNC Visualization')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        # plt.legend()
        plt.show()