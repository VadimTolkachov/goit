from collections import UserDict
contacts = []

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



contacts = AddressBook()













class Bot:
    
    def hello(self):
        return "How can I help you?"
    
    def input_errors(func):
        def inner(*args):
            try:
                return func(*args)
            except (KeyError, IndexError, ValueError):
                return "Not enough arguments."
        return inner
    
    @input_errors
    def add(self, *args:str):
    
        lst_cont = args[0].split()
        name = Name(lst_cont[1])
        number_phone = Phone(lst_cont[2])
        rec = Record(name, number_phone)
        contacts.add_record(rec)
        if not number_phone:
            raise IndexError()
        
        return f'I add new contact: {name} {number_phone}'
    

    @input_errors
    def change(self,*args:str):
        lst_cont = args[0].split()
        name = Name(lst_cont[1])
        number_phone = Phone(lst_cont[2])
        iter = 0
        for contact in contacts:
            if contact['name'] == name and contact['number_phone'] == number_phone:
                new_number_phone = input('Enter new nomber phone:')
                contacts[iter]['number_phone'] = new_number_phone
                return f'Contact: {contact["name"]} has new telephone number: {new_number_phone}'
            iter += 1
    
        return "I didn't find this cocntact!"
    



def handler(text):
    bot = Bot()
    if text == 'hello':
        return bot.hello()
    elif text.startswith('add'):
        return Bot.add(text)
    


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