list1 = [5, 19, 16, 16, 8, 10, 10, 6]
list2 = [28, 26, 26, 23, 20, 11, 15, 8]
points = [1, 8, 15, 17, 19, 23, 29, 36, 43, 50]


def binary(points, point):
    left = 0
    right = len(points)-1
    potential = len(points)-1
    while left <= right:
        m = left + ((right - left) // 2)
        if points[m] == point:
            return m
        elif points[m] < point:
            left = m + 1
        else:
            potential = m
            right = m - 1
    return potential


def placing(array, left, right):
    ml, mr = left, left
    for i in range(left + 1, right + 1):
        if array[0][i] == array[0][left]:
            mr += 1
            for a in array:
                a[i], a[mr] = a[mr], a[i]
        elif array[0][i] < array[0][left] and ml != mr:
            ml += 1
            mr += 1
            for a in array:
                a[i], a[mr] = a[mr], a[i]
                a[ml], a[mr] = a[mr], a[ml]
        elif array[0][i] < array[0][left]:
            ml += 1
            mr += 1
            for a in array:
                a[i], a[mr] = a[mr], a[i]
    else:
        for a in array:
            a[left], a[ml] = a[ml], a[left]
    return ml, mr


def my_quick_sort(array: "tuple", left=None, right=None, Rank=False):
    if len(array) != 1:
        for i in range(1, len(array)):
            if len(array[i - 1]) != len(array[i]):
                print(f"length of array{i - 1} not equal length of array{i}")
                return exit(0)
            if not isinstance(array[i-1], list) or not isinstance(array[i], list):
                print(f"type of array{i - 1} not equal to type of array{i}")
                return exit(0)
    if left is None and right is None:
        left, right = 0, len(array[0]) - 1
    if left >= right:
        return
    k = left + ((right - left) // 2)
    for current_array in array:
        current_array[left], current_array[k] = current_array[k], current_array[left]
    equal = placing(array, left, right)
    if len(array) != 1:
        my_quick_sort(array[1:], equal[0], equal[1])
    my_quick_sort(array, left, equal[0] - 1)
    my_quick_sort(array, equal[1] + 1, right)
    return


def points_cover(_1starts, _2ends, points):
    my_quick_sort((_1starts,))
    my_quick_sort((_2ends,))
    my_quick_sort((points,))
    covering = []
    cover = 0
    li = 0
    ri = 0
    while li < len(_1starts) or ri < len(_2ends):
        if len(points) == 0:
            break
        index = 0
        for point in points:
            index += 1
            if li < len(_1starts) and _1starts[li] <= point:
                cover += 1
                li += 1
                break
            elif ri < len(_2ends) and _2ends[ri] < point:
                cover -= 1
                ri += 1
                break
            else:
                covering += [cover]
                points = points[index:]
                break
    if len(points[point:]) > 0:
        covering += [0] * len(points[point:])
    return covering

"""
result = points_cover(list1, list2, points)
print(result)

my_quick_sort((points,))
my_quick_sort((list1, list2))
list3 = [(5,6), (6,8), (8,10), (10,11), (11, 15), (15,16), (16,19), (19,20), (20,23),(23,26),(26,28)]
list4 = list(zip(list1, list2))
m = binary(list1, 28)
print(m)
"""

starts = [-4, -2, -1, 1, 2, 2, 4, 5, 5, 9]
ends = [2, 4, 4, 5, 5, 6, 7, 7, 7, 13]
points = [-5, -3, 2, 3, 6, 9]
REFER = [0, 1, 6, 5, 4, 1]
result = points_cover(starts,ends,points)
print(result)
