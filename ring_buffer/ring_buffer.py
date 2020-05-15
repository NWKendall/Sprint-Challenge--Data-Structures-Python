# A ring buffer is a non-growable buffer with a fixed size. When the ring buffer is full and a new element is inserted, the oldest element in the ring buffer is overwritten with the newest element. This kind of data structure is very useful for use cases such as storing logs and history information, where you typically want to store information up until it reaches a certain age, after which you don't care about it anymore and don't mind seeing it overwritten by newer data.

# Implement this behavior in the RingBuffer class. RingBuffer has two methods, `append` and `get`. The `append` method adds the given element to the buffer. The `get` method returns all of the elements in the buffer in a list in their given order. It should not return any `None` values in the list even if they are present in the ring buffer.

# need DLL
## append func
    # needs to append when less than capacity
        # insert at tail
    # needs to overwrite old data when full
        # set head pointer to next
        # delete old head
        # insert new node to tail
## get func
    # needs to print/return each value in cache

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = DoublyLinkedList()
        self.size = 0

    def append(self, item):
        if self.size is self.capacity:
            self.size -1
            self.storage.new_head(item)
        else:
            self.size += 1
            self.storage.add_to_tail(item)

    def get(self):
        self.storage.get_values()


class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def delete_node(self):
            if self.prev:
                self.prev.next = self.next
            if self.next:
                self.next.prev = self.prev


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
    
    def get_head(self):
        return self.head.value

    def get_tail(self):
        return self.tail.value

    def add_to_tail(self, item):
        new_node = Node(item)
        # sets new node to head and tail if empty
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
            
        elif new_node is None:
            return
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            return new_node.value

    def new_head(self, item):
        ## creating new node to add to end
        new_node = Node(item)
        # storing old head value
        old_head_value = self.head.value
        # reassigning head to next in chain
        self.head = self.head.next
        # sets the new tail prev to existing tail
        new_node.prev = self.tail
        # links old tail to new
        self.tail.next = new_node
        # reassigns tail to new node
        self.tail = new_node
        # add one to len

    def get_values(self):
        values = []
        current = self.head
        while current is not None:
            values.append(current.value)
            current = current.next
        # values = [v for v in values if v is not None]
        return values
        

test = RingBuffer(5)

test.append(1)
test.append(2)
test.append(3)
test.append(4)
test.append(5)
test.append(10)
test.append(20)
test.append(30)


print("OLDEST:", test.storage.get_head())
print("size:", test.size)
print("NEWEST:", test.storage.get_tail())
test.get()