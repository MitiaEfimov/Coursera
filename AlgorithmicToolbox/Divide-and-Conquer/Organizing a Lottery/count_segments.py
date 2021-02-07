# Uses python3
import collections
import sys


def fast_count_segments(starts, ends, points):
    """Fast algorithm for counting segments problem.
    The idea is to set labels for each of the arrays, sort them and apply
    counting of coverage technique.
    Samples:
    >>> fast_count_segments([0, 7], [5, 10], [1, 6, 11])
    [1, 0, 0]
    >>> fast_count_segments([-10], [10], [-100, 100, 0])
    [0, 0, 1]
    >>> fast_count_segments([0, -3, 7], [5, 2, 10], [1, 6])
    [2, 0]
    >>> fast_count_segments([0, 2, 4], [5, 2, 10], [1, 6, 2, 2])
    [1, 1, 2, 2]
    """
    left_label, point_label, right_label = (1, 2, 3)
    count = [0] * len(points)

    # Regular dict object cannot be used here, because points are not unique.
    points_map = collections.defaultdict(set)

    pairs = []
    for i in starts:
        pairs.append((i, left_label))
    for i in ends:
        pairs.append((i, right_label))
    for i in range(len(points)):
        point = points[i]
        pairs.append((point, point_label))
        points_map[point].add(i)

    sorted_pairs = sorted(pairs, key=lambda p: (p[0], p[1]))

    coverage = 0
    for pair in sorted_pairs:
        if pair[1] == left_label:
            coverage += 1
        if pair[1] == right_label:
            coverage -= 1
        if pair[1] == point_label:
            indices = points_map[pair[0]]
            for i in indices:
                count[i] = coverage

    return count


list1 = [5, 19, 16, 16, 8, 10, 10, 6]
list2 = [28, 26, 26, 23, 20, 11, 15, 8]
points_list = [1, 8, 15, 17, 19, 23, 29, 36, 43, 50]
res = fast_count_segments(list1, list2, points_list)
print(res)
