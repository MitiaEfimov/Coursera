# python3


def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def majority_element(elements):
    assert len(elements) <= 10 ** 5
    key_map = {}
    for i in elements:
        if i not in key_map.keys():
            key_map[i] = 0
        key_map[i] += 1
        if key_map[i] > len(elements)/2:
            return 1
    return 0


if __name__ == '__main__':
    # Input an integer N
    input_n = int(input())
    # Input sequence of N non-negative lenth N
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    # Prints 1 if the sequense contains an element that appears stricly more than N/2 times
    # Prints 0 if there is no such element
    print(majority_element(input_elements))
