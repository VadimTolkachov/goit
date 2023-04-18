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

    def add(self, phone:Phone):
        self.phones.append(phone)

    def dell(self, phone:Phone):
        for i in self.phones:
            if i == phone:

                self.phones.remove(i)
        

    def edit(self, phone:Phone, new_phone:Phone):
        self.dell(phone)
        self.add(new_phone)

    def show(self):
        return f'{self.name}: {", ".join(self.phones)}'

class AddressBooks(UserDict):
    pass


