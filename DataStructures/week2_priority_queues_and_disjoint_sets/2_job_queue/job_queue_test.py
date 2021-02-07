# Python3

import unittest
from collections import namedtuple
from random import randint, choice
from .job_queue import assign_jobs as fast_assign
from .job_queue import assign_jobs_naive as naive_assign

TESTS_PATH = "D:/PythonProjects/Coursera/DataStructures/Coursera_files/week2_priority_queues_and_disjoint_sets/2_job_queue/tests/"
AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def get_data(file_path, need_answer=False):
    with open(file_path) as f:
        n_workers, n_jobs = map(int, f.readline().split())
        jobs = list(map(int, f.readline().split()))
    if need_answer:
        answer = get_answer(file_path+".a", n_jobs)
        return n_workers, jobs, answer
    else:
        return n_workers, jobs


def get_answer(file_path, n_jobs):
    answer = []
    with open(file_path) as answer_f:
        for line in range(n_jobs):
            worker_id, started_at = map(int, answer_f.readline().split())
            answer.append(AssignedJob(worker=worker_id, started_at=started_at))
    return answer


class JobQueueTest(unittest.TestCase):

    def test_cases_brute(self):
        for i in range(1, 4):
            n_workers, jobs = get_data(TESTS_PATH+f"{i}".rjust(2, "0"))
            self.assertEqual(fast_assign(n_workers=n_workers, jobs=jobs),
                             naive_assign(n_workers=n_workers, jobs=jobs))

    def test_cases_bif(self):
        for i in range(1, 6):
            n_workers, jobs, answer = get_data(TESTS_PATH+f"{i}".rjust(2, "0"), need_answer=True)
            self.assertEqual(fast_assign(n_workers=n_workers, jobs=jobs), answer)
    # TODO test_random
