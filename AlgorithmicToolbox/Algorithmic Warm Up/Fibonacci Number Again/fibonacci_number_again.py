# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


def fibonacci_number_again(n, m):
    # Uses M'th pisano period
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        Pisano = list(range(n))
    else:
        Pisano = [0,1]
        previous = 0
        current = 1
        for i in range(n-1):
            previous, current = current, (previous + current) % m
            Pisano.append(current)
            if Pisano[-2:]== [0,1]:
                Pisano = Pisano[:-2]
                break

    n = n % len(Pisano)
    digit = Pisano[n]

    return digit


if __name__ == '__main__':
    # Input two integers N and M
    input_n, input_m = map(int, input().split())
    # print N'th Fibbonaci number mod M
    print(fibonacci_number_again(input_n, input_m))
