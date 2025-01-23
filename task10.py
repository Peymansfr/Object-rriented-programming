#contacts = {'peter':'040-5466745', 'emily': '045-1212344', 'mary': 'no number'}
contacts = {}

def phone_book(number):
    if number == 1:
        who = input("name: ")
        if who in contacts:
            return contacts[who]
        else:
            return "no data"
    elif number == 2:
        name = input("name: ")
        number = input("number: ")
        if name is not contacts:
            contacts.update({name : number})
        else:
            return "already added"
        return "Ok"
    elif number == 3:
        print("quitting...")
        return False
    else:
        return "Invalid number!"

while True:
    prompt = int(input("command(1 search, 2 add, 3 quit): "))
    result = phone_book(prompt)
    if result == False:
        break
    print(result)




