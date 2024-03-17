from models import Point
import threading

def mid_point(controlPoint1 : Point, controlPoint2 : Point) -> Point:
    mid = Point((controlPoint1.x + controlPoint2.x) / 2 , (controlPoint1.y + controlPoint2.y) / 2)
    return mid

def populate_bezier_points(controlPoint1 : Point, controlPoint2 : Point, controlPoint3 : Point, current_iteration : int, iterations : int, bezier_points : list[Point]) -> None:
    if current_iteration < iterations:
        mid_point1 = mid_point(controlPoint1, controlPoint2)
        mid_point2 = mid_point(controlPoint2, controlPoint3)
        mid_point3 = mid_point(mid_point1, mid_point2)

        current_iteration += 1
        populate_bezier_points(controlPoint1, mid_point1, mid_point3, current_iteration, iterations, bezier_points)
        bezier_points.append(mid_point3)
        populate_bezier_points(mid_point3, mid_point2, controlPoint3, current_iteration, iterations, bezier_points)

def create_bezier(controlPoint1 : Point, controlPoint2 : Point, controlPoint3 : Point, iterations : int) -> list[Point]:
    bezier_points = []
    bezier_points.append(controlPoint1)
    populate_bezier_points(controlPoint1, controlPoint2, controlPoint3, 0, iterations, bezier_points)
    bezier_points.append(controlPoint3)

    return bezier_points

def run_multithreaded(func, args_list):
    threads = []
    results = []

    def target_func(*args):
        result = func(*args)
        results.append(result)

    for args in args_list:
        thread = threading.Thread(target=target_func, args=args)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return results

# Stack Principle
# def mid_point(controlPoint1: Point, controlPoint2: Point) -> Point:
#     mid = Point((controlPoint1.x + controlPoint2.x) / 2, (controlPoint1.y + controlPoint2.y) / 2)
#     return mid

# def create_bezier(controlPoint1: Point, controlPoint2: Point, controlPoint3: Point, iterations: int) -> list[Point]:
#     bezier_points = []
#     stack = [(controlPoint1, controlPoint2, controlPoint3, 0, iterations)]
    
#     while stack:
#         control_point1, control_point2, control_point3, current_iteration, max_iterations = stack.pop()
        
#         if current_iteration < max_iterations:
#             mid_point1 = mid_point(control_point1, control_point2)
#             mid_point2 = mid_point(control_point2, control_point3)
#             mid_point3 = mid_point(mid_point1, mid_point2)

#             stack.append((mid_point3, mid_point2, control_point3, current_iteration + 1, max_iterations))
#             stack.append((control_point1, mid_point1, mid_point3, current_iteration + 1, max_iterations))
#         else:
#             bezier_points.append(control_point1)
    
#     bezier_points.append(controlPoint3)
#     return bezier_points
