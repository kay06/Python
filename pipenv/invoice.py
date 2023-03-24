#Example one 
#class Invoice:

#    def greeting(self):
#        return 'Hi There'
    

#invoice_one = Invoice()
#print(invoice_one)

#invoice_two = Invoice()
#print(invoice_two.greeting())

#Example two
#class Invoice:

#   def __init__ (self, client, total):
#        self.client = client
#        self.total = total

#    def formatter (self):
#        return f'{self.client} owes ${self.total}'
    
#google = Invoice('Google', 100)
#snapchat = Invoice('SnapChat', 200)

#print(google.formatter())
#print(snapchat.formatter())

#Example 3
#class Invoice:
        
#    def __init__ (self, client, total):
#        self.client = client
#        self.total = total

#    def formatter (self):
#        return f'{self.client} owes ${self.total}'
    
#google = Invoice('Google', 100)
#print(google.client)
#print(google.total)

#google.client = 'Yahoo'

#print(google.client)

#Example 4
#class Invoice:
#    def __init__ (self, client, total):
#        self._client = client
#        self._total = total
#
#    def formatter (self):
#        return f'{self._client} owes ${self._total}'
#    
#    @property
#    def client(self):
#        return self._client
#    
#    @client.setter
#    def client(self, client):
#        self._client = client
#
#    @property
#    def total(self):
#        return self._total
    
#google = Invoice('Google', 100)
#print(google.client)
#print(google.total)

#google.client = 'yahoo'

#print(google.client)

