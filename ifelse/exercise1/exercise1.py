# No touching
from random import randint
num = randint(1, 10) # picks random number from 1-1000
# No touching
your_num = int(input("Enter you lucky number: "))
print("You have enter", your_num)
print("The winning number is", num)
if your_num == num:
    print("You number is truely lucky!")
else:
    print("Your number does not match the winning number")