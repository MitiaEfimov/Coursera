# python3


def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1


def binary_search(keys, query):
    left = 0
    right = len(keys) - 1
    while left <= right:
        m = left + ((right - left) // 2)
        if keys[m] == query:
            return m
        elif keys[m] < query:
            left = m + 1
        else:
            right = m - 1
    return -1


if __name__ == '__main__':
    # Input integer N and sequence lenth N in increasing order
    input_keys = list(map(int, input().split()))[1:]
    # Input integer N and sequence length N of integers that would be found in keys input
    input_queries = list(map(int, input().split()))[1:]

    # For all querries prints an index of founded key or -1 if there is no such index
    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
