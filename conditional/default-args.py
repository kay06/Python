def greeting(name = 'Guest'):
    print(f'Hi {name}!')

greeting()
greeting('kayleece')

def some_function(collection = []):
    collection.append(1)
    return collection


print(some_function())

