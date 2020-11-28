class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class IHateEvenSubArrays:
    def __init__(self):
        self.result = ""
        self.stack = Stack()

    def minimize_size_by_removing_even_sub_arrays(self, s):
        self.result = ""
        self.stack = Stack()
        i = 0
        while i < len(s):
            if self.stack.is_empty():
                self.stack.push(s[i])
            elif s[i] == self.stack.peek():
                self.stack.pop()
            else:
                self.stack.push(s[i])
            i += 1
        if self.stack.size() == 0:
            self.result = 'KHALI'
        else:
            self.result = ''.join(self.stack.items)
        return self.result


if __name__ == '__main__':
    T = int(input())
    ihes = IHateEvenSubArrays()
    for _ in range(T):
        print(ihes.minimize_size_by_removing_even_sub_arrays(input()))
