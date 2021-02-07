# python3
"""Finding longest common subsiquence

Given two sequences we have to find length of longest common
subsequence.

"""


def lcs2(first_sequence, second_sequence):
    """Longest common subsequence

    Algorithm is simple:
    First we create a field N*M, where N - length of second sequence,
    M - first sequence.Every cell has zero value.

    Then just go throw all cells, and if second_sequence[j] == first_sequence[i] put
    (i-1,j-1) cell value and add 1 to cell (i,j), else put maximum
    of (i,j-1) and (i-1,j) cells.

    As result return (N,M) cell value.

    for example:

    1 2 3 and 2 3 4

      1 2 3        1 2 3
    2 0 0 0      2 0 1 1
    3 0 0 0  =>  3 0 1 2
    4 0 0 0      4 0 1 2

    Result = 2.

    """
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100

    subsequence_length = [[0]*(len(first_sequence)+1) for _ in range(len(second_sequence)+1)]
    for i in range(1, len(second_sequence)+1):
        for j in range(1, len(first_sequence)+1):
            if first_sequence[j-1] == second_sequence[i-1]:
                subsequence_length[i][j] = 1 + subsequence_length[i-1][j-1]
            else:
                subsequence_length[i][j] = max(
                    subsequence_length[i][j-1],
                    subsequence_length[i-1][j],
                )

    return subsequence_length[-1][-1]


if __name__ == '__main__':
    # Input an integer N
    n = int(input())
    # Input sequense of integers A1, A2, ..., An
    a = list(map(int, input().split()))
    assert len(a) == n

    # Input an integer M
    m = int(input())
    # Input sequens of integers B1, B2, ..., Bm
    b = list(map(int, input().split()))
    assert len(b) == m

    # Outputs lenth of A[] and B[] longest common subsequence
    print(lcs2(a, b))
