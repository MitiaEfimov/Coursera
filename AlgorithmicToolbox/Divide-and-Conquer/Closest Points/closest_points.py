# python3
from collections import namedtuple
from itertools import combinations
from math import sqrt
from random import randint

Point = namedtuple('Point', 'x y')


def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


def minimum_distance_squared_naive(points):
    min_distance_squared = float("inf")

    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared,
                                   distance_squared(p, q))

    return min_distance_squared


def minimum_distance_squared(points, is_sorted=False):
    if not is_sorted:
        points.sort()
    if len(points) == 1:
        return float("inf")
    elif len(points) == 2:
        distance = distance_squared(points[0], points[1])
        return distance

    mid = len(points) // 2
    left_half_min = minimum_distance_squared(points[:mid], is_sorted=True)
    right_half_min = minimum_distance_squared(points[mid:], is_sorted=True)
    distance = min(right_half_min, left_half_min)

    if distance == 0:
        return distance

    zone = points[mid].x - sqrt(distance)
    left = mid
    for i in range(mid, -1, -1):
        if zone <= points[i].x <= points[mid].x:
            left = i
        else:
            break

    zone = points[mid].x + sqrt(distance)
    right = mid
    for i in range(mid, len(points)):
        if points[mid].x <= points[i].x <= zone:
            right = i
        else:
            break

    strip = points[left:right+1].copy()
    strip = sorted(points, key=lambda Point: Point.y )
    for i in range(len(strip)-1):
        for j in range(i+1, len(strip)):
            if abs(i-j) >= 7:
                break
            else:
                distance = min(distance, distance_squared(
                    strip[i],
                    strip[j]
                ))

    return distance


if __name__ == '__main__':
    # Input an integer N
    input_n = int(input())
    input_points = []
    # Outputs the smallest distance between a pair of two different points.
    for _ in range(input_n):
        # Input X and Y coordinate that defines point
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)
    print("{0:.9f}".format(sqrt(minimum_distance_squared(input_points))))
