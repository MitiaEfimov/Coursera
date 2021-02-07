# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i+1))

        if next in ")]}":
            if len(opening_brackets_stack) == 0:
                return str(i+1)
            last_bracket = opening_brackets_stack.pop()
            if not are_matching(last_bracket.char, next):
                return str(i+1)
    else:
        if len(opening_brackets_stack) != 0:
            return str(opening_brackets_stack[-1].position)
        else:
            out = "Success"
            return out


def main():
    text = input()
    print(find_mismatch(text))


if __name__ == "__main__":
    main()
