# Python3
"""
In test happens many thing: creating database, doing some tables merges in that database, comparing a control property with
prepared answer.
"""


import unittest
from .merging_tables import Database


FILE_PATH = "3_merging_tables/tests/"


def get_data(file_path, need_answer=False):
    merges = []
    with open(file_path) as file:
        n_tables, n_merges = map(int, file.readline().split())
        rows_per_table_list = list(map(int, file.readline().split()))
        assert n_tables == len(rows_per_table_list)
        for line in range(n_merges):
            merges.append(tuple(map(int, file.readline().split())))

    if need_answer:
        answer = get_answer(file_path=file_path+".a", n_lines=n_merges)
        return rows_per_table_list, merges, answer
    else:
        return rows_per_table_list, merges


def get_answer(file_path, n_lines):
    answer = []
    with open(file_path) as answer_file:
        for line in range(n_lines):
            answer.append(int(answer_file.readline()[:-1]))
    return answer


class MergingTest(unittest.TestCase):

    def test_large(self):
        # If there is another tests to include it replace code below
        rows_counter, merges, actual_max_lines = get_data(FILE_PATH+"116", need_answer=True)
        db = Database(rows_counter)
        for merge, answer, i in zip(merges, actual_max_lines, range(1, len(merges)+1)):
            db.merge(merge[0] - 1, merge[1] - 1)
            self.assertEqual(answer, db.max_row_count, msg=f"Error after {i} merging. merge{merge}")
