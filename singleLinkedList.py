
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.number_of_nodes = 0

    def __iter__(self):
        itr = self.head
        while itr:
            yield itr.data
            itr = itr.next

    def __len__(self) -> int:
        return self.number_of_nodes

    def insert_at_beg(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.number_of_nodes += 1

    def insert_at_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.number_of_nodes += 1
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = node
        self.number_of_nodes += 1

    def insert(self, data, index : int):
        if self.head is None or index == 0:
            self.insert_at_beg(data)
            return

        if index < 0 or index >= self.number_of_nodes:
            raise IndexError("index out of bound")

        node = Node(data)
        itr = self.head
        while index - 1 > 0:
            itr = itr.next
            index -= 1

        temp_node = itr.next
        itr.next = node
        node.next = temp_node
        self.number_of_nodes += 1


sll1 = SLinkedList()
sll1.insert_at_beg(2)
sll1.insert_at_beg(1)
sll1.insert_at_beg(0)
sll1.insert_at_end(3)
sll1.insert_at_end(5)
sll1.insert(4, 4)
sll1.insert(6, 5)
print([data for data in sll1 ], len(sll1))
