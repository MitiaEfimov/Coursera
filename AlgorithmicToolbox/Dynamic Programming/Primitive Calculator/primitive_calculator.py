# python3
"""Minimum number of operations

 The main idea the same as dynamic money change.

 """


def compute_operations(n):
    """Dynamic algorithm

     To calculate minimum operations number for n using only operations
     add 1, multiply by 2 and multiply by 3, is needed to calculate
     minimum operations number for n-1, n//2 and n//3
     Since we are interested in smallest number, we take min of these three

    """
    assert 1 <= n <= 10 ** 6
    required_among_operations = [0, 1, 1, 1] + [0] * (n - 3)
    sequence = [1]
    if n == 1:
        return sequence
    elif 1 < n < 4:
        return sequence + [n]
    for i in range(4, n + 1):
        if i % 2 == 0 and i % 3 == 0:
            required_among_operations[i] = 1 + min(
                required_among_operations[i - 1],
                required_among_operations[i // 2],
                required_among_operations[i // 3],
            )
        elif i % 2 == 0:
            required_among_operations[i] = 1 + min(
                required_among_operations[i - 1],
                required_among_operations[i // 2],
            )
        elif i % 3 == 0:
            required_among_operations[i] = 1 + min(
                required_among_operations[i - 1],
                required_among_operations[i // 3],
            )
        else:
            required_among_operations[i] = 1 + required_among_operations[i - 1]

    sequence += [0]*(required_among_operations[-1])
    sequence[-1] = n
    for i in range(-2, -len(sequence), -1):
        i_minus_1 = required_among_operations[sequence[i+1]-1]
        i_divided_by_2 = required_among_operations[sequence[i + 1] // 2]
        i_divided_by_3 = required_among_operations[sequence[i + 1] // 3]
        if sequence[i + 1] % 3 == 0 and sequence[i + 1] % 2 == 0:
            if i_minus_1 <= i_divided_by_2 and \
                    i_minus_1 <= i_divided_by_3:
                sequence[i] = sequence[i+1] - 1
            elif i_divided_by_2 <= i_divided_by_3 and \
                    i_divided_by_2 <= i_minus_1:
                sequence[i] = sequence[i+1] // 2
            else:
                sequence[i] = sequence[i+1] // 3
        elif sequence[i + 1] % 2 == 0:
            if i_minus_1 <= i_divided_by_2:
                sequence[i] = sequence[i+1] - 1
            else:
                sequence[i] = sequence[i+1] // 2
        elif sequence[i + 1] % 3 == 0:
            if i_minus_1 <= i_divided_by_3:
                sequence[i] = sequence[i+1] - 1
            else:
                sequence[i] = sequence[i+1] // 3
        else:
            sequence[i] = sequence[i+1] - 1

    return sequence


if __name__ == '__main__':
    # Input an integer N
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    # Outputs minimum number of operation needed to get n from 1
    print(len(output_sequence) - 1)
    # Outputs a sequence of intermediate numbers.
    print(*output_sequence)
