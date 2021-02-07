import unittest
from .check_brackets import find_mismatch


def get_data(file_path):
    with open(file_path, "r") as file:
        text = file.readline()[:-1]
        return text


class TestBracket(unittest.TestCase):

    def test_check_brackets(self):
        path = "D:/PythonProjects/Coursera/DataStructures/Coursera_files/week1_basic_data_structures/1_brackets_in_code/tests/"

        for i in range(1, 55):
            file = path + f"{i}".rjust(2, "0")
            data = get_data(file)
            answer = get_data(file+".a")
            self.assertEqual(find_mismatch(data), answer)
