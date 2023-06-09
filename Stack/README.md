## Stack

A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle. It has two main operations, `push` and `pop`, which add and remove elements from the top of the stack, respectively.

<center>

## Time and Space Complexity

</center>

### • Stack List 

This `Stack` class is implemented using a Python list. The list is used to store the elements in the stack, and the class provides methods to interact with the list and perform stack operations. 

| Method | Description | Time Complexity | Space Complexity |
| ------ | ----------- | --------------- | ---------------- |
| `length` | Returns the length of the stack | O(1) | O(1) |
| `is empty` | Returns `True` if the stack is empty, `False` otherwise | O(1) | O(1) |
| `push` | Adds an element to the top of the stack | O(1)/O(n<sup>2</sup>) | O(1) |
| `pop` | Removes and returns the top element of the stack | O(1) | O(1) |
| `peek` | Returns the top element of the stack without removing it | O(1) | O(1) |
| `clear` | Removes all elements from the stack | O(1) | O(1) |

<br>

### • Limited Size Stack

This implementation of a `Stack` uses a Python list to store the elements, but with a limited size specified during the initialization of the stack object.

| Method | Description | Time Complexity | Space Complexity |
| ------ | ----------- | --------------- | ---------------- |
| `length` | Returns the length of the stack | O(1) | O(1) |
| `is empty` | Returns `True` if the stack is empty, `False` otherwise | O(1) | O(1) |
| `push` | Adds an element to the top of the stack | O(1)/O(n<sup>2</sup>) | O(1) |
| `pop` | Removes and returns the top element of the stack | O(1) | O(1) |
| `peek` | Returns the top element of the stack without removing it | O(1) | O(1) |
| `clear` | Removes all elements from the stack | O(1) | O(1) |

<br>

### • Stack Linked List
This code implements a Stack data structure using a singly linked list. The linked list is implemented using a Node class with a data attribute and a next attribute that points to the next node in the list. The LinkedList class maintains a head attribute that points to the first node in the list and a nodes attribute that keeps track of the number of nodes in the list.

| Method | Description | Time Complexity | Space Complexity |
| ------ | ----------- | --------------- | ---------------- |
| `length` | Returns the length of the stack | O(1) | O(1) |
| `is empty` | Returns `True` if the stack is empty, `False` otherwise | O(1) | O(1) |
| `push` | Adds an element to the top of the stack | O(1) | O(1) |
| `pop` | Removes and returns the top element of the stack | O(1) | O(1) |
| `peek` | Returns the top element of the stack without removing it | O(1) | O(1) |
| `clear` | Removes all elements from the stack | O(1) | O(1) |

*Note: n is the number of elements in the list.*