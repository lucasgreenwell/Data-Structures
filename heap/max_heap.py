import math
class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(self.get_size() - 1)

    def delete(self):
        pass

    def get_max(self):
        pass

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        if index is 0:
            return
        child = self.storage[index]
        parentIndex = math.floor((index - 1) / 2)
        parent = self.storage[parentIndex]
        if child > parent and child is not self.storage[0]:
            self.storage[index] = parent
            self.storage[parentIndex] = child
            self._bubble_up(parentIndex)

    def _sift_down(self, index):
        pass
