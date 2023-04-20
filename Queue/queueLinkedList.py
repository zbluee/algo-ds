
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.nodes = 0


class Queue:
    def __init__(self):
        self.linkedList = LinkedList()

    def __iter__(self):
        itr = self.linkedList.head
        while itr:
            yield itr.data
            itr = itr.next

    def __len__(self):
        return self.linkedList.nodes

    def is_empty(self) -> bool:
        return self.linkedList.head == None

    def enqueue(self, data) -> None:
        node = Node(data)
        if self.is_empty():
            self.linkedList.head = node
            self.linkedList.tail = node
            self.linkedList.nodes += 1
            return

        self.linkedList.tail.next = node
        self.linkedList.tail = node
        self.linkedList.nodes += 1


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print([v for v in q], len(q))
