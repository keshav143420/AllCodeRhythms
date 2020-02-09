class WetClothesP:
    def __init__(self):
        self.no_completely_wet_clothes = 0
        self.no_time_intervals = 0
        self.limit_to_dry = 0
        self.time_intervals = []
        self.dry_rate = []


class WetClothes:
    def __init__(self):
        self._count = 0
        self._max_gap = 0

    def saved_wet_cloths(self, w):
        for i in range(w.no_completely_wet_clothes - 1):
            delta = w.time_intervals[i + 1] - w.time_intervals[i]
            self._max_gap = max(self._max_gap, delta)
        for i in w.dry_rate:
            if i <= self._max_gap:
                self._count += 1
        return self._count


if __name__ == "__main__":
    wcp = WetClothesP()
    (wcp.no_completely_wet_clothes,
     wcp.no_time_intervals,
     wcp.limit_to_dry) = (int(i) for i in input().split())
    wcp.time_intervals = list(int(i) for i in input().split())
    wcp.dry_rate = list(int(i) for i in input().split())
    wc = WetClothes()
    result = wc.saved_wet_cloths(wcp)
    print(result)
