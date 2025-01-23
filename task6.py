from task4 import *

def sum_pos_int(list):
    pos_list= [number for number in list if number > 0 and not number % 3 ]
    print(pos_list)

sum_pos_int(number_except_zero())