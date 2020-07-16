import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self, value=None):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList(node=value)

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):

        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_head()

        else:
            pass

    def dequeue_for_bst(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_head_for_bst()
        else:
            pass

    def len(self):
        return self.size
