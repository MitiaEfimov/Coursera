import unittest
from organizing_lottery import points_cover, points_cover_naive
from count_segments import fast_count_segments
from random import randint

class PointsAndSegments(unittest.TestCase):
    def test_small(self):
        for starts, ends, points in [
            ([0, 7], [5, 10], [1, 6, 11]),
            ([0, 5, 2, 3, 10], [3, 8, 6, 7, 11], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        ]:
            self.assertEqual(points_cover(list(starts), list(ends), list(points)),
                             points_cover_naive(starts, ends, points))

    def test_random(self):
        for i in [10]:
            for times in range(1000000):
                data = [randint(-i,i) for _ in range(i)]
                starts = [ s - randint(0, 10*i) for s in data]
                ends = [e + randint(0, 10*i) for e in data]
                points = [randint(-100*i, 100*i) for _ in range(i)]

                self.assertEqual(points_cover_naive(starts, ends, points),
                                 points_cover(starts, ends, points))

    def test_large(self):
        for i in [5000]:
                data = [randint(0, i) for _ in range(i)]
                starts = [s - randint(0, i // 2) for s in data]
                ends = [e + randint(0, i // 2) for e in data]
                points = [randint(-i, i) for _ in range(i)]
                self.assertEqual(points_cover(starts, ends, points),
                                 fast_count_segments(starts, ends, points))


if __name__ == '__main__':
    unittest.main()
