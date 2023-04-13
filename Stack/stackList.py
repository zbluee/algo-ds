
class Stack:
    def __init__(self):
        self.list = []
        self.length = 0

    def __iter__(self):
        for i in self.list:
            yield i

    def __len__(self):
        return self.length

    def is_empty(self):
        return self.length == 0

    def push(self, value) -> None:
        self.list.append(value)
        self.length += 1


stack = Stack()
stack.push(4)
stack.push(3)
stack.push(2)
stack.push(1)
print([v for v in stack], len(stack))
