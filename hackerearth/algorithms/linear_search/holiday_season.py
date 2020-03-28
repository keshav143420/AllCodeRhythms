class HolidaySeason:

    def __init__(self) -> None:
        self.count = 0

    def num_of_sub_sequences(self, num_ele_in_seq, sequence):
        self.count = 0
        if num_ele_in_seq < 4:
            self.count = 0
        else:
            for a in range(0, num_ele_in_seq - 3):
                for b in range(a + 1, num_ele_in_seq - 2):
                    self.compare_right_part(a, b, num_ele_in_seq, sequence)
        return self.count

    def compare_right_part(self, a, b, num_ele_in_seq, sequence):
        for c in range(b + 1, num_ele_in_seq - 1):
            for d in range(c + 1, num_ele_in_seq):
                if sequence[a] == sequence[c] and sequence[b] == sequence[d]:
                    self.count = self.count + 1


if __name__ == '__main__':
    n = int(input())
    arr = input()
    hs = HolidaySeason()
    result = hs.num_of_sub_sequences(n, arr)
    print(result)
