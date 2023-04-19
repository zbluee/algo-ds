
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

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Remove from empty queue.")

        first_value = self.list[self.front]
        self.list[self.front] = None

        # when one element left in the queue, update the front and rare values to their start position
        if self.front == self.rare:
            self.front = -1
            self.rare = -1
        else:
            self.front = (self.front + 1) % self.max_size

        return first_value

    def peek(self):
        if self.is_empty():
            return IndexError("The Queue is empty.")
        return self.list[self.front]

    def clear(self):
        if not self.is_empty():
            self.list = [None] * self.max_size
            self.front = -1
            self.rare = -1

