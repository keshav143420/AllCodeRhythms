class RootOfTheProblem:

    def __init__(self):
        self.root = 0

    def get_the_root(self, arr):
        left_sum = 0
        right_sum = 0
        for (left_node, right_node) in arr:
            left_sum += left_node
            right_sum += right_node
        self.root = left_sum - right_sum
        return self.root


if __name__ == '__main__':

    root_of_the_problem = RootOfTheProblem()
    test_cases = int(input())
    for _ in range(test_cases):
        number_of_nodes = int(input())
        tree = []
        for _ in range(number_of_nodes):
            tree.append(list(int(i) for i in input().split()))
        print(root_of_the_problem.get_the_root(tree))
