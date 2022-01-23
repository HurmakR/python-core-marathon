class Employee:
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
    
    @classmethod
    def from_string(cls, str1):
        lst = str1.split("-")
        return cls(lst[0], lst[1], int(lst[2]))
 