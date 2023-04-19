
class CircularQueue:
    def __init__(self, max_size):
        self.list = [None] * max_size
        self.max_size = max_size
        self.front = -1
        self.rare = -1

    def __iter__(self):
        for value in self.list:
            yield value

    def is_empty(self) -> bool:
        return self.front == -1 and self.rare == -1

    def is_full(self) -> bool:
        return (self.rare + 1) % self.max_size == self.front

    def enqueue(self, value) -> None:
        if self.is_full():
            raise IndexError("The Queue is full.")

        if self.is_empty():
            self.front = 0
            self.rare = 0

        else:
            self.rare = (self.rare + 1) % self.max_size

        self.list[self.rare] = value


cq = CircularQueue(3)
print(cq.is_empty(), cq.is_full())
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
print(cq.is_empty(), cq.is_full())
print([v for v in cq])
