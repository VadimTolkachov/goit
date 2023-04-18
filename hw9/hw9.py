contacts = []

def input_errors(func):
    def inner(*args):
        try:
            return func(*args)
        except (KeyError, IndexError, ValueError):
            return "Not enough arguments."
    return inner



@input_errors
def add(*args):
    
    lst_cont = args[0].split()
    name = lst_cont[1]
    number_phone = lst_cont[2]
    contacts.append({'name': name, 'number_phone': number_phone})
    if not number_phone:
        raise IndexError()
    return f'I add new contact: {name} {number_phone}'



@input_errors
def change(*args):
    lst_cont = args[0].split()
    name = lst_cont[1]
    number_phone = lst_cont[2]
    iter = 0
    for contact in contacts:
        if contact['name'] == name and contact['number_phone'] == number_phone:
            new_number_phone = input('Enter new nomber phone:')
            contacts[iter]['number_phone'] = new_number_phone
            return f'Contact: {contact["name"]} has new telephone number: {new_number_phone}'
        iter += 1
    
    return "I didn't find this cocntact!"

def phone(*args):
    lst_cont = args[0].split()
    name = lst_cont[1]
    for contact in contacts:
        if contact['name'] == name:
            return contact['number_phone']
        

    return "I didn't find this cocntact!"

def show_all():
    if len(contacts)>0:
        for i in contacts:
            print(f'{i["name"]}: {i["number_phone"]}')
    return ''

def hello():
    return "How can I help you?"

def comand_enoter():
    return 'Unknow comand. Please, try again.'



def hendler(text:str):
   
    if text == 'hello':
        return hello()
    
    elif text.startswith('add'):
        return add(text)
    
    elif text.startswith('change'):
        return change(text)
    
    elif text.startswith('phone'):
        return phone(text)
    
    elif text.startswith('show all'):
        return show_all()
    else:
        return comand_enoter()


def main():

    while True:
        input_comand = input('Pleace, enter comand:').lower() 
        if input_comand == 'exit' or input_comand =='close' or input_comand == 'good bye':
            print("Good bye!")
            break

        comand = hendler(input_comand)
        print(comand)


        



if __name__ == '__main__':
    main()