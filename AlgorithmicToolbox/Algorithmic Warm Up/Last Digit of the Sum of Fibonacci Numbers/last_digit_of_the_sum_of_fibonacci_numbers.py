# python3


def last_digit_of_the_sum_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers) % 10


def last_digit_of_the_sum_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    previous = 0
    current = 1
    total_list = [0,1]
    total = 1

    while total_list[-(len(total_list)/2):] != [0,1] or len(total_list) < 3 : 
        total = (total +previous+ current)%10
        total_list.append(total)
        previous, current = current, (previous + current) % 10

    total_list = total_list[:-2]
    n %= len(total_list)
    total = total_list[n]

    return total


if __name__ == '__main__':
    # Input an integer N
    input_n = int(input())
    # Print the last digit of the sum F0 + F1 + ... + Fn
    print(last_digit_of_the_sum_of_fibonacci_numbers(input_n))

