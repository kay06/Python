"""
user database query
Kristine
Tiffany
Kayleece
"""

users = ['Kristine', 'Tiffany', 'Kayleece']

print(users)

users.insert(0, 'Anthony') 
#.insert(position_number) will add an element to the position_nunber listed
print(users)

users.append("Ian")
#.append() adds a element to the end of your array
print(users)

print([users[2]])
#print([list_name[element_position]]) will print the element in list_name at element_position

users[4] = 'Brayden'
#using list-name[position_number] will grab the element at position_number 
#setting it = to another element replaces the element at position_number
print(users)

#how to remove items from a list

#version 1 - when you know the exact value

users.remove('Kayleece')
#.remove('string') will go throught your list to find the string and
# remove the string from the list, can also be used with normal elements
print(users)

#version 2 - when you want to use the last element in a list

popped_user = users.pop()
#.pop() pops the last element off and by putting it into a var and printing 
# you get the last element you can also print the original var to get the
#  list with last element removed
print(popped_user)
print(users)

#version 3 - when you know the index value of the element

del users[0]
#del list_name[position_number] will take the list_name and remove the element at position_number
print(users)