# python3

from collections import namedtuple
from sys import stdin

Segment = namedtuple('Segment', 'start end')


def compute_optimal_points(segments):
    point_set = []
    segments.sort()
    while len(segments) > 0:
        pointL = segments[0][0]
        pointR = segments[0][1]
        for i in range(len(segments)):
            if pointL <= segments[i][1] <= pointR:
                pointR = segments[i][1]
            if pointL <= segments[i][0] <= pointR:
                pointL = segments[i][0]
            else:
                segments = segments[i:]
                break
        else:
            segments = []
        if pointL == pointR:
            point_set.append(pointL)
        else:
            point_set.append(((pointL + pointR) // 2))
    return point_set

if __name__ == '__main__':
    # The first line of the input contains the number 𝑛 of segments. 
    # Each of the following 𝑛 lines contains two integers 
    # 𝑎𝑖 and 𝑏𝑖 (separated by a space) defining the coordinates of endpoints of the 𝑖-th segment.
    n, *data = map(int, stdin.read().split())
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    assert n == len(input_segments)
    output_points = compute_optimal_points(input_segments)
    # Outputs the minimum number 𝑚 of points.
    print(len(output_points))
    # Outputs the integer coordinates of 𝑚 points.
    print(*output_points)
