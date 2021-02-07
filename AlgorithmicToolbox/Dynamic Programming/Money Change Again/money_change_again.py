# python3
"""Dynamic algorithm for money change problem

There are naive and fast algorithms for solution money change problem in program.

"""


def change_naive(money):
    """naive solution

    This solution iterates over all possible exchange combinations,
    and returns the combination with the least coins amount.

    """
    min_coins = float("inf")

    for num1 in range(money + 1):
        for num3 in range(money // 3 + 1):
            for num4 in range(money // 4 + 1):
                if 1 * num1 + 3 * num3 + 4 * num4 == money:
                    min_coins = min(min_coins, num1 + num3 + num4)

    return min_coins


def change(money):
    """Dynamic solution

    At first calculate, how much coins need to exchange 0, 1, 2, 3, 4 moneys.
    There for to takes 5 by adding one coin with denominations 1, 3, 4 is possible only
    with 4, 2 or 1 on hand.
    Therefore, the solution for 5 will be 1 new coin plus the number of coins needed
    to collect 4, 2 or 1.

    That is the idea.
    You can calculate how many coins you need to exchange for 'n' by adding one coin
    to the solution for finding n-1, n-3 or n-4.
    Since we are interested in the smallest number of coins,
    we will choose the smallest of these three solutions.

    As the result, you need to know the solution only for the previous 4,
    to calculate the required amount for n.

    """
    required_coin_amount = [0, 1, 2, 1, 1] + [0]*(money-4)
    if money == 0:
        return money
    if 0 < money < 5:
        return required_coin_amount[money]
    for i in range(5, money + 1):
        required_coin_amount[i] = 1 + min(
            required_coin_amount[i-1],
            required_coin_amount[i-3],
            required_coin_amount[i-4],
        )

    return required_coin_amount[-1]


if __name__ == '__main__':
    # Input Integer money.
    amount = int(input())
    # Outputs The minimum number of coins 
    # with denominations 1, 3, 4 that changes money.
    print(change(amount))
