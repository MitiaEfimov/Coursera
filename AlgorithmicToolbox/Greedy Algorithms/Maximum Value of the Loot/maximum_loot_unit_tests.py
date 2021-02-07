import unittest
from maximum_loot import maximum_loot_value
from random import randint


class TestMaximumLoot(unittest.TestCase):
    def test(self):
            for (capacity, weights, prices, answer) in [
                (50, [20, 50, 30], [60, 100, 120], 180.0),
                (10, [30], [500], 500 / 3),
                (10, [5, 5, 4, 7], [10, 20, 20, 21], 43),
                (100, [21, 5, 17, 4, 13, 19, 2], [1241, 3554, 3523, 8964, 87456, 135, 120], 104993)
            ]:
                self.assertAlmostEqual(
                    maximum_loot_value(capacity, weights, prices),
                    answer,
                    delta=1e-03
                )


if __name__ == '__main__':
    unittest.main()
