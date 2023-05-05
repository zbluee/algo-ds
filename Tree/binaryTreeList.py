
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

        Returns:
        --------
        bool
            True if the binary tree is empty, False otherwise.

        """
        return self.last_visited_index == 0

    def insert(self, data):
        """
        Inserts a new node with value `val` into the binary tree.

        Parameters:
        -----------
        data : Any
            The value to be inserted into the tree.

        Returns:
        --------
        bool
            True if the insertion is successful, False if the tree is full.

        """
        if self.last_visited_index  >= self.max_size:
            return IndexError("it's on maximum capcity.")

        self.last_visited_index += 1
        self.root[self.last_visited_index] = data
        return True




