## Tree

A tree is a widely used abstract data type that simulates a hierarchical tree structure with a set of linked nodes. Each node in a tree contains a value or data, and zero or more child nodes, which are also trees. The topmost node in a tree is called the root node, and it doesn't have a parent node. 

The tree data structure has a wide range of applications, including representing hierarchical data such as file systems, organization charts, and family trees, as well as algorithms such as binary search trees and heaps.

<center>

## Time and Space Complexity

</center>

### • Binary Tree LinkedList

 A `binary tree` is a tree data structure in which each node has at most two children, referred to as the left child and the right child. The structure of a binary tree is recursive in nature, as each node in the tree may be considered as the root of a subtree that itself is a binary tree.


| Method | Description | Time Complexity | Space Complexity |
| ------ | ----------- | --------------- | ---------------- |
| `create tree` | Initializes an empty binary tree with a root node of `None`. | O(1) | O(1) |
| `length` | Returns the number of nodes in the binary tree. | O(1) | O(1) |
| `preorder_traversal` |Traverses the tree in pre-order (root, left, right) and returns a list of nodes visited. This is done using a stack and adding the root to the stack initially. Each node is visited in the order it is popped off the stack. | O(n) | O(n) |
| `inorder_traversal` |Traverses the tree in in-order (left, root, right) and returns a list of nodes visited. This is done using a stack to keep track of the left children of each node. When a node is visited, its right child is added to the stack. | O(n) | O(n) |
| `postorder_traversal` |Traverses the tree in post-order (left, right, root) and returns a list of nodes visited. This is done using a stack and a variable to keep track of the last node visited. When a node is visited, its right child is added to the stack first. | O(n) | O(n) |
| `levelorder_traversal` |	Traverses the tree in level-order and returns a list of nodes visited. This is done using a queue and adding the root to the queue initially. Each node is visited in the order it is dequeued from the queue. | O(n) | O(n) |
| `insert` | Inserts a new node with the given data into the tree. If the tree is empty, the node becomes the root. Otherwise, the node is added to the first available spot in the tree using a queue to traverse the tree. | O(n)| O(n) |
| `search` |Searches for the node containing the given data in the binary tree. This is done using a queue to traverse the tree. If the node is found, the method returns True. Otherwise, it returns False. | O(n) | O(n) |
| `get_deepest_node` | Returns the deepest leaf node in the binary tree rooted at the given node. This is done using a queue to traverse the tree.| O(n) | O(n) |
| `delete_deepest_node` | Deletes the deepest node in the binary tree rooted at the given node. This is done using a queue to traverse the tree to find the deepest node, and then deleting it. If the tree has only one node, the root is set to None.| O(n) | O(n) |
| `delete` |  method deletes a node with the given data from the binary tree, if it exists. If the root node has the data to be deleted, it is replaced with the deepest node in the tree, which is then deleted. If the data is not found in the root node, the method performs a level-order traversal of the tree to find the node with the data. Once found, the method replaces the node with the deepest node in the tree, which is then deleted. The method returns `True` if the node was found and deleted, and `False` otherwise.| O(n) | O(n) |
| `height` | Returns the number of nodes in the binary tree. | O(n) | O(n) |
| `clear` | Deletes the entire binary tree. | O(1) | O(1) |

<br>

*Note: **n** represents the number of nodes in the tree.*

