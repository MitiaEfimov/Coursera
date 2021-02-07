# python3
"""Minimum number to transform one string into other one"""


def print_on(first_string, second_string, matrix):
    """Function for printing both string with edit distance

    Works beauty with first string length less then 11

    """
    first = ["_", "_"]+[0]*len(first_string)
    for i in range(2, len(first)):
        first[i] = first_string[i-2]
    second = ["_"] + [0]*len(second_string)
    for i in range(1, len(second)):
        second[i] = second_string[i-1]
    print(*first_string, sep="  ")
    for i in range(len(matrix)):
        print(second_string[i], matrix[i])


def edit_distance(first_string, second_string):
    """Compute minimum operations for transform one string into other one.

    There is algorithm:
    1)First is needed to do is define four operations.
    - insertions  -  situation when second string has bigger length then first length.
    Insertions is adding one symbol to first string operations.
    - deletions  -  situation when second string has length less them first.
    Deletions is removing one symbol from first string operations.
    - mismatch  -  situation when first and second strings lengths are equal.
    Mismatch is removing both symbols from first and second string.
    - match  -  situations when symbols from first and second strings are equal.
    Match is not operations, it is just tell that there is nothing to do with current symbols.

    2)To compute the hole edit distance N*M, we should compute edit distance for
    (N-1)*M (deletion operation), N*(M-1) (insertion operation), (N-1)*(M-1)
     (match if equal and mismatch, if not equal operations) edits distance.\
     Since we are looking fo minimum transform number we choose the smallest of this three ways.

    """
    distance = [[0]*(len(first_string)+1) for _ in range(len(second_string)+1)]
    for i in range(len(second_string)+1):
        if i == 0:
            # insertion operation for all first line
            distance[i] = list(range(len(first_string)+1))
            continue
        for j in range(len(first_string)+1):
            if j == 0:
                # deletion operation for first column first element
                distance[i][j] = distance[i-1][j] + 1
                continue
            insertion = 1 + distance[i][j-1]
            deletion = 1 + distance[i-1][j]
            mismatch = 1 + distance[i-1][j-1]
            match = distance[i-1][j-1]
            if first_string[j-1] == second_string[i-1]:
                distance[i][j] = min(insertion, deletion, match)
            elif first_string[j-1] != second_string[i-1]:
                distance[i][j] = min(insertion, deletion, mismatch)

    return distance[-1][-1]


if __name__ == "__main__":
    # Input two lines
    # Each of the two lines of the input contains a string 
    # consisting of lower case latin letters.
    print(edit_distance(input(), input()))
