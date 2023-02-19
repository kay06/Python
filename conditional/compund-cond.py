username = 'jonsnow'
email = 'jon@snow.com'
password = 'thenorth'

if username == 'jonsnow' and password == 'thenorth': 
    #you can change and for or to only require 1 or the other object ex below
    print('account found')
else:
    print('account not found')

#if username == 'jonsnow' or password == 'thenorth': 
#to use more than 2 use the following
#if (username == 'jonsnow' or email == 'jon@snow.com') and password == 'thenorth': 



log_in = True
guest = True

if log_in and not guest:
    print('you can access the admin dashboard')
else:
    print('you can only access the standard dashboard')
