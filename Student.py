import string


class Person:
    def __int__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


class Student(Person):
    def __int__(self, name, age):
        self.name = name
        self.age = age
