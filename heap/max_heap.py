import math
class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(self.get_size())

    def delete(self):
        pass

    def get_max(self):
        pass

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        children = self.storage[index]
        parentIndex = math.floor((index - 1) / 2) + 1
        parent = self.storage[parentIndex]
        if children > parent:
            self.storage[index] = parent
            self.storage[parentIndex] = children
            self._bubble_up(parentIndex)

    def _sift_down(self, index):
        pass
