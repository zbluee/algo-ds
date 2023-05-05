
class BinaryTree:
    """
    A binary tree implemented using a Python list.

    Args:
    - max_size (int): The maximum size of the binary tree.

    Attributes:
    - root (list): A list representing the binary tree.
    - last_visited_index (int): The index of the last visited node in the binary tree.
    - max_size (int): The maximum size of the binary tree.

    Notes:
    - The root node is stored at index i = 1 of the list. The left child of a node at index i is stored at index 2i, and the right child of a node at index i is stored at index 2i+1.
    """
    def __init__(self, max_size : int):
        self.root = [None] * max_size
        self.last_visited_index = 0
        self.max_size = max_size

    def __len__(self):
        """
        Returns the number of nodes in the binary tree.
        """
        return self.last_visited_index

    def is_empty(self) -> bool:
        """
        Checks if the binary tree is empty.

        """
        return self.last_visited_index == 0

    def insert(self, data):
        """
        Inserts a new node with value `data` into the binary tree.

        """
        if self.last_visited_index + 1 == self.max_size:
            return IndexError("Binary tree is full.")

        self.last_visited_index += 1
        self.root[self.last_visited_index] = data
        return True

    def get_root(self):
        """
        Returns the root node of the binary tree.

        """
        if self.is_empty():
            return IndexError("Binary tree is empty.")
        return self.root[1]

    def contains(self, data) -> bool:
        """
        Searches the binary tree for a node with value `data`.
        """
        if self.is_empty():
            return False

        for i in range(1, self.last_visited_index + 1):
            if self.root[i] == data:
                return True
        return False

    def preorder_traversal(self) -> list:
        """
        Traverses the tree in in-order (root, left , right) and returns a list of nodes visited.

        """
        index, result = 1, []

        def preorder_helper(index):
            if index > self.last_visited_index:
                return
            result.append(self.root[index])
            preorder_helper(index * 2)
            preorder_helper(index * 2 + 1)

        preorder_helper(index)
        return result

    def inorder_traversal(self) -> list:
        """
        Traverses the tree in in-order (left, root, right) and returns a list of nodes visited.

        """
        index, result = 1, []

        def inorder_helper(index):
            if index > self.last_visited_index:
                return

            inorder_helper(index * 2)
            result.append(self.root[index])
            inorder_helper(index * 2 + 1)

        inorder_helper(index)
        return result

    def postorder_traversal(self) -> list:
        """
        Traverses the tree in in-order (left, right, root) and returns a list of nodes visited.

        """
        index, result = 1, []

        def postorder_helper(index):
            if index > self.last_visited_index:
                return

            postorder_helper(index * 2)
            postorder_helper(index * 2 + 1)
            result.append(self.root[index])

        postorder_helper(index)
        return result

    def levelorder_traversal(self) -> list:
        """
        Traverses the tree in level-order and returns a list of nodes visited.

        """
        result = []
        for i in range(1, self.last_visited_index + 1):
            result.append(self.root[i])

        return result

    def get_deepest_node(self):
        """
        Returns the deepest leaf node in the binary tree rooted

        """
        if self.is_empty():
            return IndexError("Binary Tree is empty.")
        return self.root[self.last_visited_index]

    def delete_deepest_node(self) -> bool:
        """
        Deletes the deepest node in the binary tree.

        """
        if self.is_empty():
            return IndexError("Binary Tree is empty.")

        self.root[self.last_visited_index] = None
        self.last_visited_index -= 1
        return True

    def delete(self, data) -> bool:
        """
        Deletes the node with the given data from the tree, if it exists.

        """
        if self.is_empty():
            return IndexError("Binary Tree is empty")

        for i in range(1, self.last_visited_index + 1):
            if self.root[i] == data:
                self.root[i] = self.get_deepest_node()
                self.delete_deepest_node()
                return True

        return False

    def clear(self) -> None:
        """
        Clears the binary tree, removing all nodes.

        """
        self.root = [None] * self.max_size
        self.last_visited_index = 0


