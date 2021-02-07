# python3

import sys
from random import randint
from time import sleep


### 1 abcaacababbcabbcbcaccbbbaaaccc abc

def hash_func(string, multiplier: int, prime: int):
	if prime == 1:
		prime = 10**9 + 7
	elif prime == 2:
		prime = 10**9 + 9

	ans = 0
	for c in string[::-1]:
		ans = (ans * multiplier + ord(c)) % prime
	return ans


def precompute_hashes(text: str, len_pattern: int, multiplier: int, prime: int):
	if prime == 1:
		prime = 10**9 + 7
	elif prime == 2:
		prime = 10**9 + 9
	
	hashes = [0] * (len(text) - len_pattern + 1)
	last_sub_str = str(text[len(text)-len_pattern:])
	hashes[len(text)-len_pattern] = hash_func(last_sub_str, multiplier, prime)
	y = 1
	for i in range(1, len_pattern+1):
		y = (y * multiplier) % prime
	for i in range(len(text)-len_pattern-1, -1, -1):
		hashes[i] = int(((multiplier * hashes[i + 1]) + ord(text[i]) - (y * ord(text[i + len_pattern]))) % prime)
	return hashes


def precompute_hash_table(text, prime, multiplier, max_len=0):
	if prime == 1:
		prime = 10**9 + 7
	elif prime == 2:
		prime = 10**9 + 9
	if not max_len:
		max_len = len(text)
	h_table = dict()
	h_table["multiplier"] = multiplier
	h_table["text"] = text
	for length in range(0, max_len):
		h_table[length] = precompute_hashes(text, length+1, multiplier, prime)
	return h_table


def solve(allowed_distance, text, pattern):
	x = randint(10*5, 10**6)
	pattern_hash_table = precompute_hash_table(text=pattern, prime=1, multiplier=x, max_len=len(pattern))
	text_hash_table = precompute_hash_table(text=text, prime=1, multiplier=x, max_len=len(pattern))
	positions = dict()
	loop = len(text) - len(pattern)
	for i in range(len(text)-len(pattern)+1):
		start, end = i, i+len(pattern)
		for distance in range(allowed_distance+1):
			next_mismatch = find_next_mismatch(pattern[start-i:],
										  text[start:end],
										  pattern_hash_table,
										  text_hash_table,
										  pattern_index=start-i,
										  text_index=start)

			if next_mismatch+start-i == len(pattern):
				positions[i] = True
				break
			else:	
				start += next_mismatch+1



	return list(positions.keys())

def find_next_mismatch(pattern, text, pattern_hash_table, text_hash_table, pattern_index, text_index):
	left, right = 0, len(pattern)-1
	position = 0
	while left <= right:
		lenght = (left+right) // 2
		equal = do_compare(pattern_hash_table, text_hash_table, lenght, pattern_index, text_index)
		if equal:
			left = lenght+1
			position = left
		else:
			right = lenght-1
	return position


def do_compare(hash_table_1, hash_table_2, lenght, pattern_index, text_index):
	if hash_table_1["multiplier"] != hash_table_2["multiplier"]:
		return exit(0)
	else:
		multiplier = hash_table_2["multiplier"]
	hash_line_1, text_1 = hash_table_1[lenght], hash_table_1["text"][pattern_index:pattern_index+lenght+1]
	hash_line_2, text_2 = hash_table_2[lenght], hash_table_2["text"][text_index:text_index+lenght+1]

	if hash_line_1[pattern_index] == hash_line_2[text_index]:
		ind_1 = hash_func(text_1, multiplier, prime=2)
		ind_2 = hash_func(text_2, multiplier, prime=2)
		if ind_1 == ind_2:
			return True, lenght
	return False
	
"""
if __name__ == "__main__":
	k, t, p = 1, "abcaacababbcabbcbcaccbbbaaaccc", "abc"
	ans = solve(int(k), t, p)
	print(len(ans), *ans) 
	k, t, p = 0, "ababab", "baaa"
	ans = solve(int(k), t, p)
	print(len(ans), *ans)	
	k, t, p = 1, "ababab", "baaa"
	ans = solve(int(k), t, p)
	print(len(ans), *ans)
	k, t, p = 1, "xabcabc", "ccc"
	ans = solve(int(k), t, p)
	print(len(ans), *ans)
	k, t, p = 2, "xabcabc", "ccc"
	ans = solve(int(k), t, p)
	print(len(ans), *ans)
	k, t, p = 3, "aaa", "xxx"
	ans = solve(int(k), t, p)
	print(len(ans), *ans) 
"""

"""
if __name__ == "__main__":
	lines = int(input())
	for l in range(lines):
		k, t, p = input().split()
		ans = solve(int(k), t, p)
		print(len(ans), *ans)
"""



for line in sys.stdin.readlines():
	k, t, p = line.split()
	ans = solve(int(k), t, p)
	print(len(ans), *ans)

