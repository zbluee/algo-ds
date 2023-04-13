
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

    def pop(self):
        if self.is_empty():
            raise IndexError("remove from empty stack")

        removed = self.list.pop()
        self.length -= 1
        return removed

    def peek(self):
        if self.is_empty():
            raise IndexError("empty stack")

        return self.list[self.length - 1]

    def clear(self) -> None:
        if not self.is_empty():
            self.list = []
            self.length = 0


