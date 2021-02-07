import unittest
import sys
import threading

from .tree_height_slow import compute_height as slow
from .tree_height import compute as fast

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)


def get_data(path):
    with open(path, "r") as file:
        n = int(file.readline())
        parents = list(map(int, file.readline().split()))
        return n, parents


def get_answer(path):
    with open(path, "r") as file:
        answer = file.readline()
        return int(answer[:-1])


class TestTreeHeight(unittest.TestCase):

    path = "D:/PythonProjects/Coursera/DataStructures/Coursera_files/week1_basic_data_structures/2_tree_height/tests/"

    def test_big(self, path=path):

        for i in range(1, 25):
            file = path + f"{i}".rjust(2, "0")
            n, parents = get_data(file)
            file = file + ".a"
            answer = get_answer(file)
            improved = fast(n, parents)
            self.assertEqual(improved, answer)

