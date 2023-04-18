from collections import UserDict


class Field:
    pass

class Name(Field):
    pass

class Phone(Field):
    pass


class Record:
    def __init__(self, name:Name, phone:Phone=None):
        self.name = name
        self.phones = [phone] if phone else []

    def add(self):
        pass

    def dell(self):
        pass

    def edit(self):
        pass

class AddressBooks(UserDict):
    pass


contacts = []