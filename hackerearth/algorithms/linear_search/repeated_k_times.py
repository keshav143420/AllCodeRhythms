class RepeatedKTimes:

    def __init__(self) -> None:
        self.num_count_dict = {}

    def smallest_k_times_repeated_number(self, nums, limit):
        self.__get_number_count_dict__(nums)

        for num_count in sorted(self.num_count_dict):
            if self.num_count_dict[num_count] == limit:
                return num_count
        return 0

    def __get_number_count_dict__(self, nums):
        for i in nums:
            if i in self.num_count_dict:
                self.num_count_dict[i] = self.num_count_dict[i] + 1
            else:
                self.num_count_dict[i] = 1


if __name__ == '__main__':
    rkt = RepeatedKTimes()
    n = int(input())
    # arr = [2, 2, 3, 1, 1]
    arr = [int(x) for x in input().split(' ')]
    # k = 2
    k = int(input())
    print(rkt.smallest_k_times_repeated_number(arr, k))
