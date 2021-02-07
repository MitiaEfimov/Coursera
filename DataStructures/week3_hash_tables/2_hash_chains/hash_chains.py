# python3


from _collections import deque


class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = []
        self.table = dict()

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query_naive(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            self.write_chain(cur for cur in reversed(self.elems)
                        if self._hash_func(cur) == query.ind)
        else:
            try:
                ind = self.elems.index(query.s)
            except ValueError:
                ind = -1
            if query.type == 'find':
                self.write_search_result(ind != -1)
            elif query.type == 'add':
                if ind == -1:
                    self.elems.append(query.s)
            else:
                if ind != -1:
                    self.elems.pop(ind)

    def process_query(self, query):
        # Output the content of the i-th list in the table. 
        # Use spaces to separate the elements of the list.
        # If i-th list is empty, output a blank line.
        if query.type == "check":
            self.write_chain(cur for cur in reversed(self.table.get(query.ind, list())))
        
        else:
            h = self._hash_func(query.s)
            if self.table.get(h):
                try:
                    ind = self.table[h].index(query.s)
                except ValueError:
                    ind = -1
            else:
                ind = -1

            # Output “yes" or “no"(without quotes)depending on whether the table contains string or not.
            if query.type == "find":
                self.write_search_result(ind != -1)
    
            # Insert string into the table. 
            # If there is already such string in the hash table, then just ignore the query. 
            elif query.type == "add":
                if self.table.get(h) == None:
                    self.table[h] = []
                if ind == -1:
                    self.table[h].append(query.s)

            # Remove string from the table.
            # If there is no such string in the hash table, then just ignore the query.    
            elif query.type == "del":
                if ind != -1:
                    self.table[h].pop(ind)


    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())



if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
