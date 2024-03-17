from models import Point

def bezier_curve(points: list[Point], t: float) -> Point:
    if len(points) == 2:
        return Point((1 - t) * points[0].x + t * points[1].x, (1 - t) * points[0].y + t * points[1].y)
    else:
        Q = [bezier_curve(points[i:i+2], t) for i in range(len(points) - 1)]
        return bezier_curve(Q, t)

def brute_force_bezier(P0: Point, P1: Point, P2: Point, iterations: int) -> list[Point]:
    real_curve = []
    curve_1 = []
    curve_2 = []
    for i in range(iterations + 1):
        t = i / iterations
        Q0, Q1, R0 = bezier_curve(P0, P1, P2, t)
        real_curve.append(R0)
        curve_1.append(Q0)
        curve_2.append(Q1)
    return real_curve, curve_1, curve_2