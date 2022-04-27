# Food Classifying 

from random import choice 
food = choice(["apple", "grape", "bason", "steak", "worm", "dirt"])

if food == "apple" or food == "grape":
    print("fuit")
elif food == "bason" or food == "steak":
    print("meet")
elif food == "worm" or food == "dirt":
    print("yuck")