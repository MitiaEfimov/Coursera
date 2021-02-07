#python3
from _collections import deque


def max_sliding_window(sequence, size):
    if len(sequence) == 1:
        return [sequence[0]]
    elif size == 1:
        return sequence
    result = []
    _max_q = deque(maxlen=size)
    _window = deque(maxlen=size)
    _window.append(sequence[0])
    _max_q.append(sequence[0])
    for index, item in zip(range(1, len(sequence)), sequence[1:]):
        if index < size:
            _window.append(item)
            while _max_q and item > _max_q[-1]:
                _max_q.pop()
            else:
                _max_q.append(item)

        elif _window[0] == _max_q[0]:
            result.append(_max_q.popleft())
            _window.append(item)
            while _max_q and item > _max_q[-1]:
                _max_q.pop()
            else:
                _max_q.append(item)

        else:
            result.append(_max_q[0])
            _window.append(item)
            while _max_q and item > _max_q[-1]:
                _max_q.pop()
            else:
                _max_q.append(item)
    else:
        result.append(_max_q[0])

    return result


def main():
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())
    print(*max_sliding_window(input_sequence, window_size))


def test():
    user_size = 2
    user_sequence = [9, 9, 8, 7, 7]
    result = max_sliding_window(user_sequence, user_size)
    if __name__ == "__main__":
        print(user_sequence)
        print(*result)
    return result


if __name__ == '__main__':
    main()
