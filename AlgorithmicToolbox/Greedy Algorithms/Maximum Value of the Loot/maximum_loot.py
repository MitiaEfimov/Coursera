# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    val_per_unit = [float(prices[x]/weights[x]) for x in range(len(weights))]
    index = 0
    opt_value = 0
    while capacity != 0:
        index = val_per_unit.index(max(val_per_unit))
        while weights[index] != 0:
            opt_value += val_per_unit[index]
            capacity -=1
            weights[index] -= 1
            if capacity == 0:
                break
        val_per_unit.pop(index)
        weights.pop(index)
        prices.pop(index)
        if len(weights) == 0:
            break
    return opt_value

if __name__ == "__main__":
    # The first line of the input contains the number 𝑛 of items 
    # and the capacity 𝑊 of a knapsack.
    # The next 𝑛 lines define the values and weights of the items. 
    # The 𝑖-th line contains integers 𝑣𝑖 and 𝑤𝑖—the
    # value and the weight of 𝑖-th item, respectively
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    # Outputs the maximal value of fractions of items that fit into the knapsack.
    print("{:.10f}".format(opt_value))
