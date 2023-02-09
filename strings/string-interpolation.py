#allows you to process python code in strings

name = 'Kristine'
#greeting = f'Hi {name}' #this code puts the name variable into the greeting variable
#interpolation makes it so we can put in code into our strings by putting in brackets
#however if brackets are needed in your text in your string you will want to double bracket it
#example:  greeting = f'This is my {{Bracket}} blog post'


#this code creates a personalized email
product = 'Python elearning course'

email_content = f"""
Hi {name}

Thank you for purchasing {product}

Regards, 

Sales Team
"""

print(email_content)