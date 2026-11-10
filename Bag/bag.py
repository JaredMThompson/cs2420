from prime import is_prime

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
        if self.exists(data):
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
        if not self.exists(data):
            return False
        self.head = self.recursive_delete(data, self.head)
        self.item_count -= 1
        return True

    def recursive_delete(self, data, c):
        if data < c.item:
            c.left = self.recursive_delete(data, c.left)
        elif data > c.item:
            c.right = self.recursive_delete(data, c.right)
        else:
            if not c.left:
                c = c.right
            elif not c.right:
                c = c.left
            else:
                predecessor = c.left
                while predecessor.right:
                    predecessor = predecessor.right
                c.item = predecessor.item
                c.left = self.recursive_delete(predecessor.item, c.left)
        return c

    def exists(self, data):
        current = self.head
        while current is not None:
            if data == current.item:
                return True
            elif data > current.item:
                current = current.right
            else:
                current = current.left
        return False

    def retrieve(self, data):
        current = self.head
        while current is not None:
            if data == current.item:
                return current.item
            elif data > current.item:
                current = current.right
            else:
                current = current.left
        return False

    def size(self):
        return self.item_count
        '''
        count = 0
        for item in self:
            count += 1
        return count
        '''

    def __iter__(self):
        if self.head is not None:
            yield from self.recursive_iter(self.head)

    def recursive_iter(self, leaf_node):
        if leaf_node is not None:
            yield from self.recursive_iter(leaf_node.left)
            yield leaf_node.item
            yield from self.recursive_iter(leaf_node.right)

class leaf():

    def __init__(self, data):
        self.item = data
        self.left = None
        self.right = None

#override you hash and comparisons
class bag_hash():
    def __init__(self, init_table_size = 3):
        if init_table_size%2 == 0:
            init_table_size += 1
        while not is_prime(init_table_size):
            init_table_size += 2
        self.table_size = init_table_size
        self.hash_table = [None] * self.table_size
        self.total = 0
        self.total_active = 0

    def insert(self, data):
        #could be faster if the exists check was in the func rather than a seperate func making us do roughly twice
        #the work but it is fairly cheap with our data and this is more readable so it wins
        if self.exists(data):
            return False
        location = hash(data)%self.table_size
        current = self.hash_table[location]
        location_offset = 0
        while current is not None and current is not False:
            location_offset += 1
            current = self.hash_table[(location + location_offset)%self.table_size]
        if current is None:
            self.total += 1
        self.total_active += 1
        self.hash_table[(location + location_offset)%self.table_size] = data
        self.resize_check()

    def delete(self, data):
        #in this case I do not use exists because it is still really easy to read,
        #when checking if it exists if it does just replace it instead of doing it again
        location = hash(data)%self.table_size
        current = self.hash_table[location]
        location_offset = 0
        while current is not None:
            if current is not False and current == data: #handle edge case of compairing a bool with the item causing an error
                self.hash_table[(location + location_offset)%self.table_size] = False
                self.total_active -= 1
                return True
            location_offset += 1
            current = self.hash_table[(location + location_offset)%self.table_size]
        return False

    def exists(self, data):
        location = hash(data)%self.table_size
        current = self.hash_table[location]
        location_offset = 0
        while current is not None:
            if current is not False and current == data:
                return True
            location_offset += 1
            current = self.hash_table[(location + location_offset)%self.table_size]
        return False

    def retrieve(self, data):
        #once again better to just do the work then call exists to do it twice, honestly exists seems fairly useless in most of these bags unless you want/need more clarity
        location = hash(data)%self.table_size
        current = self.hash_table[location]
        location_offset = 0
        while current is not None:
            if current is not False and current == data:
                return current
            location_offset += 1
            current = self.hash_table[(location + location_offset)%self.table_size]
        return False

    def size(self):
        return self.total_active

    def __iter__(self):
        for i in range(self.table_size):
            if self.hash_table[i] is not None and self.hash_table[i] is not False:
                yield self.hash_table[i]

    #dynmaic resize
    def resize_check(self):
        if (self.total_active/self.total) < 0.5: #if data is > %50 garbage clean the garbage
            self.total = self.total_active
            self.new_table(self.table_size)

        elif (self.total/self.table_size) >= 0.7: #if data is >= %70 of table double table size and garbage gets cleaned
            self.total = self.total_active
            new_table_size = (self.table_size * 2) + 1
            while not is_prime(new_table_size):
                new_table_size += 2
            self.new_table(new_table_size)

        elif (self.total/self.table_size) <= 0.3: #if data is <= %30 of table half table size and garbage gest cleaned
            self.total = self.total_active
            new_table_size = (self.table_size // 2) + 1
            while not is_prime(new_table_size):
                new_table_size += 2
            self.new_table(new_table_size)

    def new_table(self, table_size):
        old_list = []
        for item in self:
            old_list.append(item)
        self.table_size = table_size
        self.hash_table = [None] * table_size
        for item in old_list:
            self.insert(item)