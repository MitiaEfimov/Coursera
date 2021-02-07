# python3


import sys


class Solver:
	_prime1 = 1000000007
	_prime2 = 1000000009
	x = 11
	
	def __init__(self, s):
		self.s = s
		self.hash_table = dict()
		self.pow_of_prime_1 = [1]
		self.hash_table_2 = dict()
		self.pow_of_prime_2 = [1]

	def hash_func(self, string, multiplier: int, prime: int):
	    ans = 0
	    for c in string[::-1]:
	        ans = (((ans * multiplier) % prime) + ord(c)) % prime
	    return ans
	

	def precompute_hashes(self, text: str, pattern: str, multiplier: int, prime:int, y):
	    hashes = [0] * (len(text) - len(pattern) + 1)
	    last_sub_str = str(text[len(text)-len(pattern):])
	    hashes[len(text)-len(pattern)] = self.hash_func(last_sub_str, multiplier, prime)
		
	    for i in range(len(text)-len(pattern)-1, -1, -1):
	        hashes[i] = ( ((multiplier * hashes[i + 1]) %prime) + ord(text[i]) - (y * ord(text[i + len(pattern)]))%prime ) % prime
	    return hashes

	def compute_power(self, prime,  start:"lenght of pow list", stop:"lenght of pattern"):
		if prime == self._prime1:
			y = self.pow_of_prime_1[-1]
			for i in range(start, stop+1):
				y = (y * self.x) % prime
				self.pow_of_prime_1.append(y)
		else:
			y = self.pow_of_prime_2[-1]
			for i in range(start, stop+1):
				y = (y * self.x) % prime
				self.pow_of_prime_2.append(y)			


	def ask(self, a, b, l):
		if not self.hash_table.get(l, False):
			if l >= len(self.pow_of_prime_1):
				self.compute_power(self._prime1, len(self.pow_of_prime_1), l)
				self.compute_power(self._prime2, len(self.pow_of_prime_2), l)
			h_1 = self.precompute_hashes(self.s, s[a:a+l], self.x, self._prime1, self.pow_of_prime_1[l])
			h_2 = self.precompute_hashes(self.s, s[a:a+l], self.x, self._prime2, self.pow_of_prime_2[l])
			self.hash_table[l] = h_1
			self.hash_table_2[l] = h_2


		if self.hash_table[l][a] == self.hash_table[l][b]:
			ind_1 = self.hash_table_2[l][a]
			ind_2 = self.hash_table_2[l][b]
			return ind_1 == ind_2	

"""
s = sys.stdin.readline()[:-1]
q = int(sys.stdin.readline())
solver = Solver(s)
for i in range(q):
	a, b, l = map(int, sys.stdin.readline().split())
	print("Yes" if solver.ask(a, b, l) else "No")
"""

if __name__ == "__main__":
	s = input()
	q = int(input())
	solver = Solver(s)
	for i in range(q):
		a, b, l = map(int, input().split())
		print("Yes" if solver.ask(a, b, l) else "No")

