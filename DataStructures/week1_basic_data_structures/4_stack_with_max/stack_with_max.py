#python3
import sys


class StackWithMax(object):
    """
    Artificial stack.
    Initialised with empty list "__stack" and max number "max"(default None)

    Push(a) - append tuple(a, max_number)
    Pop() - pop from "__stack" end
    Max() - return "max_number" from last element in "__stack"
    """
    def __init__(self):
        self.__stack = []
        self.max = None

    def Push(self, a):
        """
        Function compare "a" with actual max number(if it exists) and appends tuple(a, max_number) to "__stack"
        :param a: integer
        """
        if not self.max or a > self.max:
            self.max = a
            a = (a, a)
            self.__stack.append(a)
        else:
            a = (a, self.max)
            self.__stack.append(a)

    def Pop(self):
        """
        Function that remove last element from "__stack", check removed element wasn't "max_number", if it was,
        upgrades "max_number" with last element in "__stack" or default.
        """
        assert(len(self.__stack))
        item = self.__stack.pop()
        if self.max == item[1] and self.__stack:
            self.max = self.__stack[-1][1]
        elif self.max == item[1] and not self.__stack:
            self.max = None

    def Max(self):
        """
        Function return "max_number" from last element in "__stack"
        Therefore last item initialised with actual max_number it always right.
        :return:
        """
        assert(len(self.__stack))
        return self.__stack[-1][1]


def simulating_implemented(queries):
    stack = StackWithMax()
    result = []

    for query in queries:
        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            result.append(stack.Max())
        else:
            assert(0)
    return result


def main():
    """
    Function iterates throw all user inputs and do stuff:
     - Push: append to stack tuple(number, max_number)
     - Pop: pop from stack
     - Max: return max_number from last item in stack
    :return:
    """
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)


if __name__ == '__main__':
    main()
