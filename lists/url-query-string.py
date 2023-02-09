#this application adds the searched tags to the end of the url
#out put should look like the below google link
# https://www.google.com/search?q=python+development+tutorial

uri = 'https://www.google.com/search?q='

tags = ['python', 'development', 'tutorial']
formatted_tags = '+'.join(tags)
query_uri = f'{uri}{formatted_tags}'
print(query_uri)
