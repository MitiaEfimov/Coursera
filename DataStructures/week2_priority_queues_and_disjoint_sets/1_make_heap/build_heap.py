# python3


def build_heap(data):
    """
    Build a heap from ``data`` inplace by shifting n/2 elements. Shifting goes while an biggest elements would lie at the
    bottom of the heap.
    :param data: sequence of integers
    :return a sequence of swaps performed by the algorithm.
    """
    swaps = []
    last_index = len(data) - 1
    size = len(data)
    for i in range((last_index+1)//2, 0, -1):
        try:
            process_swaps = shift_down(array=data, size=size, parent_index=i-1)
            swaps += process_swaps
        except TypeError:
            continue
    return swaps


def find_child(parent_index, child_position: str = "left"):
    """
    Function that find current index of node i child
    :param parent_index: node index
    :param child_position: position of child (left or right), default = "left"
    :return: child index
    """
    parent_position = parent_index + 1
    if child_position == "left":
        return (2*parent_position) - 1
    else:
        return (2*parent_position + 1) - 1


def shift_down(array, size, parent_index):
    """
    Function that shift down an elements. It compares an parent element with his own children and if there is an element that
    is smaller then others, it comes up, when parent goes down. the process goes recursively until parent element would
    lie at the possible bottom position.
    In addiction the function collect all the swaps and return swaps tuple list.
    :param array: a sequence, need to be mutate
    :param size: array size where mutate goes
    :param parent_index: index of parent node
    :return: list of swapped elements indexes [(i, j), (n, m),... ]
    """
    min_index = parent_index
    left_child_index = find_child(min_index, "left")
    right_child_index = find_child(min_index, "right")
    if left_child_index <= size-1 and array[left_child_index] < array[min_index]:
        min_index = left_child_index
    if right_child_index <= size-1 and array[right_child_index] < array[min_index]:
        min_index = right_child_index
    if parent_index != min_index:
        array[parent_index], array[min_index] = array[min_index], array[parent_index]
        swaps = [(parent_index, min_index)]
        try:
            swaps += shift_down(array, size, min_index)
            return swaps
        except TypeError:
            return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)
    print(data)


if __name__ == "__main__":
    main()
