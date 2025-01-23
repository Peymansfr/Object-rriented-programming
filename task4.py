
def number_except_zero():
    list = []
    while True:
        number = int(input("Enter a new number: "))
        if number != 0:
            list.append(number)
        else:
            negative_numbers = [num for num in list if num < 0 ]
            print(negative_numbers)
            return list

number_except_zero()


