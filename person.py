#Create a "Person" class
class Person:
    name = "person"

    def __init__(self, first: str, last: str, age: int, gender = "male"):
        self.first_name = first
        self.last_name = last
        self.age = age
        self.gender = gender
        self.full_name = f'{self.first_name} {self.last_name}'

print(Person.name)