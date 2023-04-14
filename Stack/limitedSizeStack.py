
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

    def pop(self):
        if self.is_empty():
            raise IndexError("Remove form empty stack.")

        return self.list.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("The stack is empty.")

        return self.list[-1]

    def clear(self) -> None:
        if not self.is_empty():
            self.list = []


