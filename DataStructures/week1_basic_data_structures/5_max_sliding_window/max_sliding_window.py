# python3


def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums


def naive_sliding(sequence, size):
    return max_sliding_window_naive(sequence, size)


def main():
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())
    print(*max_sliding_window_naive(input_sequence, window_size))


if __name__ == '__main__':
    main()


