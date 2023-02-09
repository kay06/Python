teams = {
    "astros":["Altuve", "Correa", "Bregman"],
    "angels":["Trout", "Jim"],
    "yankees":["Joe", "Jimmy", "Jeffry"]
}

teams['red sox'] = ['Price', 'Betts'] #how to add another element to the list

print(teams['astros'][2])

featured_team = teams.get('mets', 'No Freatured Team')

print(featured_team)

featured_team = teams.get('yankees', 'No Freatured Team')

print(featured_team)

