# python3


def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []

    while n > 0:

        for i in range(n):
            if n-(i+1) > i+1:
                n -= (i+1)
                summands.append(i+1)
            else:
                summands.append(n)
                n = 0
                break

    return summands


if __name__ == '__main__':
    # consists of a single integer 𝑛.
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    # Outputs the maximum number 𝑘 such that 𝑛 can be represented as a sum
    # of 𝑘 pairwise distinct positive integers
    print(len(output_summands))
    # Outputs 𝑘 pairwise distinct positive integers 
    # that sum up to 𝑛 
    print(*output_summands)
