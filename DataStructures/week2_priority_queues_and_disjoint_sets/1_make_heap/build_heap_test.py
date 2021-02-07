# python3

import unittest
from .build_heap import build_heap


def get_data(file_path):
    with open(file_path) as f:
        n = f.readline()
        data = f.read()[:-1]
    return n, data


class TestHeap(unittest.TestCase):

    def test_build_heap(self):
        path = "D:/PythonProjects/Coursera/DataStructures/Coursera_files/" \
               "week2_priority_queues_and_disjoint_sets/1_make_heap/tests/"

        for i in range(4, 5):
            file = path + f"{i}".rjust(2, "0")
            data = list(map(int, get_data(file)[1].split()))
            answer_data = list(get_data(file+".a")[1].split(sep="\n"))
            swaps = build_heap(data)
            for index in range(len(answer_data)):
                answer_data[index] = tuple(map(int, answer_data[index].split()))
                self.assertEqual(answer_data[index], swaps[index])

