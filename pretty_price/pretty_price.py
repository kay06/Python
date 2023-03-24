#input = 3.21
#output = 3.99

def pretty_price(gross_price, extension):
    if isinstance(extension, int):
        extension = extension * 0.01
    return int(gross_price) + extension


print(pretty_price(3.20, 99))
#should print 3.99
print(pretty_price(3.20, 0.95))
#should print 3.95