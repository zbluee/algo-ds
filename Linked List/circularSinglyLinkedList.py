
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

    def remove_at_beg(self) -> None:
        if self.head is None:
            raise IndexError("remove from emtpy list")

        if self.number_of_nodes == 1:
            self.head.next = None
            self.head = None
            self.tail = None
            self.number_of_nodes -= 1
            return

        self.head = self.head.next
        self.tail.next = self.head
        self.number_of_nodes -= 1

    def remove_at_end(self) -> None:
        if self.head is None:
            raise IndexError("remove from emtpy list")

        if self.number_of_nodes == 1:
            self.remove_at_beg()
            return

        itr = self.head
        while itr.next.next != self.head:
            itr = itr.next

        itr.next = self.head
        self.tail = itr
        self.number_of_nodes -= 1

    def remove(self, index : int) -> None:
        if index == 0:
            self.remove_at_beg()
            return

        if index == self.number_of_nodes - 1:
            self.remove_at_end()
            return

        if self.head is None:
            raise IndexError("remove from empty list")

        if index < 0 or index >= self.number_of_nodes:
            raise IndexError("index out of bound")

        itr = self.head
        while index - 1 > 0 :
            itr = itr.next
            index -= 1

        itr.next = itr.next.next
        self.number_of_nodes -= 1


    def search(self, value) -> bool:
        if self.head is None:
            return False

        itr = self.head
        while itr:
            if itr.data == value:
                return True
            itr = itr.next

            if itr.next == self.head:
                return False

    def clear(self) -> None:
        if self.head is not None:
            self.head = None
            self.tail.next = None
            self.tail = None
            self.number_of_nodes = 0


# csll = CircularSLinkedList()
#csll.insert_at_beg(4)       [4]
#csll.insert_at_beg(3)       [3, 4]
#csll.insert_at_end(5)       [3, 4, 5]
#csll.insert(3.5, 1)         [3, 3,5, 4, 5]
#csll.remove(0)              [3.5, 4, 5]
#csll.remove(2)              [3.5, 5]
#print(csll.search(4))       True
#print(csll.search(11))      False
#print([data for data in csll], len(csll))


