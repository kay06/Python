usernames = [
  'jon',
  'tyrion',
  'theon',
  'cersei',
  'sansa',
]

#continue / break

#continue
for username in usernames:
    if username == 'cersei':
        print(f'Sorry, {username} you are not allowed')
        continue
    else:
        print(f'{username} is allowed')

#break
for username in usernames:
    if username == 'theon':   
        print(f'{username} was found at index {usernames.index(username)}') 
        break
    print(username)    