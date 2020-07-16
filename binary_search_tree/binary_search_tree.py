import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    # everything in a binary search tree can be done recursively, so let's get trippy
    def insert(self, value):

        if value > self.value:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        elif value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            self.right = BinarySearchTree(value)
            self.left = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif self.value > target:
            if not self.left:
                return False
            else:
               return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
               return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.right:
            self.right.for_each(cb)
        if self.left:
            self.left.for_each(cb)


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # print("something")
        if node.left:
            node.left.in_order_print(node.left)
        print("hello from other methods")
        print(node.value)
        if node.right:
            node.right.in_order_print(node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    # https: // www.geeksforgeeks.org / bfs - vs - dfs - binary - tree /
    # cannot figure out what is broken, it still fails when I do nothing but return the expected output
    def bft_print(self, node):
        # print("1\n8\n5\n7\n3\n6\n4\n2\n")
        queue = Queue()
        queue.enqueue(node)
        print('hello from breadth first traversal')
        while queue.size > 0:
            current_node = queue.dequeue()
            print(current_node.value)
            if current_node.left is not None:
                queue.enqueue(current_node.left)
            if current_node.right is not None:
                queue.enqueue(current_node.right)








    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass



# Testing
bst = BinarySearchTree(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)
bst.bft_print(bst)
bst.dft_print(bst)
print("elegant methods")
print("pre order")
bst.pre_order_dft(bst)
print("in order")
bst.in_order_dft(bst)
print("post order")
bst.post_order_dft(bst)