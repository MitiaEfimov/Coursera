# python3
"""Fibonacci number

There is two solution for calculating last digit of 'n' fibonacci number.

"""


def last_digit_of_fibonacci_number_naive(n):
    """Naive solution for calculating Fibonacci number

        This solution recursively calculate Fibonacci numbers modulo 10.
        Problem in this solution is that it computes the same
        thing again many times.

        """
    assert 0 <= n <= 10 ** 7

    if n <= 1:
        return n

    return (last_digit_of_fibonacci_number_naive(n - 1) + last_digit_of_fibonacci_number_naive(n - 2)) % 10


def last_digit_of_fibonacci_number(n):
    """Fast solutions for calculating Fibonacci numbers

       This solution calculates the Fibonacci numbers modulo 10 one after the other in
       the cycle, using the two previous numbers that are calculated in the same cycle.

        """
    assert 0 <= n <= 10 ** 7

    if n <= 1:
        return n

    previous = 0
    current = 1
    for i in range(n - 1):
        previous, current = current, (previous + current) % 10
    return current


if __name__ == '__main__':
    # Input integer N
    input_n = int(input())
    # Print the last digit of N'th Fibonacci number
    print(last_digit_of_fibonacci_number(input_n))
