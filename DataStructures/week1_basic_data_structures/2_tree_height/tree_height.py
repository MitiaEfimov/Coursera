# python3

import sys
import threading
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class Node(object):

    def __init__(self):
        self.children = []
        self.root = False
        self.parent = 0


class Tree:

    def __init__(self):
        self.n = 0
        self.parent = []
        self.nodes = {}
        self.root = 0

    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))

    def get_from_file(self, n, parent):
        self.n = n
        self.parent = parent

    def grow_tree(self):
        for index in range(len(self.parent)):
            self.nodes[index] = Node()

        for index in range(len(self.parent)):
            parent = self.parent[index]
            if parent == -1:
                self.nodes[index].root = True
                self.nodes[index].parent = None
                self.root = index
            else:
                self.nodes[parent].children.append(index)
                self.nodes[index].parent = parent

    def compute_height(self, grown_tree=False, root=None, depth=1):
        if not grown_tree:
            self.grow_tree()
            root = self.root

        height = depth+1
        for node in self.nodes[root].children:
            if self.nodes[node].children:
                height = max(self.compute_height(grown_tree=True, root=node, depth=depth+1), height)
        else:
            if height > depth:
                return height
            else:
                return depth


def compute(n, parent):
    tree = Tree()
    tree.get_from_file(n, parent)
    height = tree.compute_height()
    print(height)
    return height


def main():
    tree = Tree()
    tree.read()
    height = tree.compute_height()
    print(height)
    return height


if __name__ == '__main__':
    threading.Thread(target=main).start()