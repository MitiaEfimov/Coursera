# Python3

import unittest
from timeit import Timer

from tree_orders import run_test
from tree_orders import create_tree

TESTS_PATH = "D:/PythonProjects/Coursera/DataStructures/Coursera_files/week4_binary_search_trees/1_tree_traversals/tests/"

def get_data(file_path, need_answer=False):
    with open(file_path) as f:
        lines = int(f.readline())
        keys = [0] * lines
        left = [0] * lines
        right = [0] * lines
        for i in range(lines):
            [a, b, c] = map(int, f.readline().split())
            keys[i] = a
            left[i] = b
            right[i] = c

    if need_answer:
        inorder, preorder, postorder = get_answer(file_path+".a", lines)
        return keys, left, right, inorder, preorder, postorder
    else:
        return keys, left, right


def get_answer(file_path, node_number):
    answer = []
    with open(file_path) as answer_f:
        for i in range(3):
            answer.append(list(map(int, answer_f.readline().split())))
    inorder = answer[0]
    preorder = answer[1]
    postorder = answer[2]
    return inorder, preorder, postorder

"""
class TraversalTest(unittest.TestCase):

    def test_cases(self):
        for i in range(21, 22):
            query, answer = get_data(TESTS_PATH+f"{i}".rjust(2, "0"), need_answer=True)
            self.assertEqual(run_test(query_list=query), answer, msg="")
"""

def correct_answer_test():
    for i in range(19, 21):
        (key, left, right, inorder, preorder, postorder) = get_data(TESTS_PATH+f"{i}".rjust(2, "0"), True)
        tree = create_tree(key, left, right)
        answer = run_test(tree)
        inMain, preMain, postMain = answer[0]
        inIter, preIter, postIter = answer[1]
        if inMain == inorder and inIter == inorder:
            time_testing(tree, traversal="In order")
        elif inMain == inorder:
            print("there is mistake in Iter solution")
        else:
            print("there is mistake in Main solution")
        if preMain == preorder and preIter == preorder:
            time_testing(tree, traversal="Pre order")
        elif preMain == preorder:
            print("there is mistake in Iter solution")
        else:
            print("there is mistake in Main solution")
        if postMain == postorder and postIter == postorder:
            time_testing(tree, traversal="Post order")
        elif postMain == postorder:
            print("there is mistake in Iter solution")
        else:
            print("there is mistake in Main solution")
        #print("inMain solution is fine" if inMain == inorder else "there is mistake in inMain solution")
        #print("preMain solution is fine" if preMain == preorder else "there is mistake in preMain solution")
        #print("postMain solution is fine" if postMain == postorder else "there is mistake in postMain solution")
        #print("inIter solution is fine" if inIter == inorder else "there is mistake in inIter solution")
        #print("preIter solution is fine" if preIter == preorder else "there is mistake in preIter solution")
        #print("postIter solution is fine" if postIter == postorder else "there is mistake in postIter solution")
        #time_testing(tree)
    else:
        print("КРАСАВА")

def time_testing(tree, traversal):
    if traversal == "In order":
        inMainTime = Timer(lambda: tree.inOrder())
        inMainTime = float(inMainTime.timeit(number=1000))
        inIterTime = Timer(lambda: tree.inOrderIter())
        inIterTime = float(inIterTime.timeit(number=1000))
        msg = f"\ninOrder traversal: (answer is fine)\n"\
              f"Main solution = {inMainTime} vs Iter solution {inIterTime}\n"
    elif traversal == "Pre order":
        preMainTime = Timer(lambda: tree.preOrder())
        preMainTime = float(preMainTime.timeit(number=1000))
        preIterTime = Timer(lambda: tree.preOrderIter())
        preIterTime = float(preIterTime.timeit(number=1000))
        msg = f"preOrder traversal:(answer is fine)\n"\
              f"Main solution = {preMainTime} vs Iter solution {preIterTime}\n"
    elif traversal == "Post order":
        postMainTime = Timer(lambda: tree.postOrder())
        postMainTime = float(postMainTime.timeit(number=1000))
        postIterTime = Timer(lambda: tree.postOrderIter())
        postIterTime = float(postIterTime.timeit(number=1000))
        msg = f"postOrder traversal:(answer is fine)\n"\
              f"Main solution = {postMainTime} vs Iter solution {postIterTime}\n"
    print(msg)

    

if __name__ == "__main__":
    correct_answer_test()



