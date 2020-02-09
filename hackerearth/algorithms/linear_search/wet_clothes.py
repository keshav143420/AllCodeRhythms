class WetClothes:
    def __init__(self):
        self._count = 0
        self._max_gap = 0

    def saved_wet_cloths(self,
                         nmg,
                         intervals,
                         time_to_dry):
        (no_time_intervals,
         _,
         _) = nmg
        for i in range(no_time_intervals - 1):
            self._max_gap = max(self._max_gap, intervals[i + 1] - intervals[i])
        for i in time_to_dry:
            if i <= self._max_gap:
                self._count += 1
        return self._count


if __name__ == "__main__":
    (n, m, g) = (int(i) for i in input().split())
    N = list(int(i) for i in input().split())
    A = list(int(i) for i in input().split())
    wc = WetClothes()
    result = wc.saved_wet_cloths((n, m, g), N, A)
    print(result)
