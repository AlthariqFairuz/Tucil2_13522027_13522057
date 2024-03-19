import matplotlib.pyplot as plt
import matplotlib.animation as animation
from models import Point
import timeit

class BruteForceBezier:
    def __init__(self, points:list[Point], iterations:int) -> None:
        self.curve_points =[]
        self.points = points
        self.iterations = iterations

    def calculate_pascal_triangle_row(self,row_number: int) -> list[int]:
        """Calculate a row in Pascal's Triangle based on the given row number."""
        if row_number == 0:
            return [1]

        row = [1]
        for i in range(1, row_number + 1):
            # Initialize a new row with 1s and update the middle elements
            new_row = [1] * (i + 1)
            for j in range(1, i):
                new_row[j] = row[j - 1] + row[j]
            row = new_row

        return row

    def create_bezier_curve(self) -> None:
        """Approximate the Bezier curve by brute-force iteration."""
        curve = []
        n = len(self.points) - 1
        coefficients = self.calculate_pascal_triangle_row(n)
        for i in range(self.iterations + 1):
            t = i / self.iterations
            x = y = 0
            # Build the curve point by iterating through the control points
            for j in range(n + 1):
                coefficient = coefficients[j] * (1 - t) ** (n - j) * t ** j
                x += coefficient * self.points[j].x
                y += coefficient * self.points[j].y
            curve.append(Point(x, y))
        self.curve_points = curve
    
    def visualize_curves(self):
        """Visualize the Bezier curve and main points using matplotlib."""
        fig, ax = plt.subplots()

        # Set plot limits based on the points
        max_x = max(point.x for point in self.points)
        max_y = max(point.y for point in self.points)
        min_x = min(point.x for point in self.points)
        min_y = min(point.y for point in self.points)
        x_margin = (max_x - min_x) * 0.2  
        y_margin = (max_y - min_y) * 0.2 
        ax.set_xlim(min_x - x_margin, max_x + x_margin)
        ax.set_ylim(min_y - y_margin, max_y + y_margin+2)

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

            for i in range(len(self.points) - 1):
                line_connect = ax.plot([self.points[i].x, self.points[i+1].x],
                                       [self.points[i].y, self.points[i+1].y],
                                       color='purple', linestyle=':')[0]
                lines_connect.append(line_connect)

            return lines + [scatter_main_points, scatter_curve_points] + lines_connect

        def update(frame):
            # Update curve and point positions for animation
            x_curve = [point.x for point in self.curve_points[:frame + 1]]
            y_curve = [point.y for point in self.curve_points[:frame + 1]]
            line_curve.set_data(x_curve, y_curve)
            scatter_curve_points.set_offsets([(x, y) for x, y in zip(x_curve, y_curve)])

            x_main = [point.x for point in self.points]
            y_main = [point.y for point in self.points]
            scatter_main_points.set_offsets([(x, y) for x, y in zip(x_main, y_main)])

            return lines + [scatter_main_points, scatter_curve_points] + lines_connect

        # Create the animation
        ani = animation.FuncAnimation(fig, update, frames=len(self.curve_points), init_func=init, blit=False, repeat=False)

        execution_time = timeit.timeit(lambda: self.create_bezier_curve(), number=1) * 1000  # dalam milidetik

        info_text = f'Number of Points: {len(self.curve_points)}\nExecution Time: {round(execution_time, 3)} milliseconds'
        print(info_text)
        for i, cv in enumerate(self.curve_points):
            print(f'Curve point {i+1}: {cv.x}, {cv.y}')
        ax.text(0.5, 0.9, info_text, transform=ax.transAxes, fontsize=10, verticalalignment='top', ha='center', bbox=dict(facecolor='white', alpha=0.5, pad=10))

        # Mengatur warna latar belakang menjadi putih dan menonaktifkan grid
        ax.set_facecolor('white')
        ax.grid(False)
        
        # Plot labels and legend
        plt.title('Bezier Curve Bruteforce Visualization')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.grid(False)
        # plt.legend()
        plt.show()
