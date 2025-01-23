from task4 import *
def even_int(list):
    even_numbers = [even for even in list if not even%2]
    print(len(even_numbers))

even_int(number_except_zero())


