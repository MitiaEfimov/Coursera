# python3

from sys import stdin


def maximum_gold(capacity, weights):
    """
    Given 𝑛 gold bars with weights W1, W2 ... Wn
    Finds the maximum weight of gold that fits into a bag of capacity 𝑊.
    """
    assert 1 <= capacity <= 10 ** 4
    assert 1 <= len(weights) <= 10 ** 3
    assert all(1 <= w <= 10 ** 5 for w in weights)

    most_expensive = [[0]*(capacity+1) for _ in range(len(weights)+1)]
    for i in range(1, len(weights)+1):
        for j in range(1, capacity+1):
            most_expensive[i][j] = most_expensive[i-1][j]
            if j >= weights[i-1]:
                pretend = max(
                    most_expensive[i][j],
                    most_expensive[i-1][j-weights[i-1]] + weights[i-1],
                )
                if pretend <= capacity:
                    most_expensive[i][j] = pretend

    return most_expensive[-1][-1]


if __name__ == '__main__':
    # On the first line Input two integers defines capacity and numbers of bars
    # On the next line input weights of the each gold bar
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n
    val = maximum_gold(input_capacity, input_weights)
    # Outputs the maximum weight of gold that fits into a knapsack of capacity 𝑊.
    print(val)
