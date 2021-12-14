#python 3 module index

import random

for i in range(4):
       print(random.randint(40,50))


members = ['Roshan', 'Durgesh', 'Batman', 'Green Arrow', 'Ironaman', 'Superman']

leader = random.choice(members)

print(leader)


class RollDice:
    
    def roll_the_dice():

    
        roll_the_dice = random.randint(0,7)
        roll_dice_again =  random.randint(0,7)
        print(f"Rolling the dice \n ({roll_the_dice},{roll_dice_again})")
        return roll_dice_again, roll_the_dice

A = RollDice
print(A.roll_the_dice())
