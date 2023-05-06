
class BSTNode:
    """
    A node in a binary search tree (BST).

    Attributes:
        data: The data stored in the node.
        left: The left child node of the current node.
        right: The right child node of the current node.
    """
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None


class BST:
    """
    A binary search tree (BST) implementation.

    Attributes:
        root: The root node of the BST.
        nodes: The number of nodes in the BST.
    """
    def __init__(self):
        self.root = None
        self.nodes = 0

    def __len__(self):
        return self.nodes

    def get_min_node(self, root = None) -> BSTNode:
        """
        Get the node with the minimum value in the BST.

        """
        current_node = root if root else self.root
        while current_node.left:
            current_node = current_node.left
        return current_node

    def get_max_node(self, root = None) -> BSTNode:
        """
        Get the node with the maximum value in the BST.

        """
        current_node = root if root else self.root
        while current_node.right:
            current_node = current_node.right
        return current_node


