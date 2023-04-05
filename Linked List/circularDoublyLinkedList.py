
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.prev = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.__number_of_nodes = 0

    def __iter__(self):
        itr = self.head
        while itr:
            yield itr.data
            if itr.next == self.head:
                break
            itr = itr.next

    def __len__(self) -> int:
        return self.__number_of_nodes

    def reverse(self):
        itr = self.tail
        while itr:
            yield itr.data
            if itr.prev == self.tail:
                break
            itr = itr.prev

    def insert_at_beg(self, data) -> None:
        node = Node(data)
        if self.head is None:
            node.next = node
            node.prev = node
            self.head = node
            self.tail = node
            self.__number_of_nodes += 1
            return

        node.next = self.head
        node.prev = self.tail
        self.head.prev = node
        self.head = node
        self.tail.next = node
        self.__number_of_nodes += 1

    def insert_at_end(self, data) -> None:
        if self.head is None:
            self.insert_at_beg(data)
            return

        node = Node(data)
        node.next = self.head
        node.prev = self.tail
        self.tail.next = node
        self.head.prev = node
        self.tail = node
        self.__number_of_nodes += 1

    def insert(self, data, index : int) -> None:
        if index == 0:
            self.insert_at_beg(data)
            return

        if index < 0 or index >= self.__number_of_nodes:
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
        self.__number_of_nodes += 1

    def remove_at_beg(self) -> None:
        if self.head is None:
            raise IndexError("remove from empty list")

        if self.head == self.tail:
            self.head.next = None
            self.head.prev = None
            self.head = None
            self.tail = None
            self.__number_of_nodes -= 1
            return

        self.head = self.head.next
        self.head.prev = self.tail
        self.tail.next = self.head
        self.__number_of_nodes -= 1

    def remove_at_end(self) -> None:
        if self.head == self.tail:
            self.remove_at_beg()
            return

        if self.head is None:
            raise IndexError("remove from empty list")

        self.tail = self.tail.prev
        self.tail.next = self.head
        self.head.prev = self.tail
        self.__number_of_nodes -= 1

    def remove(self, index : int) -> None:
        if index == 0:
            self.remove_at_beg()
            return

        if index == self.__number_of_nodes - 1:
            self.remove_at_end()
            return

        if self.head is None:
            raise IndexError("remove from empty list")

        if index < 0 or index >= self.__number_of_nodes:
            raise IndexError("index out of bound")

        itr = self.head
        while index - 1 > 0:
            itr = itr.next
            index -= 1

        itr.next = itr.next.next
        itr.next.prev = itr
        self.__number_of_nodes -= 1

    def search(self, value) -> bool:
        itr = self.head
        while itr:
            if itr.data == value:
                return True
            if itr.next == self.head:
                break
            itr = itr.next

        return False

    def clear(self) -> None:
        if self.head is not None:

            self.tail.next = None
            itr = self.head

            while itr:
                itr.prev = None
                itr = itr.next

            self.head = None
            self.tail = None
            self.__number_of_nodes = 0
