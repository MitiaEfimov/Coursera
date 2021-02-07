import unittest

from random import seed
from random import choice
from random import randint

from .stack_with_max import simulating_implemented as fast
from .stack_with_max_naive import simulating_naive as slow


class TestStack(unittest.TestCase):

    def test_brute_random(self):
        for _ in range(100):
            queries = form_queries()
            naive = slow(queries)
            implemented = fast(queries)
            self.assertEqual(naive, implemented, msg=f"right: {naive},\nwrong: {implemented}")


def form_queries():
    seed(randint(1, 10000000))
    amount = randint(5, 100)
    q = [["push"], ["push"], ["pop"], ["max"]]
    push = 0
    pop = 0
    queries = list()
    for _ in range(amount):
        query = choice(q)
        if (query[0] == "pop" or query[0] == "max") and pop >= push:
            continue
        elif query[0] == "pop":
            queries.append(query)
            pop += 1
        elif query[0] == "max":
            queries.append(query)
        elif query[0] == "push":
            query = [query[0], str(randint(-1000, 1000))]
            queries.append(query)
            push +=1
    else:
        not_null = [["push", "50"], ["max"]]
        return queries if queries else not_null


