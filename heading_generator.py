"""
What we want to be able to put in what it should show
heading_generator(title, heading_type)
heading_generator('greeting', '1')
<h1>Greeting<h1>

heading_generator('Hi there', '3')
<h3>Hi there<h3>
"""

def heading_generator(title, heading_type):
  return f'<h{heading_type}>{title}</h{heading_type}>'
  

print(heading_generator('Greetings!', '1'))
print(heading_generator('I am in a title', '3'))
