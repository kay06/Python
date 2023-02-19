def greeting (time_of_day, *args, **kwargs):
    print(f"Hi {' '.join(args)}, I hope you are having a great {time_of_day}")

    if kwargs:
        print('your tasks for the day are:')
        for key, val in kwargs.items():
            print(f"{key} => {val}")

greeting('morning', 'kayleece', 'gentry', 
        first = 'Do dishes', second = 'take dog out', third = 'homework')

greeting('morning', 'katelyn', 'peterson', first = 'dishes', second = 'stairs', third = "hallway")