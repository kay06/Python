import operator
from functools import reduce 
#reduce is a functional element in python  and what we mean by 
# functional is it takes in a function and then instead of having 
# to manually call each one of those elements and perform tasks such as
#  you know another way that we could have done this and it would have been
#  a lot more code to write is we could have said that we were going to set 
# up some type of total variable here and set it equal to zero. And then we 
# were going to take our collections so we do you know a for element in collection 
# type of loop and then from there, we would do some things inside of it such as that's
#  where we could perform that look up, and perform that computation.

"""
dynamic_reducer([1, 2, 3], '+') # 6
dynamic_reducer([1, 2, 3], '-') # -
dynamic_reducer([1, 2, 3], '*') # 6
dynamic_reducer([1, 2, 3], '/') # -

"""

def dynamic_reducer(collection, op): #how to create a function
    operators = {
        "+":operator.add, 
        "-":operator.sub, 
        "*":operator.mul, 
        "/":operator.truediv        
    }

    return reduce((lambda total, element: operators[op](total, element)), collection)
    

print(dynamic_reducer([1, 2, 3], '+') )# 6
print(dynamic_reducer([1, 2, 3], '-') )# -
print(dynamic_reducer([1, 2, 3], '*') )# 6
print(dynamic_reducer([1, 2, 3], '/') )# -