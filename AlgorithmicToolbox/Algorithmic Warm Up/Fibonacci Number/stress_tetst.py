from fibonacci_number import fibonacci_number_naive as brutal
from fibonacci_number import fibonacci_number as fast

"""Simple stress test

Since the direct solution is right, it can be used
in a stress test for small fibonacci numbers.

"""


def stress_test():
    """Takes naive result and compare with fast solution """
    for number in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        if brutal(number) != fast(number):
            print(f"{number} Fibonacci wrong. {brutal(number)} != {fast(number)}")
        else:
            print(f"{number}: OK;", end=" ")


if __name__ == "__main__":
    stress_test()
