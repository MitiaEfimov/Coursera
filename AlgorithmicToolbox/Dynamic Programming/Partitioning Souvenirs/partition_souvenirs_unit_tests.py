import unittest
from partition_souvenirs import partition3


class PartitionSouvenirs(unittest.TestCase):
    def test(self):
        for values, answer in (
            ((20, ), 0),
            ((7, 7, 7), 1),
            ((3, 3, 3), 1),
            ((3, 3, 3, 3), 0),
            ((1, 3, 4, 5, 7, 20, 12, 3, 6, 8, 19, 26), 1)
        ):
            self.assertEqual(partition3(values), answer)


if __name__ == '__main__':
    unittest.main()
