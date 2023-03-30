
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

    def insert_at_beg(self, data) -> None:
        node = Node(data)
        node.next = self.head
        self.head = node
        self.number_of_nodes += 1

    def insert_at_end(self, data) -> None:
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

    def insert(self, data, index : int) -> None:
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

    def remove_at_beg(self) -> None:
        if self.head is None:
            raise IndexError("remove from empty list")

        self.head = self.head.next
        self.number_of_nodes -= 1

    def remove_at_end(self) -> None:
        if self.head is None:
            raise IndexError("remove from empty list")

        itr = self.head
        while itr.next.next:
            itr = itr.next

        itr.next = None
        self.number_of_nodes -= 1

    def remove(self, index) -> None:
        if self.head is None:
            raise IndexError("remove from empty list")

        if index < 0 or index >= self.number_of_nodes:
            raise IndexError("index out of bound")

        if index == 0:
            self.remove_at_beg()
            return

        if index == self.number_of_nodes - 1:
            self.remove_at_end()
            return

        itr = self.head
        while index - 1 > 0:
            itr = itr.next
            index -= 1

        itr.next = itr.next.next
        self.number_of_nodes -= 1

    def search(self, value):
        itr = self.head
        while itr:
            if itr.data == value:
                return True
            itr = itr.next
        return False

    def clear(self):
        if self.head is not None:
            self.head = None
            self.number_of_nodes = 0

