# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])
# Worker = named list("Worker", ["id", "free_at"])


def assign_jobs_naive(n_workers, jobs):
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result


def assign_jobs(n_workers, jobs):
    """
    Function that create a heap of n_workers node than loop throw all jobs need to be done where add time for current job
    complete to the root and shift root down. Shifting keeps the root as most available worker of thread.
    :param n_workers: amount of workers in thread
    :param jobs: list of work need to be done
    :return: list of size jobs with namedtuple("AssignedJob", ["worker", "started_at"])
    """
    result = []
    threads = [[x, 0] for x in range(n_workers)]  # as list of Workers
    for job in jobs:
        result.append(AssignedJob(worker=threads[0][0], started_at=threads[0][1]))
        threads[0][1] += job
        shift_down_worker(threads, 0)

    return result


def shift_down_worker(workers_pack: list, parent_worker_in_pack_index: int):
    """
    Procedure that shifts down an element of 'named' heap. Every node has "id" and it's "value" is time, when worker
    free at. Shifting goes in two ways: if child value is smaller that parent or if child value is equal and
    it's id is smaller than parent id.
    :param workers_pack: list of threads with workers. Worker repr as list(int("id"), int("free_at_time"))
    :param parent_worker_in_pack_index: index of parent node
    """
    min_free_time_index = parent_worker_in_pack_index
    left_child = find_child(parent_index=parent_worker_in_pack_index, child_position="left")
    right_child = find_child(parent_index=parent_worker_in_pack_index, child_position="right")

    if right_child <= len(workers_pack) - 1:
        if workers_pack[right_child][1] < workers_pack[min_free_time_index][1]:
            min_free_time_index = right_child
        elif workers_pack[left_child][1] == workers_pack[min_free_time_index][1] and \
                workers_pack[right_child][0] < workers_pack[min_free_time_index][0]:
            min_free_time_index = right_child

    if left_child <= len(workers_pack) - 1:
        if workers_pack[left_child][1] < workers_pack[min_free_time_index][1]:
            min_free_time_index = left_child
        elif workers_pack[left_child][1] == workers_pack[min_free_time_index][1] and \
                workers_pack[left_child][0] < workers_pack[min_free_time_index][0]:
            min_free_time_index = left_child

    if min_free_time_index != parent_worker_in_pack_index:
        workers_pack[parent_worker_in_pack_index], workers_pack[min_free_time_index] = (
            workers_pack[min_free_time_index], workers_pack[parent_worker_in_pack_index]
        )
        shift_down_worker(workers_pack, parent_worker_in_pack_index=min_free_time_index)


def find_child(parent_index, child_position: str = "left"):
    """
    Function that find current index of node i child
    :param parent_index: node index
    :param child_position: position of child (left or right), default = "left"
    :return: child index
    """
    if child_position == "left":
        return (2*parent_index) + 1
    else:
        return (2*parent_index) + 2


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
