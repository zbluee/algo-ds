
class Queue:
    def __init__(self):
        self.list = []
        self.count = 0

    def __iter__(self):
        for value in self.list:
            yield value

    def __len__(self):
        return self.count

    def is_empty(self) -> bool:
        return self.count == 0

    def enqueue(self, value) -> None:
        self.list.append(value)
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Remove from empty queue.")

        remove = self.list.pop(0)
        self.count -= 1
        return remove

    def peek(self):
        if self.is_empty():
            raise IndexError("The Queue is empty.")

        return self.list[0]

    def clear(self) -> None:
        if not self.is_empty():
            self.list = []
            self.count = 0


q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
q.dequeue()
q.clear()
print(q.peek())
print([v for v in q], len(q))
