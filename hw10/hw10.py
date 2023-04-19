from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

class Name(Field):
    pass

class Phone(Field):
    
    pass
    

class Record:
    def __init__(self, name: Name, phone: Phone | list[Phone] = None):
        self.name = name
        if type(phone) == str or type(phone) == Phone:
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
    
    def __str__(self):
        phones = ", ".join([str(phone) for phone in self.phones])
        return f"{self.name}: {phones}"    

    

class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def __str__(self):
        result = []
        for record in self.data.values():
            result.append(f"{record.name.value}: {', '.join([phone.value for phone in record.phones])}")
        return "\n".join(result)

class Bot:

    def hello(self):
        return "How can I help you?"
    

comands = {Bot: 'hello'}

def handler(comand):
    for comand_bot, key in comands.items():
        if key == comand_bot:
            return comand_bot



def main():

    while True:
        input_comand = input('Pleace, enter comand:').lower()
        if input_comand == 'exit' or input_comand =='close' or input_comand == 'good bye':
            print("Good bye!")
            break

        comand = handler(input_comand)
        print(comand)


if __name__ == '__main__':
    main()