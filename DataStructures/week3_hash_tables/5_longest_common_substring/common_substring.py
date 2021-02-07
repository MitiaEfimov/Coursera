# python3

import sys
from collections import namedtuple
from random import randint

Answer = namedtuple('answer_type', 'i j len')


def solve_naive(s, t):
	ans = Answer(0, 0, 0)
	for i in range(len(s)):
		for j in range(len(t)):
			for l in range(min(len(s) - i, len(t) - j) + 1):
				if (l > ans.len) and (s[i:i+l] == t[j:j+l]):
					ans = Answer(i, j, l)
	return ans


def hash_func(string, multiplier: int, prime: int):
	ans = 0
	for c in string[::-1]:
		ans = (ans * multiplier + ord(c)) % prime
	return ans


def precompute_hashes(text: str, len_pattern: int, multiplier: int, prime: int):
	hashes = [0] * (len(text) - len_pattern + 1)
	last_sub_str = str(text[len(text)-len_pattern:])
	hashes[len(text)-len_pattern] = hash_func(last_sub_str, multiplier, prime)
	y = 1
	for i in range(1, len_pattern+1):
		y = (y * multiplier) % prime
	for i in range(len(text)-len_pattern-1, -1, -1):
		hashes[i] = ((multiplier * hashes[i + 1]) + ord(text[i]) - (y * ord(text[i + len_pattern]))) % prime
	return hashes


def find_matches(hash_table_1: dict, leftmost_1:int, hash_table_2: dict, leftmost_2:int, length):
	prime_1 = 10**9 + 7
	prime_2 = 10**9 + 9
	
	if not hash_table_1.get(length, False):
		hash_table_1[length] = precompute_hashes(hash_table_1["text"], length, hash_table_1["multiplier"], prime_1)
		ht_1 = hash_table_1[length]
	if not hash_table_2.get(length, False):
		hash_table_2[length] = precompute_hashes(hash_table_2["text"], length, hash_table_2["multiplier"], prime_1)
		ht_2 = hash_table_2[length]
	

	for ih_1 in range(leftmost_1, len(ht_1)):
		for ih_2 in range(leftmost_2, len(ht_2)):
			if ht_1[ih_1] == ht_2[ih_2]:
				ind_1 = hash_func(hash_table_1["text"][ih_1:(ih_1+length)], hash_table_1["multiplier"], prime_2)
				ind_2 = hash_func(hash_table_2["text"][ih_2:(ih_2+length)], hash_table_2["multiplier"], prime_2)
				if ind_1 == ind_2:
					return (ih_1, ih_2)
	else:
		return False


def solve(s, t):
	ans = Answer(0, 0, 0)
	multiplier = randint(1,10**5)
	s_hash_table, t_hash_table = dict(), dict()
	s_hash_table["text"], t_hash_table["text"] = s, t
	s_hash_table["multiplier"], t_hash_table["multiplier"] = multiplier, multiplier

	left, right = 0, min(len(s), len(t))
	while left <= right:
		#print("lef = ", left)
		#print("right = ", right)
		mid = left + ((right-left)//2)
		#print("mid = ", mid)
		match_found = find_matches(s_hash_table, ans.i, t_hash_table, ans.j, mid)
		if match_found:
			ans = Answer(match_found[0], match_found[1], mid)
			left = mid + 1
		else:
			right = mid - 1  
	return ans


"""
if __name__ == "__main__":
	s, t = "cool", "toolbox"
	ans = solve(s, t)
	print(ans.i, ans.j, ans.len)
	s, t = "aaa", "bb"
	ans = solve(s, t)
	print(ans.i, ans.j, ans.len)
	s, t = "aabaa", "babbaab"
	ans = solve(s, t)
	print(ans.i, ans.j, ans.len)
"""

"""
if __name__ == "__main__":
	lines = int(input())
	for l in range(lines):
		s, t = input().split()
		ans = solve(s, t)
		print(ans.i, ans.j, ans.len)
"""
"""
for line in sys.stdin.readlines():
	s, t = line.split()
	ans = solve(s, t)
	print(ans.i, ans.j, ans.len)
"""

if __name__ == "__main__":
	lines = input().split("\n")
	for line in lines:
		s, t = line.split()