# python3
from time import sleep

def last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    fibonacci_numbers = [0] * (to_index + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, to_index + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]
        
    return sum(fibonacci_numbers[from_index:to_index + 1]) % 10


def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18
    
    if to_index <= 2:
        return to_index

    current = 1
    previous = 0
    total = 1
    previous_index = 0
    total_list = []
    fib_list = [0,1]

    for i in range(to_index+1):
    	print(i)

    	if i < from_index:
    		print(previous_index, i)
	    	previous_index += 1
	    	total = 0
    	elif i == to_index:
    		print(f"total = {total} + {previous} ")
	    	total += previous
	    	print(f"step{i}total={total}")
	    	total_list.append(total)
	    	break
    	elif i == from_index or from_index == 0:
    		print(f"total = {total} + {previous} + {current}")
	    	total = (total + previous + current) % 10
	    	print(f"step{i}total={total}")
	    	total_list.append(total)
    	else:
    		print(f"total = {total} + {current}")
	    	total = (total + current) % 10
	    	print(f"step{i}total={total}")
	    	total_list.append(total)

    	previous , current = current, (current+previous)%10
    	fib_list.append(current)
    	print(total_list)
    	print(fib_list)

    return total


if __name__ == '__main__':
    # Input two non-negative integers M an N separated by a space
    input_from, input_to = map(int, input().split())
    # Prints the last digit of the sum Fm + Fm+1 + ... + Fn
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))