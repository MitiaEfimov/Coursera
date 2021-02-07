#Uses python3

import sys
from collections import deque

def distance(adj, s, t):
    #write your code here
    return -1



class Vertice():
    def __init__(self, pos):
        self.pos = pos
        self.nbors_to = []
        self.nbors_from = []
        self.prev = []
        self.dist = [] 
        self.zone = None
        self.pre_clock = 0
        self.post_clock = 0
        

class Graph(object):
    def __init__(self, vertices:list = [], edges:list = []):
        self.vertices = vertices
        self.visited_list = [False] * len(self.vertices)
        self.edges = edges
        self.zone_num = 0
        self.zones = {}
        self.acyclic = True
        self.tick = 0
        self.post_order = {"list": []}
        self.pre_oreder = {"list": []}
        self.bipartite = True

    def is_acyclic(self, acyclic:bool):
        self.acyclic = acyclic

    def zone_counter(self, increase=False, decrease=False):
        if increase:
            self.zone_num += 1
        elif decrease:
            self.zone_num -= 1

    def solve(self, param_1=False, param_2=False):
        answer = self.reconstruct_path(param_1, param_2)
        return len(answer) if answer else -1

    def assign_zone(self, Vertice):
        Vertice.zone = self.zone_num
        if self.zones.get(self.zone_num, False):
            self.zones[self.zone_num].append(Vertice.pos)
            self.acyclic = False
        else:
            self.zones[self.zone_num] = [Vertice.pos]
    
    def add_vertice(self, Vertice):
        self.vertices.append(Vertice)

    def pre_visit(self, Vertice):
        Vertice.pre_clock = self.tick
        self.pre_oreder[self.tick] = Vertice
        self.pre_oreder["list"].append(self.tick)
        self.tick += 1

    def post_visit(self, Vertice):
        Vertice.post_clock = self.tick
        self.post_order[self.tick] = Vertice
        self.post_order["list"].append(self.tick)
        self.tick += 1

    def mark_unvisited(self):
        self.visited_list = [False] * len(self.vertices)

    def explore_directed(self, Vertice, reverse_orientation=False, zone_ident=False, pre_visit=False, post_visit=False):
        self.visited_list[Vertice.pos] = True
        if zone_ident:
            self.assign_zone(Vertice)
        if pre_visit:
            self.pre_visit(Vertice)

        nbors = Vertice.nbors_from if reverse_orientation else Vertice.nbors_to
        for vertice in nbors:
            if not self.visited_list[vertice.pos]:
                self.explore_directed(vertice,
                                      reverse_orientation=reverse_orientation,
                                      zone_ident=zone_ident,
                                      pre_visit=pre_visit,
                                      post_visit=post_visit)

        if post_visit:
            self.post_visit(Vertice)

    def explore_undirected(self, Vertice, zone_ident=False, pre_visit=False, post_visit=False):
        self.visited_list[Vertice.pos] = True
        if zone_ident:
            self.assign_zone(Vertice)
        if pre_visit:
            self.pre_visit(Vertice)

        nbors = Vertice.nbors_from + Vertice.nbors_to
        for vertice in nbors:
            if not self.visited_list[vertice.pos]:
                self.explore_undirected(vertice,
                                         zone_ident=zone_ident, 
                                         pre_visit=pre_visit, 
                                         post_visit=post_visit)

        if post_visit:
            self.post_visit(Vertice)

    def dfs(self, reverse_orientation=False, pre_visit=False, post_visit=False, zone_ident=False, undirected=False):
        self.mark_unvisited()
        for v in self.vertices:
            if not self.visited_list[v.pos]:
                if not undirected:
                    self.explore_directed(v, reverse_orientation=reverse_orientation, pre_visit=pre_visit, post_visit=post_visit)
                else:
                    self.explore_undirected(v, pre_visit=pre_visit, post_visit=post_visit, zone_ident=zone_ident)
                    self.zone_counter(increase=True)

    def bfs(self, Vertice, undirected=True):
        Vertice.dist = [float("+inf")] * len(self.vertices)
        Vertice.prev = [None] * len(self.vertices)
        Vertice.dist[Vertice.pos] = 0
        discovering_queue = deque()
        discovering_queue.append(Vertice)
        while len(discovering_queue) != 0:
            vertice = discovering_queue.popleft()
            if undirected:
                nbors = vertice.nbors_from + vertice.nbors_to
            else:
                nbors = vertice.nbors_to
            for nbor in nbors:
                if Vertice.dist[nbor.pos] == float("+inf"):
                    discovering_queue.append(nbor)
                    Vertice.dist[nbor.pos] = Vertice.dist[vertice.pos] + 1
                    Vertice.prev[nbor.pos] = vertice
                else:
                    self.bipartite = False

    def strong_connection_components(self):
        self.zone_num = 0
        self.zones = {}
        self.dfs(reverse_orientation=True, pre_visit=True, post_visit=True)
        self.mark_unvisited()
        for i in reversed(self.post_order["list"]):
            vert_ind = self.post_order[i].pos
            if not self.visited_list[vert_ind]:
                self.explore_directed(self.post_order[i], zone_ident=True)
                self.zone_counter(increase=True)

    def connection_components(self):
        self.zone_num = 0
        self.zones = {}
        self.dfs(zone_ident=True, undirected=True)

    def topological_sort(self):
        self.dfs(post_visit=True)
        self.tick = 0
        self.topological_order = []
        for i in reversed(self.post_order["list"]):
            self.topological_order.append(self.post_order[i].pos)

    def reconstruct_path(self, from_vert: Vertice, to_vert:Vertice, undirected=True):
        self.bfs(from_vert, undirected=undirected)
        prev = from_vert.prev
        if prev[to_vert.pos] is None:
            return False

        path = deque() 
        while from_vert != to_vert:
            path.appendleft(to_vert.pos)
            to_vert = prev[to_vert.pos]
        return path        


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [Vertice(i) for i in range(n)]
    for (a, b) in edges:
        adj[a - 1].nbors_to.append(adj[b - 1])
        adj[b - 1].nbors_from.append(adj[a - 1])
    s, t = adj[data[2 * m] - 1], adj[data[2 * m + 1] - 1]
    g = Graph(adj, edges)
    print(g.solve(s, t))
