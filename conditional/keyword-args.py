def greeting(**kwargs): 
    if kwargs:
        print(f"Hi {kwargs['first_name']} {kwargs['last_name']}")
    else:
        print(f"Hi Guest have a great day")

greeting(first_name = 'Kayleece', last_name = 'Gentry')
greeting()