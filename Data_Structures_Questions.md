Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?
constant O(1)
2. What is the runtime complexity of `dequeue`?
constant O(1)
3. What is the runtime complexity of `len`?
constant O(1)

## Binary Search Tree

1. What is the runtime complexity of `insert`? 
logarithmic O((log(n)))
2. What is the runtime complexity of `contains`?
logrithmic O((log(n)))
3. What is the runtime complexity of `get_max`? 
logarithmic O(log(n))
## Heap

1. What is the runtime complexity of `_bubble_up`?
logarithmic O((log(n)))
2. What is the runtime complexity of `_sift_down`?
logarithmic O((log(n)))
3. What is the runtime complexity of `insert`?
logarithmic O((log(n)))
4. What is the runtime complexity of `delete`?
logarithmic O((log(n)))
5. What is the runtime complexity of `get_max`?
constant O(1)
## Doubly Linked List


1. What is the runtime complexity of `ListNode.insert_after`?
constant O(1)
2. What is the runtime complexity of `ListNode.insert_before`?
constant O(1)
3. What is the runtime complexity of `ListNode.delete`?
constant O(1)
4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?
constant O(1)
5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
constant O(1)
6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
constant O(1)
7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?
constant O(1)
8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?
constant O(1)
9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?
constant O(1)
10. What is the runtime complexity of `DoublyLinkedList.delete`?
constant O(1)
    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?
    constant O(1) vs constant O(1) up to linear O(n) in the worst case