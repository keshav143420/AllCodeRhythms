class CarVans:
    def __init__(self):
        self.result = 1

    def maximum_speed(self, car_speeds):
        current_min = car_speeds[0]
        for i in car_speeds[1:]:
            if i <= current_min:
                self.result += 1
                current_min = i
        return self.result


def main():
    test_cases = int(input())
    for _ in range(test_cases):
        _ = int(input())
        car_speeds = list(int(x) for x in input().split())
        cv = CarVans()
        count = cv.maximum_speed(car_speeds)
        print(count)


if __name__ == '__main__':
    main()
