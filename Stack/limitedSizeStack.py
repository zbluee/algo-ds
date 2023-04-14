
class Stack:
    def __init__(self, max_size : int):
        self.max_size = max_size
        self.list = []

    def __iter__(self):
        for val in self.list:
            yield val

    def __len__(self):
        return len(self.list)

    def is_empty(self) -> bool:
        return len(self.list) == 0

    def is_full(self) -> bool:
        return len(self.list) == self.max_size

    def push(self, value) -> None:
        if self.is_full():
            raise IndexError("The stack is full.")

        self.list.append(value)


stack = Stack(5)
stack.push(4)
stack.push(3)
stack.push(3)
stack.push(3)
stack.push(2)
stack.push(3)
print([v for v in stack], len(stack))
