# python3
"""Solution for money change problem

This solution based on greedy algorithm.

"""


def money_change(money):
    assert 0 <= money <= 10 ** 3
    coin = 0
    while money != 0:
        while money // 10 != 0:
            coin += 1
            money -= 10
        while money // 5 != 0:
            coin += 1
            money -= 5
        while money // 1 != 0:
            coin += 1
            money -= 1
    return coin


if __name__ == '__main__':
    # Input an integer M
    input_money = int(input())
    # Outputs the minimum number of coins with 
    # denominations 1, 5, 10 that changes M
    print(money_change(input_money))
