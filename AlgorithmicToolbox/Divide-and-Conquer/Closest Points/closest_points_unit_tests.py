import unittest
from random import randint
from math import sqrt
from closest_points import minimum_distance_squared
from closest_points import minimum_distance_squared_naive
from ClosestPP import solution
from closest_points import Point


class ClosestPoints(unittest.TestCase):
    def test_small(self):
        for points in (
            [Point(1, 0), Point(1, 1)],
            [Point(2,3), Point(10,3), Point(3,3)]
        ):
            self.assertAlmostEqual(minimum_distance_squared(points),
                                   minimum_distance_squared_naive(points),
                                   delta=1e-03)

    def test_random(self):
        test = 0
        for _ in range(10):
            for n in [3, 10, 25, 50, 500]:
                for max_value in [10**9]:
                    points = []
                    for _ in range(n):
                        x = randint(-max_value, max_value)
                        y = randint(-max_value, max_value)
                        points.append(Point(x, y))
                    test += 1

                    if minimum_distance_squared(points) != minimum_distance_squared_naive(points):
                        print(f"case {test}:right {minimum_distance_squared_naive(points)} wrong {minimum_distance_squared(points)}")
                        print(points)
                        return
                    elif test % 1000 == 0:
                        print(f"{test} have done")

                    self.assertAlmostEqual(minimum_distance_squared(points),
                                           minimum_distance_squared_naive(points),
                                           delta=1e-03)

    def test_large(self):
        pass


if __name__ == '__main__':
    unittest.main()
