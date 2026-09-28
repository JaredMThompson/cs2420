class student():
    def __init__(self, last, first, ssn, email, age):
        self.last = last
        self.first = first
        self.ssn = ssn
        self.email = email
        self.age = age

    def __eq__(self, value):
        return self.ssn == value.ssn