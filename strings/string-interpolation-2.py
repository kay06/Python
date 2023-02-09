name = 'Kristine'
age = 12
product = 'Python elearning course'

#greeting ="Hi {0}, you are listed as {1} years old and you have purchased: {2} - {3}".format(name, age, product, 'Kayleece G')
#you can do it like the above but to avoid confusion do what is below
from_account = 'Kayleece G'
greeting = f"Hi {name}, you are listed as {age} years old and you have purchased: {product} - {from_account}"
print(greeting)