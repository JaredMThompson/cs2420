#you must override __eq__ for your data type for finding dupes
class bag():
    def __init__(self):
        self.items = []

    def insert(self, data):
        exists = self.exists(data)
        if exists is False:
            return False
        self.items.append(data)

    def delete(self, data):
        exists = self.exists(data)
        if exists is False:
            return False
        self.items[exists] = self.items[-1]
        self.items.pop()

    def exists(self, data):
        for i in range(len(self.items)):
            if self.items[i] == data:
                return i
        return False

    def size(self):
        return len(self.items)

    def __iter__(self):
        for item in self.items:
            yield item #kinda like return but does not end the process until it jumps out of the for loop and does nothing so i goes to what is next after the orginal call.
