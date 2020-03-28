class MonkTakesAWalk:
    def __init__(self):
        self.bad_labels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

    def number_of_not_good_trees(self, trees):
        not_good_trees = 0
        for tree_label in trees:
            if tree_label in self.bad_labels:
                not_good_trees = not_good_trees + 1
        return not_good_trees


if __name__ == "__main__":
    monk_takes_a_walk = MonkTakesAWalk()
    total_test_cases = input()
    for test_case in range(int(total_test_cases)):
        print(monk_takes_a_walk.number_of_not_good_trees(input()))
