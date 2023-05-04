
class TreeNode:
    """
    A node in a binary tree.

    Attributes:
        data: The data stored in the node.
        left: The left child of the node.
        right: The right child of the node.
    """
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    """
    A binary tree data structure.

    Attributes:
        root: The root node of the tree.
        nodes: The total number of nodes in the tree.
    """
    def __init__(self):
        self.root = None
        self.nodes = 0

    def __len__(self):
        """
        Returns the total number of nodes in the tree.
        """
        return self.nodes

