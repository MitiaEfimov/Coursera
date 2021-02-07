# python3

from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def largest_number(numbers):
    numbers = [str(i) for i in numbers]
    numbers.sort(reverse=True)
    num = ""
    while len(numbers) != 1:
        for i in range(len(numbers)):
            for j in range(i,len(numbers)):
                if numbers[i][0] > numbers[j][0]:
                    num += numbers[i]
                    numbers.pop(i)
                    break
                elif int(numbers[i] + numbers[j]) >= int(numbers[j] + numbers[i]):
                    continue
                else:
                    numbers.insert(0,numbers.pop(j))
                    break
            else:
                num += numbers[i]
                numbers.pop(i)
                break
            break
    num += numbers[0]
    num = int(num)
    return num


if __name__ == '__main__':
    # Input an integer N
    n = int(input())
    # Input a sequence of integers lenth N
    input_numbers = input().split()
    assert len(input_numbers) == n
    # Output the largest number that can be composed out of 𝑎1, 𝑎2, . . . , 𝑎𝑛.
    print(largest_number(input_numbers))
