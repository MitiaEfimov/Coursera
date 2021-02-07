# Python 3
"""
In this test used cases given from week3_hash_tables's resource page.
"""
import sys
import unittest
#from ..phone_book import process_queries as fast
#from ..phone_book import process_queries_naive as naive
#from ..phone_book import read_queries

FILE_PATH = "tests/"


def get_data(file_path, need_answer=False):
    data = []
    with open(file_path) as file:
        n_queries = int(file.readline())
        answer_counter = 0
        for line in range(n_queries):
            data.append(file.readline())
            if data[-1][0] == "find":
            	answer_counter += 1

    if need_answer:
        answer = get_answer(file_path=file_path+"a", n_lines=answer_counter)
        return data, answer
    else:
        return data


def get_answer(file_path, n_lines):
    answer = []
    with open(file_path) as answer_file:
        for line in range(n_lines):
            answer.append(answer_file.readline()[:-1])
    return answer


class PhoneBookTest(unittest.TestCase):

    def test_broot(self):
    	for file in range(1, 3):
    		data, answer = get_data(FILE_PATH+str(file).rjust(2, "0"), need_answer=True)
    		naive_answer = process_queries_naive(read_queries(test=True, data=data))
    		fast_answer = process_queries(read_queries(test=True, data=data))
    		self.assertEqual(naive_answer, fast_answer)


# need to delete all stuff below that line

def test():
	for file in range(1, 3):
		data = get_data(FILE_PATH+str(file).rjust(2, "0"))
		naive_answer = process_queries_naive(read_queries(test=True, data=data))
		fast_answer = process_queries(read_queries(test=True, data=data))
		if naive_answer == fast_answer:
			print(f"{file} is OK")
			print(f"naive = {naive_answer}\nfast  = {fast_answer}")


class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


def read_queries(test=False, data=None):
    if test:
        return [Query(data[i].split()) for i in range(len(data))]
    else:
        n = int(input())
        return [Query(input().split()) for _ in range(n)]



def write_responses(result):
    if not test:
        print('\n'.join(result))


def return_responses(number_of_queries):
    return process_queries(read_queries(number_of_queries))


def process_queries_naive(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = []
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            for contact in contacts:
                if contact.number == cur_query.number:
                    contact.name = cur_query.name
                    break
            else:  # otherwise, just add it
                contacts.append(cur_query)
        elif cur_query.type == 'del':
            for j in range(len(contacts)):
                if contacts[j].number == cur_query.number:
                    contacts.pop(j)
                    break
        else:
            response = 'not found'
            for contact in contacts:
                if contact.number == cur_query.number:
                    response = contact.name
                    break
            result.append(response)
    return result


def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = {}
    for cur_query in queries:
        if cur_query.type == 'add':
            contacts[cur_query.number] = cur_query.name
        elif cur_query.type == 'del':
            contacts.pop(cur_query.number, None)
        else:
            result.append(contacts.get(cur_query.number, "not found"))
    return result


if __name__ == "__main__":
	test()
