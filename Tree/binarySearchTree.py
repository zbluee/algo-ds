
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


