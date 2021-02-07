# python3

from itertools import permutations


def max_dot_product_naive(first_sequence, second_sequence):
    assert len(first_sequence) == len(second_sequence)
    assert len(first_sequence) <= 10 ** 3
    assert all(0 <= f <= 10 ** 5 for f in first_sequence)
    assert all(0 <= s <= 10 ** 5 for s in second_sequence)

    max_product = 0
    for permutation in permutations(second_sequence):
        dot_product = sum(first_sequence[i] * permutation[i] for i in range(len(first_sequence)))
        max_product = max(max_product, dot_product)

    return max_product


def max_dot_product(first_sequence, second_sequence):
    assert len(first_sequence) == len(second_sequence)
    assert len(first_sequence) <= 10 ** 3
    assert all(0 <= f <= 10 ** 5 for f in first_sequence)
    assert all(0 <= s <= 10 ** 5 for s in second_sequence)

    first_sequence.sort()
    second_sequence.sort()
    max_product = sum(first_sequence[i]*second_sequence[i] for i in range(len(first_sequence)))
    return max_product


if __name__ == '__main__':
    # Input an integer N
    n = int(input())
    # Input a sequence of integers lenth N: A[]
    prices = list(map(int, input().split()))
    # Input a sequence of integers lenth N: B[]
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    # Outputs the maximum value of N-elements sum where
    # i-th element = Ai * Ci.  C[] is permutation of B[]
    print(max_dot_product(prices, clicks))
