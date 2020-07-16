class Heap:
    def __init__(self, comparator):
        self.storage = []
        self.comparator = comparator
        self.size = 0

    def insert(self, value):
        self.storage.append(value)
        self.size += 1
        self._bubble_up(self.get_size() - 1)

    def delete(self):
        self.storage.pop()
        # self._bubble_up(self.get_size() - 1)
        return self.get_size()

    def get_priority(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)
# not working still
    def _bubble_up(self, moving_index):
        parent_index = (moving_index - 1)//2
        if self.storage[moving_index] > self.storage[parent_index]:
            self.storage[parent_index] = self.storage[moving_index]
            self.storage[moving_index] = self.storage[parent_index]

    def _sift_down(self, index):
        pass
