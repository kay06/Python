def full_name(first, last):
    print(f'Hi there, {first} {last}')
#always put 2 spaces here in a function
#
full_name("kayleece", "gentry")


def auth(email, password):
    if email == 'kayleece@gentry.com' and password == 'secret':
        print('Authorized')
    else:
        print('Not Authorized')

auth('kayleece@gentry.com', 'secret')


def hundred():
    for num in range(1, 10):
        print(num)


hundred()

def counter(max_value):
    for num in range(1, max_value):
        print(num)


counter(20)