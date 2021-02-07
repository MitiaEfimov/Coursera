# python3
from sys import stdin
from bisect import bisect_left, bisect_right


def points_cover_naive(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)

    for index, point in enumerate(points):
        for start, end in zip(starts, ends):
            if start <= point <= end:
                count[index] += 1

    return count


def points_cover(starts, ends, points):
    starts.sort()
    ends.sort()
    for i in range(len(points)):
        points[i] = (points[i], i)
    points.sort()
    covering = [0] * len(points)
    cover = 0
    li = 0
    ri = 0
    while li < len(starts) or ri < len(ends):
        if len(points) == 0:
            break
        index = 0
        for point, place in points:
            index += 1
            if li < len(starts) and starts[li] <= point:
                cover += 1
                li += 1
                break
            elif ri < len(ends) and ends[ri] < point:
                cover -= 1
                ri += 1
                break
            else:
                covering[place] += cover
                points = points[index:]
                break
    return covering


if __name__ == '__main__':
    # On first line input two non-negative integers S and P
    # defining the number if segments and number of points on a line
    # Next S lines contain two integers A and B
    # defining the i-th segment
    # Next line contain P integers X1, X2, ... Xp
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]
    output = points_cover(input_starts, input_ends, input_points)
    # Outputs P non-negative integers where an integer is the number of segments wich contain Xi
    print(*output)
