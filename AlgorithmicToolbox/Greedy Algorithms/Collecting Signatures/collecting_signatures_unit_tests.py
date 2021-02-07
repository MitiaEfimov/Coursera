import unittest
from collecting_signatures import compute_optimal_points, Segment


class CollectingSignatures(unittest.TestCase):
    def test(self):
        for (segments, answer) in [
            ([Segment(1, 3), Segment(2, 5), Segment(3, 6)], 1),
            ([Segment(4, 7), Segment(1, 3), Segment(2, 5), Segment(5, 6)], 2),
            ([Segment(2,5), Segment(1,10), Segment(3,10), Segment(1,3),
              Segment(4,8), Segment(6,8), Segment(2,9), Segment(1,2),
              Segment(3,4), Segment(9,10)], 4),
            ([Segment(1,60), Segment(18,80), Segment(48,90), Segment(49,51)], 1)
        ]:
            self.assertEqual(len(compute_optimal_points(segments)), answer)


if __name__ == '__main__':
    unittest.main()
