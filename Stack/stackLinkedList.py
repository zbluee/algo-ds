
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.nodes = 0


class Stack:
    def __init__(self):
        self.linkedList = LinkedList()

    def __iter__(self):
        itr = self.linkedList.head
        while itr:
            yield itr.data
            itr = itr.next

    def __len__(self):
        return self.linkedList.nodes

    def is_empty(self):
        return self.linkedList.head == None

    def push(self, data) -> None:
        node = Node(data)
        node.next = self.linkedList.head
        self.linkedList.head = node
        self.linkedList.nodes += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Remove from empty stack.")

        removed = self.linkedList.head.data
        self.linkedList.head = self.linkedList.head.next
        self.linkedList.nodes -= 1
        return removed

    def peek(self):
        if self.is_empty():
            raise IndexError("Empty Stack")

        return self.linkedList.head.data

    def clear(self) -> None:
        if not self.is_empty():
            self.linkedList.head = None
            self.linkedList.nodes = 0

