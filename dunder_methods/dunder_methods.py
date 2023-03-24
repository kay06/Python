#Example 1
#the goal of the __str__ class is to get visibility into the class 
#   (printed on the first line when run)
#the goal of __repr__ is to get raw output 
#   (printed on second line when run)
#
class Invoice:
    def __init__(self, client, total):
        self.client = client
        self.total = total


    def __str__(self):
        return f'invoice from {self.client} for {self.total}'
    
    def __repr__(self):
        return f'Invoice <values- Client: {self.client}, Total: {self.total}'

inv = Invoice('Google', 500)
print(str(inv))
print(repr(inv))