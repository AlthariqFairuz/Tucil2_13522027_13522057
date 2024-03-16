import matplotlib.pyplot as plt
from models import Point

def bezier_curve(P0 : Point, P1 : Point, P2 : Point, t : int) -> Point:
    Q0 = Point((1-t)*P0.x + t*P1.x, (1-t)*P0.y + t*P1.y)
    Q1 = Point((1-t)*P1.x + t*P2.x, (1-t)*P1.y + t*P2.y)
    R0 = Point((1-t)*Q0.x + t*Q1.x, (1-t)*Q0.y + t*Q1.y)
    return R0

def brute_force_bezier(P0 : Point, P1 :Point, P2 : Point, iterations : int) -> list[Point]:
    curve = []
    for i in range(iterations+1):
        t = i / iterations
        point = bezier_curve(P0, P1, P2, t)
        curve.append(point)
    return curve

# Ini gw cuman coba ngetes aja, outputnya harusnya udah sama ama yg divide and conquer, ebdanya kalau brute force iterasinya harus banyak biar hasilnya bagus
# btw gw masih belum bisa gambar curve nya pake matplotlib :v
# P0 = Point(0, 0)
# P1 = Point(11.5, 8)
# P2 = Point(23, 0)
# iterations = 100  

# curve = brute_force_bezier(P0, P1, P2, iterations)

# x = [point.x for point in curve]
# y = [point.y for point in curve]


# plt.plot(x, y)
# plt.show()


