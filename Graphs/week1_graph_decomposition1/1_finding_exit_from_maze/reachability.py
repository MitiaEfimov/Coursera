#Uses python3

import sys


def explore(adj, vertice):
    adj[vertice][0] = True
    for i in adj[vertice][1:]:
        if not adj[i][0]:
            explore(adj, i)


def reach(adj, x, y):
    explore(adj, x)
    return (1 if adj[y][0] else 0)


def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[False] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))


def test():
    first, second = input().split()
    first, second = int(first), int(second)
    data = [first, second]
    for i in range(second + 1):
        data += list(map(int, input().split()))
    #data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[False] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))


if __name__ == '__main__':
    main()