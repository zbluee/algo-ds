
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

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Remove from empty queue.")

        first_value = self.linkedList.head.data

        if self.linkedList.head == self.linkedList.tail:
            self.linkedList.head = None
            self.linkedList.tail = None
            self.linkedList.nodes -= 1
            return first_value

        self.linkedList.head = self.linkedList.head.next
        self.linkedList.nodes -= 1
        return first_value

    def peek(self):
        if self.is_empty():
            raise IndexError("The Queue is empty.")
        return self.linkedList.head.data

    def clear(self):
        if not self.is_empty():
            self.linkedList = LinkedList()


