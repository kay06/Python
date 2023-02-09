product_cost = 88.40
commision_rate = 0.08
qty = 450 

product_cost += (commision_rate * product_cost)
print(product_cost * qty) 
#42962.4
#this is the value given when working with floats

from decimal import Decimal
product_cost_2 = Decimal(88.40)
commision_rate_2 = Decimal(0.08)
qty_2 = 450 

product_cost_2 += (commision_rate_2 * product_cost_2)
print(product_cost_2 * qty_2)

#42962.40000000000282883716451
#this is the value given when working with decimals