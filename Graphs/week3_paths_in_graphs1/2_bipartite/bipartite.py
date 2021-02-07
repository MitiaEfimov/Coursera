#Uses python3

import sys
import random
from timeit import timeit
from collections import deque

def bipartite(adj):
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
        self.visit_counter = 0
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
        self.is_bipartite()
        return 0 if not self.bipartite else 1

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
            self.visited_list[vertice.pos] = True
            self.visit_counter += 1
            if undirected:
                nbors = vertice.nbors_from + vertice.nbors_to
            else:
                nbors = vertice.nbors_to
            for nbor in nbors:
                if Vertice.dist[nbor.pos] == float("+inf"):
                    discovering_queue.append(nbor)
                    Vertice.dist[nbor.pos] = Vertice.dist[vertice.pos] + 1
                    Vertice.prev[nbor.pos] = vertice
                elif (Vertice.dist[nbor.pos] - Vertice.dist[vertice.pos]) == 0:
                    self.bipartite = False
                    # it's enough for this problem, so just quit
                    return

    def is_bipartite(self):
        self.mark_unvisited()
        for i, vertice in enumerate(self.vertices):
            if not self.visited_list[i]:
                if isinstance(vertice, int):
                    self.vertices[vertice] = Vertice(vertice)
                    self.visited_list[vertice] = True
                    self.visit_counter += 1
                    continue
                self.bfs(vertice, undirected=True)
                vertice.dist = []
                vertice.prev = []                
                if not self.bipartite:
                    break
                elif self.visit_counter == len(self.vertices):
                    break



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


def create_case(n, m):
    # read the number of vertices and the edges from the input
    # that is not always the most convenient way for handling such a script, but I use it for simplicity
    partA = []
    partB = []
    # generate a random partition
    for i in range(n):
      if random.randint(1,2) == 1:
        partA.append(i)
      else:
        partB.append(i)
    
    # make sure that it is possible to have m edges at all:
    m = min(m, len(partA) * len(partB))  
    
    edges = set()
    while len(edges) < m:
      x = partA[random.randrange(len(partA))]
      y = partB[random.randrange(len(partB))]
      # add an edge to the set (swap x and y if x > y to avoid parallel edges)
      edges.add((min(x,y), max(x,y)))
    
    # print the edge
    
    return edges 


def test():
    for _ in range(100):
        vertices_num = random.randint(10**5 - 100, 10**5)
        edges_num = random.randint(10**5 - 100, 10**5)
        adj = [Vertice(i) for i in range(vertices_num)]
        edges = create_case(vertices_num, edges_num)
        for (a, b) in edges:
            adj[a - 1].nbors_to.append(adj[b - 1])
            adj[b - 1].nbors_from.append(adj[a - 1])
        g = Graph(adj, edges)
        t = timeit(lambda: g.is_bipartite(), number=1) 
        print(str(t)+"\n")
        if not g.bipartite:
            print(vertices_num,  edges_num)
            for e in edges:
              print(e[0],  e[1])
            print(g.solve(adj))
            print("don't know why it is not right")


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = list(range(n))
    for (a, b) in edges:
        if isinstance(adj[a - 1], int):
            adj[a - 1] = Vertice(a-1)
        if isinstance(adj[b - 1], int):
            adj[b - 1] = Vertice(b-1)
        adj[a - 1].nbors_to.append(adj[b - 1])
        adj[b - 1].nbors_from.append(adj[a - 1])
    g = Graph(adj, edges)
    print(g.solve(adj))
