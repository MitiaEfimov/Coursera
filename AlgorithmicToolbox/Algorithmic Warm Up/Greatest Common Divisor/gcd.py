# python3


def gcd_naive(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    for divisor in range(min(a, b), 0, -1):
        if a % divisor == 0 and b % divisor == 0:
            return divisor

    assert False


def gcd(a, b):
    # Euclidean method
    assert 0 <= a <= 2 * 10 ** 9 and 0 <= b <= 2 * 10 ** 9

    while b != 0:
    	a, b = b, a % b
    return a

if __name__ == '__main__':
    # Input two integers a and b
    input_a, input_b = map(int, input().split())
    # Print a and b greatest common divisor
    print(gcd(input_a, input_b))
