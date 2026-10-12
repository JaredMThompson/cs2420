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
        for item in self:
            if item == data:
                return item
        return False
    
    def size(self):
        return len(self.items)
    
    def __iter__(self):
        for item in self.items:
            yield item #kinda like return but does not end the process until it jumps out of the for loop and does nothing so i goes to what is next after the orginal call.

    #you must override __eq__ for your data type for finding dupes
class bag_linked_list():
    
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        if self.exists(data):
            return False
        current = node(data)
        current.next = self.head
        self.head = current
    
    def delete(self, data):
        if not self.exists(data):
            return False
        current = self.head
        prev = None
        while current is not None:
            if current.data == data:
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
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
        total = 0
        for node in self:
            total += 1
        return total
    
    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.data
            current = current.next

class node():
    
    def __init__(self, data):
        self.data = data
        self.next = None
