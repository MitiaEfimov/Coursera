import unittest
from random import randint
from random import seed

from .max_sliding import max_sliding_window as fast
from .max_sliding_window import max_sliding_window_naive as slow


class SlidingTest(unittest.TestCase):

    def test_random_brute(self):

        for i in range(25*(10**5)):
            sequence, size = forming_data(max_size=500, max_int=10**5)
            naive = slow(sequence, size)
            imp = fast(sequence, size)
            if naive == imp and i % (15*(10**2)) == 0 and len(sequence) < 100:
                print("="*72)
                print("TEST {}: ok".format(i))
                print("size = ", size)
                print("sequence:", sequence)
                print("="*72)
            elif naive == imp and i % (15*(10**2)) == 0:
                print("="*72)
                print("TEST {}: ok".format(i))
                print("size = ", size)
                print("sequence: [ ... ]")
                print("="*72)
            elif naive != imp:
                print("no")
                print("sequence:", sequence)
                print("size = ", size)
                print(f"right:{naive}\n"
                      f"wrong:{imp}")
            self.assertEqual(naive, imp, msg="\n"+"="*70+f"\nright:{naive}\nwrong:{imp}\n\n{size}\n{sequence}\n"+"="*70)


def forming_data(max_size: int = 5, max_int: int = 10):
    seed(randint(1, 100000000000))
    sequence_size = randint(1, max_size)
    window_size = randint(1, sequence_size)
    sequence = [randint(0, max_int) for _ in range(sequence_size)]
    return sequence, window_size

