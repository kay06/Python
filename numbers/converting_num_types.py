from decimal import Decimal

product_cost = 88.40
commision_rate = 0.08
qty = 450

#Most of the time your intigers will automatically turn into a float
#  when doing a math problem however to turn a intiger, float, or decimal into each other follow 
# the following statements


print(int(product_cost)) #turns float into an intiger but does round down not up
print(float(qty)) #turns intiger into a float
print(Decimal(product_cost)) #turns float into a decimal
print(complex(commision_rate)) #scientific notation