'''
import random

roll = int(input("roll how many?"))
dice = {}

for i in range(roll):
    random.randrange(1, 7)
for x in range(dice):
    dice[int(x)] = 1
else:
    dice[int(x)] += 1
for z in dice:
    print(z, dice[z])

'''
import random

def dice_roll (rolls):
    if rolls != 0:
        roll1 = random.randint(1, 7)
        roll1 += random.randint(1, 7)
        print(roll1)
        rolls = rolls-1
    else : 
        print("all done")

dice_roll(input("roll how many?"))