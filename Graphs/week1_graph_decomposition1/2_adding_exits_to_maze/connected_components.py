#Uses python3

import sys


class Vertice(object):
    def __init__(self, pos):
        self.pos = pos
        self.adj = []
        self.visited = False
        self.ccnum = None

    def change_visit_status(self):
        self.visited = not self.visited

    def assign_cnum(self, connection_components_num:int):
        self.ccnum = connection_components_num

    def add_nbor_to_list(self, nbor_pos):
        self.adj.append(nbor_pos)


def explore(vertice:Vertice, ccnum):
    vertice.change_visit_status()
    vertice.assign_cnum(ccnum)
    for v in vertice.adj:
        if not v.visited:
            explore(v, ccnum)


def number_of_components(adj):
    result = 0
    for vertice in adj:
        if not vertice.visited:
            explore(vertice, result)
            result += 1
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [Vertice(i) for i in range(n)]
    for (a, b) in edges:
        adj[a - 1].add_nbor_to_list(adj[b - 1])
        adj[b - 1].add_nbor_to_list(adj[a - 1])
    print(number_of_components(adj))


"""
if __name__ == '__main__':
    first, second = input().split()
    first, second = int(first), int(second)
    data = [first, second]
    for i in range(second):
        data += list(map(int, input().split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [Vertice(n) for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].add_nbor_to_list(adj[b - 1])
        adj[b - 1].add_nbor_to_list(adj[a - 1])
    print(number_of_components(adj))
"""