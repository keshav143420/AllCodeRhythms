class Vestigium:

    def __init__(self) -> None:
        self.rows = []
        self.cols = []
        self.row_repeated = 0
        self.col_repeated = 0
        self.trace = 0

    def get_result(self, num, n_arr):
        self.rows = [0] * num
        self.cols = [0] * num
        for i in range(num):
            for j in range(num):
                self.rows[n_arr[i][j] - 1] = self.rows[n_arr[i][j] - 1] + 1
                self.cols[n_arr[j][i] - 1] = self.cols[n_arr[j][i] - 1] + 1
                if i == j:
                    self.trace = self.trace + n_arr[i][j]
            for ii in range(num):
                if self.rows[ii] != 1:
                    self.row_repeated = self.row_repeated + 1
                    break
            for ii in range(num):
                if self.cols[ii] != 1:
                    self.col_repeated = self.col_repeated + 1
                    break
            self.rows = [0] * num
            self.cols = [0] * num
        return self.trace, self.row_repeated, self.col_repeated


if __name__ == '__main__':
    test_cases = int(input())
    for tc in range(test_cases):
        n = int(input())
        arr = []
        for _ in range(n):
            arr.append([int(x) for x in input().split()])
        v = Vestigium()
        result = v.get_result(n, arr)
        print("Case #{}: {} {} {}".format(tc + 1, result[0], result[1], result[2]))
