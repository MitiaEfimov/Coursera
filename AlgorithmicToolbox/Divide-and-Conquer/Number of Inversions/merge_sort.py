def MergeSort(a):
    if len(a) == 1:
        return a
    inversions = 0
    m = len(a) // 2
    left = MergeSort(a[:m])
    if type(left) == type(("type", "tuple")):
        inversions += left[1]
        left = left[0]
    right = MergeSort(a[m:])
    if type(right) == type(("type", "tuple")):
        inversions += right[1]
        right = right[0]
    a = []
    li, ri = 0, 0
    while len(left) > li and len(right) > ri:
        if left[li] <= right[ri]:
            a.append(left[li])
            li += 1
        else:
            a.append(right[ri])
            ri += 1
            inversions += 1
    if len(left) > li:
        # inversions += len(left[li:])
        a = a + left[li:]
    elif len(right) > ri:
        inversions += len(right[li:])
        a = a + right[ri:]
    return a, inversions
