import random
import math

lower = int(input("Enter the Lower Number "))
higher = int(input("Enter the Higher Number "))

r = random.randint(lower,higher)
print("You only have ",round(math.log(higher - lower + 1, 2)), " chances to guess the integer")

count = 0
while count < math.log(higher - lower + 1, 2):
    count += 1
    guess = int(input("Guess a number:- "))
 
    if r == guess:
        print("Congratulations you did it in ",count, " try")
        break
    elif r > guess:
        print("You guessed too small!")
    elif r < guess:
        print("You Guessed too high!")
if count >= math.log(higher - lower + 1, 2):
    print("\nThe number is %d" % r)
    print("\tBetter Luck Next time!")