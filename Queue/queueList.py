
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


q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.is_empty())
print([v for v in q], len(q))
