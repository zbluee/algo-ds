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

    def contains(self, data) -> bool:
        """
        Searches for the node containing the given data in the binary tree and it return True if it exists else false."

        """
        if not self.root:
            return False

        current_node = self.root
        while current_node:
            if data == current_node.data:
                return True
            if data <= current_node.data:
                current_node = current_node.left

            else:
                current_node = current_node.right

        return False

    def delete(self, data):
        """
        Deletes the node with the given data from the tree, if it exists.

        """
        if not self.root:
            return

        def delete_helper(root, data):
            if not root:
                return
            elif data < root.data:
                root.left = delete_helper(root.left, data)
            elif data > root.data:
                root.right = delete_helper(root.right, data)
            else:
                if root.left is None:
                    temp = root.right
                    root.right = None
                    self.nodes -= 1
                    return temp
                if root.right is None:
                    temp = temp.left
                    root.left = None
                    self.nodes -= 1
                    return temp

                min_node = self.get_min_node(root.right)
                root.data = min_node.data
                root.right = delete_helper(root.right, min_node.data)

            return root

        return delete_helper(self.root, data)

    def height(self) -> int:
        if not self.root:
            return 0

        def height_helper(root):
            if not root:
                return 0
            return 1 + max(height_helper(root.left), height_helper(root.right))

        return height_helper(self.root)

    def clear(self) -> None:
        self.root = None
        self.root.left = None
        self.root.right = None

