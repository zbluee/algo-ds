from collections import deque

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

    def preorder_traversal(self) -> list:
        """
        Traverses the tree in in-order (root, left, right) and returns a list of nodes visited.

        """
        result = []
        stack = [self.root] if self.root else []
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
        result = []
        stack = []
        current_node = self.root
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
        Traverses the tree in post-order (left, right, root) and returns a list of nodes visited.

        """
        result = []
        stack = []
        current_node = self.root
        last_visited = None
        while stack or current_node:
            if current_node:
                stack.append(current_node)
                current_node = current_node.left
            else:
                peek = stack[-1]
                if peek.right and peek.right != last_visited:
                    current_node = peek.right
                else:
                    last_visited = stack.pop()
                    result.append(last_visited.data)

        return result

    def levelorder_traversal(self) -> list:
        """
        Traverses the tree in level-order and returns a list of nodes visited.

        """
        if not self.root:
            return []

        result = []
        queue = deque([self.root])
        while queue:
            current_node = queue.popleft()
            result.append(current_node.data)

            if current_node.left is not None:
                queue.append(current_node.left)

            if current_node.right is not None:
                queue.append(current_node.right)

        return result

    def insert(self, data) -> None:
        """
        Inserts a new node with the given data into the tree.

        Args:
            data: The data to be stored in the new node.
        """
        node = TreeNode(data)
        if not self.root:
            self.root = node
            self.nodes += 1
            return

        queue = deque([self.root])
        while queue:
            current_node = queue.popleft()

            if current_node.left is None:
                current_node.left = node
                self.nodes += 1
                return

            if current_node.right is None:
                current_node.right = node
                self.nodes += 1
                return

            queue.append(current_node.left)
            queue.append(current_node.right)

    def search(self, data) -> bool:
        """
        Searches for the node containing the given data in the binary tree.

        Args:
            data: The data to search for.

        Returns:
            True if the data is found in the tree, False otherwise.
        """
        if not self.root:
            return False

        queue = deque([self.root])
        while queue:
            current_node = queue.popleft()

            if current_node.data == data:
                return True

            if current_node.left is not None:
                queue.append(current_node.left)

            if current_node.right is not None:
                queue.append(current_node.right)

        return False

    def get_deepest_node(self) -> TreeNode:
        """
        Returns the deepest leaf node in the binary tree rooted at the given node.

         """
        if not self.root:
            return

        queue = deque([self.root])
        while queue:
            current_node = queue.popleft()
            if current_node.left is not None:
                queue.append(current_node.left)

            if current_node.right is not None:
                queue.append(current_node.right)

        return current_node

    def delete_deepest_node(self) -> None:
        """
        Deletes the deepest node in the binary tree rooted at the given node.

        Returns:
            None.
        """
        if not self.root:
            return
        if not self.root.left and not self.root.right:
            self.root = None
            self.nodes -= 1
            return

        queue = deque([self.root])
        deepest_node = self.get_deepest_node()

        while queue:
            current_node = queue.popleft()
            if current_node is deepest_node:
                current_node = None
                self.nodes -= 1
                return

            if current_node.right and current_node.right is deepest_node:
                current_node.right = None
                self.nodes -= 1
                return

            if current_node.left and current_node.left is deepest_node:
                current_node.left = None
                self.nodes -= 1
                return

            queue.append(current_node.right)
            queue.append(current_node.left)

    def delete(self, data_to_delete) -> bool:
        """
        Deletes the node with the given data from the tree, if it exists.

        Args:
            data: The data to be deleted.

        Returns:
            True if the node was found and deleted, False otherwise.
        """
        if not self.root:
            return False

        if self.root.data == data_to_delete:
            if not self.root.left and not self.root.right:
                self.root = None
                self.nodes -= 1
            else:
                self.root.data = self.get_deepest_node().data
                self.delete_deepest_node()
            return True

        queue = deque([self.root])
        while queue:
            current_node = queue.popleft()
            if current_node.data == data_to_delete:
                current_node.data = self.get_deepest_node().data
                self.delete_deepest_node()
                return

            if current_node.left and current_node.left.data == data_to_delete:
                if not current_node.left and not current_node.right:
                    current_node.left = None
                    self.nodes -= 1
                else:
                    current_node.left.data = self.get_deepest_node().data
                    self.delete_deepest_node()

                return True

            if current_node.right and current_node.right.data == data_to_delete:
                if not current_node.left and not current_node.right:
                    current_node.right = None
                    self.nodes -= 1
                else:
                    current_node.right.data = self.get_deepest_node().data
                    self.delete_deepest_node()

                return True

            if current_node.left is not None:
                queue.append(current_node.left)

            if current_node.right is not None:
                queue.append(current_node.right)

        return False

    def height(self) -> int:
        """
        Returns the height of the binary tree.
        """
        def height_helper(root):
            if not root:
                return 0
            return 1 + max(height_helper(root.left), height_helper(root.right))

        return height_helper(self.root)

    def clear(self) -> None:
        """
        Deletes the BinaryTree.
        """
        if self.root is not None:
            self.root = None
            self.left = None
            self.right = None
            self.nodes = 0


