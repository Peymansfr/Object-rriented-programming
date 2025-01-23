list_int = []
for number in range(10):
    number = int(input("Enter a number: "))
    list_int.append(number)
print(list_int)
print("*"*50)

list_str = [input("Enter a new word: ") for word in range(10)]
print(list_str)
print("*"*50)

from random import randint

for indice in range(len(list_int)):
    list_int[indice] = randint(1,100)
print(list_int)
print("*"*50)

