heading = "Python: an Introduction"

header, _, subheader = heading.partition(': ')

print(header)
print(subheader)
#what this finction does is looks for the ': ' in your string and split the sring at that point and
#turns the heading into 2 seperate variables header and subheader and remooves the item in the string

tags = 'Python,coding,programming,development'
list_of_tags = tags.split(',')

print(list_of_tags)  

#this splits the string at the ','s and creates an array