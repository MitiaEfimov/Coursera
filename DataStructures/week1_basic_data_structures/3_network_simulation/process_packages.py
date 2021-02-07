# python3

from collections import namedtuple
from collections import deque

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = deque()

    def process(self, request):
        """
        Function that takes request and make decision that simulates network decisions:
         - Start process at the time with necessary time to process it;
         - Put process to buffer;
         - Call process from buffer;
         - Drop process.
        :param request: named tuple "Request"["arrived_at", "time_to_process"]
        :return:
        """
        # End all process, that already done by comparing with new process arrived time
        while self.finish_time and request.arrived_at >= self.finish_time[0]:
            self.finish_time.popleft()

        # Make decision drop process/put process in queue
        if self.finish_time and len(self.finish_time) >= self.size:
            return Response(True, -1)
        elif self.finish_time:
            request = Request(self.finish_time[-1], request.time_to_process)

        # Putting in queue
        self.finish_time.append(request.arrived_at + request.time_to_process)
        return Response(False, request.arrived_at)


def process_requests(requests, buffer):
    """
    Function that iterates throw all requests and simulates buffer process.
    :param requests: list of of named tuples "Request" ["arrived_at", "time_to_process"]
    :param buffer: class Buffer, initialised with integer equals buffer size
    :return: list of named tuple "Response" ["was_dropped", "started_at"]
    """
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def get_data(path: "path to testing folder"):
    """
    Data file named 00 and contain buffer_size and number = [n] of requests on first line.
    Next [n] lines contains starting time and time to process.
    :param path: absolute path to test folder
    :return: integer equals to buffer size and list of named tuples "Request" ["arrived_at", "time_to_process"]
    """

    with open(path, "r") as file:
        buffer_size, n_requests = map(int, file.readline().split())

        requests = []
        for _ in range(n_requests):
            arrived_at, time_to_process = map(int, file.readline().split())
            requests.append(Request(arrived_at, time_to_process))
    return buffer_size, requests


def testing(path: "path to test folder"):
    """
    Function that tests code with some cases, stored in Test folder
    Test folder have to contain numbered pairs of files started with 01 that means it contain data and 01.a for answer.
    :param path: absolute path to Test folder, indicated from external testing module.
    :return: list of starting time for case sample. It should be compared with right answer in external testing module.
    """
    # reading data from file
    buffer_size, requests = get_data(path)

    # starting simulation
    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    # Output simulation result
    out = []
    for response in responses:
        out.append(response.started_at if not response.was_dropped else -1)
    return out


def main():
    # reading data from input
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    # start simulation
    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    # output simulation result
    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
