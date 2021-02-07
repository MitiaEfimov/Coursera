# python3

from itertools import product
from sys import stdin


def on_screen(my_list):
    print()
    for line in my_list:
        print(line)


def partition3(values, total=0, is_possible=False):
    assert 1 <= len(values) <= 20
    assert all(1 <= v <= 30 for v in values)

    if not is_possible:
        values = list(values)
        values.sort(reverse=True)
        for i in values:
            total += i
        if total % 3 == 0:
            total = total // 3
        else:
            return 0

    if values[0] > total:
        return 0
    souvenirs_partition = [[1]*(len(values)+1)]
    souvenirs_partition += [[0]*(len(values)+1)]

    for i in range(1, 2):
        souvenirs_partition[i][0] = 1
        part = 0
        for j in range(1, len(values)+1):
            if part + values[j-1] < total:
                part += values[j-1]
                souvenirs_partition[i][j] = souvenirs_partition[i-1][j]
            elif part + values[j-1] == total:
                souvenirs_partition[i][j] = souvenirs_partition[i-1][j]
                rest_values = []
                for value in range(1, len(values)+1):
                    if souvenirs_partition[i][value] == 0:
                        rest_values += [values[value-1]]
                if len(rest_values) == 0:
                    return 1
                else:
                    souvenirs_partition[i][j] = partition3(rest_values, total, True)
                if souvenirs_partition[i][j] == 1:
                    return 1
    else:
        return 0


if __name__ == '__main__':
    # The first line contains an integer 𝑛. 
    # The second line contains integers 𝑣1, 𝑣2, . . . , 𝑣𝑛 separated by spaces.
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    # Outputs 1, if it possible to partition 𝑣1, 𝑣2, ... , 𝑣𝑛 into three 
    # subsets with equal sums, and 0 otherwise.
    print(partition3(input_values))
