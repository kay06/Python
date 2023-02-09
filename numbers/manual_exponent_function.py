#this python code will allow a user to enter in 2 numbers to get the exponent 
from functools import reduce

#VERSION 1

def manual_exponent(num, exp):
    counter = exp - 1
    total = num
    while counter > 0:
        total *= num
        counter -= 1

    return total


print(manual_exponent(2, 3))

#VERSION 2

def manual_exponent_2(num, exp):
    computed_list = [num] * exp
    
    return(reduce(lambda total, element: total * element, computed_list))

print(manual_exponent_2(2, 3))