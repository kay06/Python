post = ('Python Basics', 'Intro guide to Python', 'Some cool python content')

print(post)

#how to remove from the end
post1 = post[:-1]

print(post1)

#how to remove from the beginning
post2 = post[1:]

print(post2)

#how to remove from the middle/specific elements (messy/not reccomended)
post3 = list(post)
post3.remove('Intro guide to Python')
post3 = tuple(post3)

print(post)
