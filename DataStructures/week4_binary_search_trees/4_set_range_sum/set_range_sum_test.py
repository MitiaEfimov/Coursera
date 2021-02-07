# Python3

import unittest
from set_range_sum import run_test

TESTS_PATH = "D:/PythonProjects/Coursera/DataStructures/Coursera_files/week4_binary_search_trees/4_set_range_sum/tests/"

def get_data(file_path, need_answer=False):
    with open(file_path) as f:
        lines = int(f.readline())
        answer_lines = 0
        query = list()
        for _ in range(lines):
            query.append(f.readline().split())
            if query[-1][0] in "?s":
                answer_lines += 1

    if need_answer:
        answer = get_answer(file_path+".a", answer_lines)
        return query, answer
    else:
        return query


def get_answer(file_path, n_queries):
    answer = []
    with open(file_path) as answer_f:
        for line in range(n_queries):
            answer.append(answer_f.readline()[:-1])
    return answer


class RangeSumTest(unittest.TestCase):

    def test_cases(self):
        for i in range(1, 7):
            query, answer = get_data(TESTS_PATH+f"{i}".rjust(2, "0"), need_answer=True)
            self.assertEqual(run_test(query_list=query), answer, msg="")


"""
if __name__ == "__main__":
    for i in range(1, 7):
        query, right_answer = get_data(TESTS_PATH+f"{i}".rjust(2, "0"), True)
        answer = run_test(query)
        for index, ans in enumerate(answer):
            if right_answer[index] != ans:
                print(ans, right_answer[index])
                print("shit happened")
        # else:    
        #     print(*query, sep="\n")
        #     print(*right_answer, sep="\n")
        #     print(*answer, sep="\n")
    else:
        print("КРАСАВА")
"""
