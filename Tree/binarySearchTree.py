from collections import deque

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

    def insert(self, data):
        new_node = BSTNode(data)
        if not self.root:
            self.root = new_node
            self.nodes += 1
            return

        parent_node = None
        current_node = self.root
        while current_node:
            parent_node = current_node
            if data <= current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right


        if data <= parent_node.data:
            parent_node.left = new_node
        else:
            parent_node.right = new_node

        self.nodes += 1

    def preorder_traversal(self) -> list:
        """
        Traverses the tree in in-order (root, left, right) and returns a list of nodes visited.

        """
        stack = [self.root] if self.root else []
        result = []
        while stack:
            current_node = stack.pop()
            result.append(current_node.data)
            if current_node.right:
                stack.append(current_node.right)

            if current_node.left:
                stack.append(current_node.left)

        return result

    def inorder_traversal(self) -> list:
        """
        Traverses the tree in in-order (left, root, right) and returns a list of nodes visited.

        """
        stack = []
        current_node = self.root
        result = []
        while stack or current_node:
            while current_node:
                stack.append(current_node)
                current_node = current_node.left

            current_node = stack.pop()
            result.append(current_node.data)
            current_node = current_node.right

        return result

    def postorder_traversal(self) -> list:
        """
        Traverses the tree in in-order (left, right, root) and returns a list of nodes visited.

        """
        stack = []
        current_node = self.root
        last_visited_node = None
        result = []
        while stack or current_node:
            if current_node:
                stack.append(current_node)
                current_node = current_node.left
            else:
                peek = stack[-1]
                if peek.right and peek.right != last_visited_node:
                    current_node = peek.right
                else:
                    last_visited_node = stack.pop()
                    result.append(last_visited_node.data)

        return result

    def levelorder_traversal(self) -> list:
        """
        Traverses the tree in level-order and returns a list of nodes visited.

        """
        if not self.root:
            return []

        queue = deque([self.root])
        result = []
        while queue:
            current_node = queue.popleft()
            result.append(current_node.data)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        return result


bst = BST()
bst.insert(80)
bst.insert(60)
bst.insert(100)
bst.insert(40)
bst.insert(70)
bst.insert(30)
bst.insert(50)
bst.insert(120)
bst.insert(90)
print("preorder\n")
print(bst.preorder_traversal())
print("\ninorder\n")
print(bst.inorder_traversal())
print("\npostorder\n")
print(bst.postorder_traversal())
print("\nlevelorder\n")
print(bst.levelorder_traversal())
