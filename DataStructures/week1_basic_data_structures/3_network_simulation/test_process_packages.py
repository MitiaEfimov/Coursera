import os
import unittest
from .process_packages import testing as packing

# Testing folder with testing cases
PATH = "D:/PythonProjects/coursera/DataStructures/Coursera_files/week1_basic_data_structures/3_network_simulation/tests/"


class NetworkSimulationTesting(unittest.TestCase):

    def test_from_folder(self):
        for i in range(1, files_in_folder(PATH)//2):

            file = PATH + f"{i}".rjust(2, "0")
            my_answer = packing(file)
            file = file + ".a"
            right_answer = get_answer(file)
            self.assertEqual(my_answer, right_answer, msg=(f"test case {i}".rjust(2, "0") +
                                                           f"\nMy:{my_answer}\nRight:{right_answer}"))


def get_answer(path):
    """
    Answer file contain [n] lines with starting time if pack have been processing or -1 if it was dropped.
    :param path:
    :return: list of [n] integers
    """
    with open(path, "r") as file:
        n = lines_in_file(path[:-2])
        answer = []
        for _ in range(n):
            answer.append(int(file.readline()))
    return answer


def lines_in_file(path):
    """
    Function that counts lines amount in file
    :param path:
    :return: number of lines in file
    """
    with open(path, "r") as file:
        n = int(file.readline().split()[-1])
    return n


def files_in_folder(path):
    """
    Function that counts files amount in folder
    :param path: absolute path to folder
    :return: number of files in folder
    """
    files = os.listdir(path)
    return len(files)

