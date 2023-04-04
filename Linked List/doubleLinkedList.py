
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.number_of_nodes = 0

    def __iter__(self):
        itr = self.head
        while itr:
            yield itr.data
            itr = itr.next

    def __len__(self) -> int:
        return self.number_of_nodes

    def reverse(self):
        itr = self.tail
        while itr:
            yield itr.data
            itr = itr.prev

    def insert_at_beg(self, data) -> None:
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
            self.number_of_nodes += 1
            return

        node.next = self.head
        self.head.prev = node
        self.head = node
        self.number_of_nodes += 1

    def insert_at_end(self, data) -> None:
        if self.head is None:
            self.insert_at_beg(data)
            return

        node = Node(data)
        node.prev = self.tail
        self.tail.next = node
        self.tail = node
        self.number_of_nodes += 1

    def insert(self, data, index : int) -> None:
        if index == 0:
            self.insert_at_beg(data)
            return

        if index < 0 or index >= self.number_of_nodes:
            raise IndexError("index out of bound")

        node = Node(data)
        itr = self.head
        while index - 1 > 0:
            itr = itr.next
            index -= 1

        node.next = itr.next
        node.prev = itr
        itr.next.prev = node
        itr.next = node
        self.number_of_nodes += 1

    def remove_at_beg(self) -> None:
        if self.head is None:
            raise IndexError("remove from empty list")

        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.number_of_nodes -= 1
            return

        self.head = self.head.next
        self.head.prev = None
        self.number_of_nodes -= 1


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_at_beg(4)
    dll.insert_at_beg(3)
    dll.insert_at_beg(2)
    dll.insert_at_beg(1)
    dll.insert_at_end(5)
    dll.insert_at_end(6)
    dll.insert(0, 0)
    dll.insert(2.5, 3)
    dll.remove_at_beg()
    dll.remove_at_beg()
    dll.remove_at_beg()
    dll.remove_at_beg()
    print([data for data in dll], len(dll))

