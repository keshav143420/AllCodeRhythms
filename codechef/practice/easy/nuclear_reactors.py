class NuclearReactor:
    def __init__(self, A, N, K):
        self.A = A
        self.N = N
        self.K = K
        self.result = [0] * self.K

    def get_final_state(self):
        for i in range(self.K):
            self.result[i] = self.A % (self.N + 1)
            self.A = self.A // (self.N + 1)
            if self.A == 0:
                break
        return self.result


if __name__ == '__main__':
    (a, n, k) = list(int(x) for x in input().split())
    nr = NuclearReactor(a, n, k)
    result = nr.get_final_state()
    print(" ".join([str(i) for i in result]))
