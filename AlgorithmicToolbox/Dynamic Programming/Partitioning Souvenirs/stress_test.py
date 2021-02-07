from random import randint
from partition_souvenirs import partition3 as my
from partition import findPartition as geek


def test():
    tests = 0
    fails = 0
    fails_data = []
    while True:
        tests += 1
        values = [randint(1, 30) for _ in range(randint(1, 5))]
        values.sort(reverse=True)
        geek_answer = geek(values)
        my_answer = my(values)
        if geek_answer != my_answer:
            fails += 1
            fails_data += ([values], my_answer, geek_answer)
            print(f"FAIL: values = {values}")
            print(f"my = {my_answer}, geek = {geek_answer}")
            if fails == 10:
                break
        elif tests % 10000 == 0:
            print(f"Test {tests} is fine")
            print(f"values = {values}")
            print(f"my = {my_answer}, geek = {geek_answer}")

    data = (fails, fails_data)
    return data


if __name__ == "__main__":
    print(test())
