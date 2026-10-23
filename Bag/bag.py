#you must override __eq__ for your data type for finding dupes
class bag_list():
    
    def __init__(self):
        self.items = []
    
    def insert(self, data):
        success = self.exists(data)
        if success is not False:
            return False
        self.items.append(data)
    
    def delete(self, data):
        success = self.exists(data)
        if success is False:
            return False
        self.items[success] = self.items[-1]
        self.items.pop()
    
    def exists(self, data):
        for i in range(len(self.items)):
            if self.items[i] == data:
                return i
        return False
    
    def retrieve(self, data):
        existence = self.exists(data)
        if existence is False:
            return False
        return self.items[existence]
    
    def size(self):
        return len(self.items)
    
    def __iter__(self):
        for item in self.items:
            yield item #kinda like return but does not end the process until it jumps out of the for loop and does nothing so i goes to what is next after the orginal call.


#you must override __eq__ for your data type for finding dupes
class bag_linked_list():
    
    def __init__(self):
        self.head = None
        self.total = 0
    
    def insert(self, data):
        if self.exists(data):
            return False
        current = node(data)
        current.next = self.head
        self.head = current
        self.total += 1
    
    def delete(self, data):
        if not self.exists(data):
            return False
        current = self.head
        prev = None
        while current:
            if current.data == data:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                self.total -= 1
                break
            prev = current
            current = current.next
    
    def exists(self, data):
        return data in self
    
    def retrieve(self, data):
        for item in self:
            if item == data:
                return item
        return False
    
    def size(self):
        return self.total
    
    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

class node():
    
    def __init__(self, data):
        self.data = data
        self.next = None


#must overide your objects == > <
class bag_bst():

    def __init__(self):
        self.head = None
        self.item_count = 0

    def insert (self, data):
        if self.exists(data) is not False:
            return False
        self.item_count += 1
        leaf_node = leaf(data)
        parent = self.head
        if parent is None:
            self.head = leaf_node
        else:
            while True:
                if data < parent.item:
                    if parent.left is None:
                        parent.left = leaf_node
                        break
                    parent = parent.left
                else:
                    if parent.right is None:
                        parent.right = leaf_node
                        break
                    parent = parent.right

    def delete(self, data):
        pass

    def exists(self, data):
        current = self.head
        while current is not None:
            if data == current.item:
                return current
            elif data > current.item:
                current = current.right
            else:
                current = current.left
        return False

    def retrieve(self, data):
        location = self.exists(data)
        if location is False:
            return False
        return location.item

    def size(self):
        return self.item_count

    def __iter__(self):
        if self.head is not None:
            yield from self.recursive_iter(self.head)

    def recursive_iter(self, leaf_node):
        if leaf_node.left is not None:
            yield from self.recursive_iter(leaf_node.left)
        if leaf_node.right is not None:
            yield from self.recursive_iter(leaf_node.right)
        yield leaf_node.item

class leaf():

    def __init__(self, data):
        self.item = data
        self.left = None
        self.right = None