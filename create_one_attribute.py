#Create a "Person" class
#Create an attribute "name" in the "Person" class

class Person:
    name = 'person'

    def __init__(self, first: str, last: str, age: int):
        self.first_name = first
        self.last_name = last
        self.age = age
        self.full_name = f'{self.first_name} {self.last_name}'
        