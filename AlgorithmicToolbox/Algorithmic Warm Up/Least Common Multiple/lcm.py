# python3


def lcm_naive(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    multiple = max(a, b)
    while multiple % a != 0 or multiple % b != 0:
        multiple += 1

    return multiple


def lcm(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    num = a * b
    while b != 0:
    	a, b = b, a % b
    num /= a
    return num


if __name__ == '__main__':
    # Input two integers a and b
    input_a, input_b = map(int, input().split())
    # Print a and b least common multiple
    print(lcm(input_a, input_b))
