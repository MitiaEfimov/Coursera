from money_change_again import change as fast
from money_change_again import change_naive as naive

"""Simple stress test, that compare naive result of n money with fast"""


def stress():
    for i in range(101):
        if fast(i) != naive(i):
            print(f"{i} money error, {naive(i)} != {fast(i)}")
        elif i % 10 == 0 and i != 0:
            print(f"test for {i-10} to {i} is OK")


if __name__ == "__main__":
    stress()
