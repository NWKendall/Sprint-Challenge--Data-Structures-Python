class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.cache = []

    def append(self, item):
        if item is None:
            return
        if self.size == self.capacity:
            self.cache.append(item)
        else:
            self.size += 1
            self.cache.append(item)

    def get(self):
        return self.cache

