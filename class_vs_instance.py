class Website:
    def __init__(self, title):
        self.title = title


ws = Website('My Website Title')
print(ws.__dict__)

ws2 = Website('Second Title')
print(ws2.__dict__)

class DiffrentWebsite:
    title = 'My Class Title'

dw = DiffrentWebsite()
print(dw.__dict__)