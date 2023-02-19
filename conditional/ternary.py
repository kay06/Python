
#role = 'admin'
role = 'guest'

auth = 'Can access' if role == 'admin' else 'Cannot access'

print(auth)

