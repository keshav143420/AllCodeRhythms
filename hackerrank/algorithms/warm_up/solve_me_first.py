class SolveMeFirst:
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b

    def solve_me_first(self):
        return self.num1 + self.num2


if __name__ == '__main__':
    num1 = int(input())
    num2 = int(input())
    smf = SolveMeFirst(num1, num2)
    result = smf.solve_me_first()
    print(result)
