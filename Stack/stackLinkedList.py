
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


stack = Stack()
stack.push(5)
stack.push(4)
stack.push(3)
print(stack.is_empty())
print([v for v in stack], len(stack))
