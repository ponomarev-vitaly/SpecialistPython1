# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

x1 = input("x1: ")
x2 = input("x2: ")
y1 = input("y1: ")
y2 = input("y2: ")
x3 = input("x3: ")
y3 = input("y3: ")


def distance(p1, p2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def distance(p1, p3):
    return ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5


def distance(p2, p3):
    return ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5


def min_distance():
    if distance(p1, p2) > distance(p1, p3) and distance(p2, p3) > distance(p1, p3):
        return distance(p1, p3)
    else:
        return distance(p1, p2)


res = min_distance()
