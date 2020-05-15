
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.tail = 0
        self.head = 1
        self.size = 0

    def append(self, item):
        if not self:
            return None
        else:
            if self.size == self.capacity:
                self.remove()
                self.append(item)
            else:
                self.tail = (self.tail + 1) % self.capacity
                self.queue[self.tail] = item
                self.size = self.size + 1

    def remove(self):
        if self.size == 0:
            return
        else:
            tmp = self.queue[self.head]
            # self.head = (self.head + 1) % self.capacity

        self.size = self.size - 1
        return tmp

    def get(self):
        if self.size is None:
            print("Queue is empty")
        else:
            index = self.head
            vals = []
            for i in range(self.size):
                vals.append(self.queue[index])
                index = (index + 1) % self.capacity
            return vals
    
    def print_vals(self):
        if self.size is None:
            print("Queue is empty")
        else:
            index = self.head
            for i in range(self.size):
                print(self.queue[index])
                index = (index + 1) % self.capacity
            

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail


ased = RingBuffer(5)

ased.append(1)
ased.append(2)
ased.append(3)
ased.append(4)
ased.append(5)
ased.append(6)
ased.append(7)
ased.append(8)
ased.append(9)
ased.append(10)

print("Head", ased.get_head())
print("Tail", ased.get_tail())

ased.print_vals()


# define max capacity
# measure current size, starts at 0
# capability of adding item to left most (head)
# head - oldest data
# if max capacity is reached
# age counter/pointer = max capacity
# needs to reset after max is met
# search for current pointer + 1


# head pointer increase by 1 for every append
# tail pointer incrases by 1 for every read?
# pointers reset if exceed max capacity
