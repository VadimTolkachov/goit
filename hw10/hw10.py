from collections import UserDict


class Field:
    pass

class Name(Field):
    pass

class Phone(Field):
    pass


class Record:
    def __init__(self, name: Name, phone: Phone | list[Phone] = None):
        self.name = name
        if type(phone) == str:
            self.phones = [phone]
        elif type(phone) == list:
            self.phones = [ph for ph in phone]
        else:
            self.phones = []

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

    def __init__(self):
        self.data = {}

    def add(self, name:Name, phone:Phone):
        self.data[Record(name, phone).name] = Record(name, phone).phones