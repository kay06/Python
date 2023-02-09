players = ['Altuve', 'Bregman', 'Correa', 'Gattis']

for player in players:
    print(player)


players2 = {
  '2b': 'Altuve',
  '3b': 'Bregman',
  'ss': 'Correa',
  'dh': 'Gattis'
}

for position, player in players2.items():
    print('Position', position)