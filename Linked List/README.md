## LinkedList
A linked list is a data structure that consists of a sequence of nodes, where each node contains a data value and a reference (or pointer) to the next node in the sequence. The first node is called the head, and the last node is called the tail. Linked lists can be singly-linked, meaning that each node has a reference to the next node but not the previous one, or doubly-linked, where each node has references to both the next and previous nodes. They can be used to implement various abstract data types such as stacks, queues, and associative arrays. One of the benefits of linked lists is that they allow efficient insertion and deletion of elements at any point in the list, although accessing elements in the middle of the list can be slower compared to arrays.

<center>

## Time and Space Complexity

</center>


### • Singly Linked List 
This is an implementation of a singly linked list. A linked list is a data structure that consists of nodes, where each node has a reference to the next node in the list. In this implementation, each node has a data attribute and a next attribute that points to the next node in the list.
| Operation | Description | Time Complexity | Space Complexity |
| ------ | ----------- | -------------- | ---------------- |
| `Insert at beg` | Inserts a new node at the beginning of the linked list | `O(1)` | `O(1)` |
| `Insert at end` | Inserts a new node at the end of the linked list | `O(1)` | `O(1)` |
| `Insert` | Inserts a new node at the specified index in the linked list | `O(n)` | `O(1)` |
| `Remove at beg` | Removes the node at the beginning of the linked list | `O(1)` | `O(1)` |
| `Remove at end` | Removes the node at the end of the linked list | `O(n)` | `O(1)` |
| `Remove` | Removes the node at the specified index in the linked list | `O(n)` | `O(1)` |
| `Search` | Searches for a node with the specified value in the linked list | `O(n)` | `O(1)` |
| `Length` | Returns the number of nodes in the list | `O(1)` | `O(1)` |
| `Clear` | Removes all nodes from the linked list | `O(1)` | `O(1)` |


<br>

### • Circular Singly Linked List
This is an implementation of a circular singly linked list, a data structure where each node has a data attribute and a next attribute that points to the next node in the list, and the last node points back to the head, creating a loop.
| Operation | Description | Time Complexity | Space Complexity |
| ------ | ----------- | -------------- | ---------------- |
| `Insert at beg` | Inserts a new node at the beginning of the linked list | `O(1)` | `O(1)` |
| `Insert at end` | Inserts a new node at the end of the linked list | `O(1)` | `O(1)` |
| `Insert` | Inserts a new node at the specified index in the linked list | `O(n)` | `O(1)` |
| `Remove at beg` | Removes the node at the beginning of the linked list | `O(1)` | `O(1)` |
| `Remove at end` | Removes the node at the end of the linked list | `O(n)` | `O(1)` |
| `Remove` | Removes the node at the specified index in the linked list | `O(n)` | `O(1)` |
| `Search` | Searches for a node with the specified value in the linked list | `O(n)` | `O(1)` |
| `Length` | Returns the number of nodes in the list | `O(1)` | `O(1)` |
| `Clear` | Removes all nodes from the linked list | `O(1)` | `O(1)` |

<br>

### • Doubly Linked List
This is an implementation of a doubly linked list in Python. The doubly linked list is a type of linked list where each node has a pointer to both the next and previous node in the list, allowing for efficient traversal in both directions.
| Operation | Description | Time Complexity | Space Complexity |
| ------ | ----------- | -------------- | ---------------- |
| `Insert at beg` | Inserts a new node at the beginning of the linked list | `O(1)` | `O(1)` |
| `Insert at end` | Inserts a new node at the end of the linked list | `O(1)` | `O(1)` |
| `Insert` | Inserts a new node at the specified index in the linked list | `O(n)` | `O(1)` |
| `Remove at beg` | Removes the node at the beginning of the linked list | `O(1)` | `O(1)` |
| `Remove at end` | Removes the node at the end of the linked list | `O(1)` | `O(1)` |
| `Remove` | Removes the node at the specified index in the linked list | `O(n)` | `O(1)` |
| `Reverse` | Returns an iterator that traverses the list in reverse order | `O(n)` | `O(1)` |
| `Search` | Searches for a node with the specified value in the linked list | `O(n)` | `O(1)` |
| `Length` | Returns the number of nodes in the list | `O(1)` | `O(1)` |
| `Clear` | Removes all nodes from the linked list | `O(1)` | `O(1)` |

<br>

### • Circular Doubly Linked List
This is an implementation of a circular doubly linked list, a data structure where each node contains a reference to the next and previous nodes in the list. The last node in the list points to the first node, creating a circular structure. This implementation allows insertion and removal of nodes at the beginning, end, or a specified index of the list. It also provides a search function to check if a value exists in the list and a clear function to remove all nodes in the list.
| Operation | Description | Time Complexity | Space Complexity |
| ------ | ----------- | -------------- | ---------------- |
| `Insert at beg` | Inserts a new node at the beginning of the linked list | `O(1)` | `O(1)` |
| `Insert at end` | Inserts a new node at the end of the linked list | `O(1)` | `O(1)` |
| `Insert` | Inserts a new node at the specified index in the linked list | `O(n)` | `O(1)` |
| `Remove at beg` | Removes the node at the beginning of the linked list | `O(1)` | `O(1)` |
| `Remove at end` | Removes the node at the end of the linked list | `O(1)` | `O(1)` |
| `Remove` | Removes the node at the specified index in the linked list | `O(n)` | `O(1)` |
| `Reverse` | Returns an iterator that traverses the list in reverse order | `O(n)` | `O(1)` |
| `Search` | Searches for a node with the specified value in the linked list | `O(n)` | `O(1)` |
| `Length` | Returns the number of nodes in the list | `O(1)` | `O(1)` |
| `Clear` | Removes all nodes from the linked list | `O(n)` | `O(1)` |

*Note: n is the number of nodes in the linked list.*
