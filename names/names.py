import time

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.size = 0
        self.dupelicates = 0

    def __len__(self):
        return self.size

    def insert(self, value):
        self.size += 1
        if self is None:
            self = BSTNode(value)
        elif value.encode() < self.value.encode() is True:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    def name_check(self):
        if self.dupelicates >= 2:
            print(self.value)
            if self.left:
                return self.name_check(self.left)
    
    

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure
node_1 = BSTNode("root") # alternatice to duplicates

# Replace the nested for loops below with your improvements
for name_1 in names_1:    
    for name_2 in names_2:
        if name_1 == name_2:
            node_1.insert(name_1)
            # duplicates.append(name_1)
# node_1.insert(names_1)
# node_1.insert(names_2)
# node_1.name_check()


# node_dupes.insert(name_1)


end_time = time.time()

###### iterate #####
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")

###### bst #####
print (f"{node_1.__len__()} {node_1.name_check()}")





print (f"runtime: {end_time - start_time} seconds")












# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
