teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

del teams['astros']
#del teams.get('mets', 'No team found under that name') #returns error

removed_team = teams.pop('Correa', 'No team found by that name')

