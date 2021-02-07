# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    refills = 0
    current_position = 0
    while d > current_position + m:
        plan = current_position + m
        for i in range(len(stops)):
            if plan >= stops[i]:
                possible_position = stops[i]
                continue
            else:
                stops = stops[i:]
                break
        if possible_position == current_position:
            refills = -1
            break
        current_position = possible_position
        refills += 1
    return refills

if __name__ == '__main__':
    # Input an integer D - total distance
    input_d = int(input())
    # Input an integer M - distance that car can travel on full tank
    input_m = int(input())
    # Input an integer N
    input_n = int(input())
    # Input sequence of integers lenth N that defines stop distance 
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    # Outputs minimum numbers of refills needed if it possible to reach the distance
    # Outputs -1 if it is not possible
    print(compute_min_number_of_refills(input_d, input_m, input_stops))
