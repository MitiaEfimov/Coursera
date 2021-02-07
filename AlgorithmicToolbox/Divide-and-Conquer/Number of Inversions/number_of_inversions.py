# python3

from itertools import combinations


def compute_inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions


def compute_inversions(a):
    if len(a) == 1:
        return a
    inversions = 0
    m = len(a) // 2
    left = compute_inversions(a[:m])
    if isinstance(left, tuple):
        inversions += left[1]
        left = left[0]
    right = compute_inversions(a[m:])
    if isinstance(right, tuple):
        inversions += right[1]
        right = right[0]
    a = []
    li, ri = 0, 0
    while len(left) > li and len(right) > ri:
        if left[li] <= right[ri]:
            a.append(left[li])
            li += 1
        else:
            a.append(right[ri])
            ri += 1
            inversions += len(left[li:])
    if len(left) > li:
        a = a + left[li:]
    elif len(right) > ri:
        a = a + right[ri:]
    return a, inversions


if __name__ == '__main__':
    # Input an integer N
    input_n = int(input())
    # Input sequence of integers lenth N
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    # Outputs the number of inversions needed to sort sequence
    print(compute_inversions_naive(elements))
