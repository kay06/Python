tags= [ 'python', 'development', 'tutorials', 'code']
totals = [1, 5, 8, 546, 2]
print(tags) #base list of index order

#any changes to a list are permenant
tags.sort() #sorts alphabetical
totals.sort() #sorts from lowest to highest

print(tags)
print(totals)

tags.sort(reverse=True) #sorts backwards alphabetical
tags.sort(reverse=True) #sorts from highest to lowest

print(tags)
print(totals)

