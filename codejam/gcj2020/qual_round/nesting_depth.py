class NestingDepth:

    def __init__(self) -> None:
        self.sol = ''

    def get_nesting_depth(self, str_digits):
        self.sol = ''
        if len(str_digits) == 1:
            self.sol = '(' * int(str_digits) + str_digits + ')' * int(str_digits)

        else:
            for i in range(len(str_digits) - 1):
                if i == 0:
                    self.sol += '(' * int(str_digits[i])

                if int(str_digits[i]) > int(str_digits[i + 1]):
                    self.sol += str_digits[i]
                    self.sol += ')' * (int(str_digits[i]) - int(str_digits[i + 1]))

                if int(str_digits[i]) < int(str_digits[i + 1]):
                    self.sol += str_digits[i]
                    self.sol += '(' * (int(str_digits[i + 1]) - int(str_digits[i]))

                if int(str_digits[i]) == int(str_digits[i + 1]):
                    self.sol += str_digits[i]

            self.sol += str_digits[len(str_digits) - 1]
            self.sol += int(str_digits[len(str_digits) - 1]) * ')'
        return self.sol


if __name__ == '__main__':
    test_cases = int(input())
    np = NestingDepth()
    for test_case in range(test_cases):
        sol = np.get_nesting_depth(input())
        print('Case #{}: {}'.format(test_case + 1, sol))
