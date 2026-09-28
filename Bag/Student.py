class student():
    def __init__(self, data):
        data = data.split()
        self.last = data[0]
        self.first = data[1]
        self.ssn = data[2]
        self.email = data[3]
        self.age = data[4]

    def __eq__(self, value):
        return self.ssn == value.ssn