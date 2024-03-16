import matplotlib.pyplot as plt
from models import Point

def mid_point(controlPoint1 : Point, controlPoint2 : Point) -> Point:
    mid = Point((controlPoint1.x + controlPoint2.x) / 2 , (controlPoint1.y + controlPoint2.y) / 2)
    return mid;

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

# P0 = Point(0,0)
# P1 = Point(11.5,8)
# P2 = Point(23,0)

# iterations = 5  

# curve = create_bezier(P0, P1, P2, iterations)

# for (point) in curve:
#     print(point.x, point.y)

# # Uraikan hasil bezier curve ke dalam x dan y
# x = [point.x for point in curve]
# y = [point.y for point in curve]


# plt.plot(x, y)
# plt.show()
