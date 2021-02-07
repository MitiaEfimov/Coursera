# python3
"""Fibonacci number

There is two solution for calculating 'n' fibonacci number.

"""


def fibonacci_number_naive(n):
    """Naive solution for calculating Fibonacci number

    This solution recursively calculate Fibonacci numbers.
    Problem in this solution is that it computes the same
    thing again many times.

    """
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    """Fast solutions for calculating Fibonacci numbers

   This solution calculates the Fibonacci numbers one after the other in
   the cycle, using the two previous numbers that are calculated in the same cycle.

    """
    assert 0 <= n <= 45
    fibonacci_integer_previous = 0
    fibonacci_integer_current = 1
    if n == 0:
        return fibonacci_integer_previous
    elif n == 1:
        return fibonacci_integer_current
    else:
        for i in range(n - 1):
            FibInt = fibonacci_integer_current + fibonacci_integer_previous
            fibonacci_integer_previous, fibonacci_integer_current = (
                fibonacci_integer_current, FibInt)
        return FibInt


if __name__ == '__main__':
    # Input an integer N
    input_n = int(input())
    # Print the N'th Fibonacci number Fn
    print(fibonacci_number(input_n))
