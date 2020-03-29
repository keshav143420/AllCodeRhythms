def counter(a, b):
    temp = a + b
    lnt = len(temp)
    temp.sort()
    ca = []
    cb = []
    count_a = 0
    count_b = 0
    for i, _ in enumerate(a):
        j = temp.index(a[i])
        ca.append(lnt - len(a) - j + i)
    for i, _ in enumerate(b):
        j = temp.index(b[i])
        cb.append(lnt - len(b) - j + i)

    for i in range(len(ca) - 1):
        for j in range(i + 1, len(ca)):
            count_a += ca[j] * (ca[i] - ca[j])

    for i in range(len(cb) - 1):
        for j in range(i + 1, len(cb)):
            count_b += cb[j] * (cb[i] - cb[j])

    total = count_a + count_b
    return total


class HolidaySeason:

    def __init__(self) -> None:
        self.final = 0

    def num_of_sub_sequences(self, num_ele_in_seq, sequence):
        list_seq = list(sequence)
        my_dictionary = {}
        for i in range(num_ele_in_seq):
            if list_seq[i] in my_dictionary:
                my_dictionary[list_seq[i]].append(i)
            else:
                my_dictionary[list_seq[i]] = [i]
        self.final = 0
        run = list(my_dictionary.keys())
        for i in range(len(run) - 1):
            for j in range(i + 1, len(run)):
                self.final += counter(my_dictionary[run[i]], my_dictionary[run[j]])
        for x in my_dictionary:
            ln = len(my_dictionary[x])
            if ln >= 4:
                self.final += (ln * (ln - 1) * (ln - 2) * (ln - 3)) // 24
        return self.final


if __name__ == '__main__':
    n = int(input())
    arr = input()
    hs = HolidaySeason()
    result = hs.num_of_sub_sequences(n, arr)
    print(result)
