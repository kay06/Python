num_list = range(1, 11)
cubed_nums = []

#this is how to do the function x**3 in several lines of code 
for num in num_list:
    cubed_nums.append(num ** 3)

print(cubed_nums)

#while this is how to do this in fewer lines

cubed_nums = [num ** 3 for num in num_list]

print(cubed_nums)

#more advanced and finding only even numbers
even_numbers = []

for num in num_list:
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)

#how to do this in fewer lines of code

even_numbers = [num for num in num_list if num % 2 == 0]

print(even_numbers)


