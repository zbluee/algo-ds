
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class CircularSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.number_of_nodes = 0

    def __iter__(self):
        itr = self.head
        while itr:
            yield itr.data
            if itr.next == self.head:
                break
            itr = itr.next

    def __len__(self) -> int:
        return self.number_of_nodes

    def insert_at_beg(self, data) -> None:
        node = Node(data)
        if self.head is None:
            node.next = node
            self.head = node
            self.tail = node
            self.number_of_nodes += 1
            return

        node.next = self.head
        self.head = node
        self.tail.next = node
        self.number_of_nodes += 1

    def insert_at_end(self, data) -> None:
        if self.head is None:
            self.insert_at_beg(data)
            return

        node = Node(data)

        self.tail.next = node
        node.next = self.head
        self.tail = node
        self.number_of_nodes += 1

    def insert(self, data, index : int) -> None:
        if index == 0:
            self.insert_at_beg(data)
            return

        if index < 0 or index >= self.number_of_nodes:
            raise IndexError("index out of boun")

        node = Node(data)
        itr = self.head
        while index - 1 > 0:
            itr = itr.next
            index -= 1

        node.next = itr.next
        itr.next = node
        self.number_of_nodes += 1


csll = CircularSLinkedList()
csll.insert_at_beg(4)
csll.insert_at_beg(3)
csll.insert_at_end(5)
csll.insert(3.5, 1)
print([data for data in csll], len(csll))


