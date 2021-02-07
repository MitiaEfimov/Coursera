# python3

from random import randint


def partition3(array, left, right):
    ml, mr = left, left
    for i in range(left+1, right+1):
        if array[i] == array[left]:
            mr += 1
            array[mr], array[i] = array[i], array[mr]
        elif array[i] < array[left] and ml != mr:
            ml += 1
            mr += 1
            array[mr], array[i] = array[i], array[mr]
            array[ml], array[mr] = array[mr], array[ml]
        elif array[i] < array[left]:
            ml += 1
            mr += 1
            array[mr], array[i] = array[i], array[mr]
    else:
        array[left], array[ml] = array[ml], array[left]
    return (ml, mr)


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    zone = partition3(array, left, right)
    randomized_quick_sort(array, left, zone[0]-1)
    randomized_quick_sort(array, zone[1]+1, right)
    return


if __name__ == '__main__':
    # Input an integer N
    input_n = int(input())
    # Input sequence lenth N
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    # does quik sort by replacing elements in 3-way partition
    randomized_quick_sort(elements, 0, len(elements) - 1)
    # Outputs sequence in non-decreacing order
    print(*elements)
