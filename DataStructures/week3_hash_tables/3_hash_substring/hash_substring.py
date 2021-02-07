# python3


def read_input():
    return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    return [
        i 
        for i in range(len(text) - len(pattern) + 1) 
        if text[i:i + len(pattern)] == pattern
    ]


def hash_func(string, multiplier: int, prime: int):
    ans = 0
    for c in string[::-1]:
        ans = (ans * multiplier + ord(c)) % prime
    return ans


def precompute_hashes(text: str, pattern: str, multiplier: int, prime: int):
    hashes = [0] * (len(text) - len(pattern) + 1)
    last_sub_str = str(text[len(text)-len(pattern):])
    hashes[len(text)-len(pattern)] = hash_func(last_sub_str, multiplier, prime)
    y = 1
    for i in range(1, len(pattern)+1):
        y = (y * multiplier) % prime
    for i in range(len(text)-len(pattern)-1, -1, -1):
        hashes[i] = ((multiplier * hashes[i + 1]) + ord(text[i]) - (y * ord(text[i + len(pattern)]))) % prime
    return hashes


def RabinKarp(pattern, text):
    x, p = 2, 1000000007
    result = []
    pHash = hash_func(pattern, x, p)
    hashes = precompute_hashes(text, pattern, x, p)
    for i in range(len(text)-len(pattern)+1):
        if pHash == hashes[i] and text[i:i+len(pattern)] == pattern:
            result.append(i)
    return result


if __name__ == '__main__':
    print_occurrences(RabinKarp(*read_input()))

