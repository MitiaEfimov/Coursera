# python3


def lcs3(first_sequence, second_sequence, third_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100
    assert len(third_sequence) <= 100

    subsequence_length = [[[0] * (len(first_sequence) + 1) for _ in range(len(second_sequence) + 1)]
                          for _ in range(len(third_sequence) + 1)]

    for z in range(1, len(third_sequence) + 1):
        for i in range(1, len(second_sequence) + 1):
            for j in range(1, len(first_sequence) + 1):
                if first_sequence[j - 1] == second_sequence[i - 1] and \
                        first_sequence[j - 1] == third_sequence[z - 1]:
                    subsequence_length[z][i][j] = 1 + (subsequence_length[z - 1][i - 1][j - 1])
                else:
                    subsequence_length[z][i][j] = max(
                        subsequence_length[z][i][j-1],
                        subsequence_length[z][i-1][j],
                        subsequence_length[z-1][i][j],
                    )

    return subsequence_length[-1][-1][-1]


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

    # Input an integer Q
    q = int(input())
    # Input sequens of integers C1, C2, ..., Cq
    c = list(map(int, input().split()))
    assert len(c) == q

    # Outputs lenth of A[], B[] and C[] longest common subsequence
    print(lcs3(a, b, c))
