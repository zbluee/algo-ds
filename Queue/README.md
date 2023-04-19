## Queue

A queue is a linear data structure that allows for the ordered storage and retrieval of elements. It works on a "first in, first out" (FIFO) principle, where the element that is added first to the queue is the first one to be removed. A queue can be visualized as a line of people waiting for a service or an event, where the first person in line is the first one to be served or admitted. Queues are commonly used in computer science for tasks such as managing requests, processing data, and scheduling jobs. They can also be implemented using various data structures, such as arrays, linked lists, and queues.

<center>

## Time and Space Complexity

</center>

### • Queue List 

 `Queue` class that supports standard queue operations such as enqueue, dequeue, and peek. The class uses a list to store the elements and has additional methods to check if the queue is empty, clear the queue, and provide iterator and length functionality. 

| Method | Description | Time Complexity | Space Complexity |
| ------ | ----------- | --------------- | ---------------- |
| `create queue` | Initializes the queue with an empty list and counter. | O(1) | O(1) |
| `length` | Returns the length of the queue | O(1) | O(1) |
| `is empty` | Returns `True` if the queue is empty, `False` otherwise | O(1) | O(1) |
| `enqueue` | Adds an element to the back of the queue by appending it to the end of the list. Amortized time complexity is O(1). | Amortized O(1)| O(1) |
| `dequeue` |Removes and returns the element at the front of the queue by popping it from the front of the list. | O(n) | O(1) |
| `peek` | Returns the element at the front of the queue without removing it. | O(1) | O(1) |
| `clear` | Clears the queue by setting the list to an empty list and resetting the counter variable. | O(1) | O(1) |

<br>

*Note: n is the number of elements in the list.*