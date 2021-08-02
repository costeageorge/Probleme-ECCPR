import random
min = 1
max = 6


print("You want to rolling dices?")
roll_again=input()
while roll_again == "yes" or roll_again == "y":
    print ("Rolling the dices...")
    print ("The values are....")
    print (random.randint(min, max))
    print (random.randint(min, max))
    print("Rolling again?")
    roll_again=input()
