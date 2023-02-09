import math

sale_prices = [
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1,
  3
]

#sort
sorted_list = sorted(sale_prices)
print(sorted_list)
#split
num_of_sales = len(sorted_list)
print(num_of_sales)
half_slice = math.floor(num_of_sales/2)
first_sale_items = sorted_list[:half_slice]
last_sale_items = sorted_list[-(half_slice):]

print(first_sale_items)
print(last_sale_items)


median = sorted_list[half_slice : half_slice + 1]

print(median)

