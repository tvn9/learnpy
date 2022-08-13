# list element are mutable 

shopingCard = ["New Laptop", "Wireless Mouse", "Backpack", "Scientific Calculator", "Pens"]

# Adding item to list
shopingCard.append("Batteries")

# Return index 
print(shopingCard.index("Backpack")) 

# Retern true/false if item exist item in list
print("Pencil" in shopingCard)
print("Pens" in shopingCard)

# sort list
shopingCard.sort()
print(shopingCard)

# sorted returns the sorted list
print(sorted(shopingCard))

# 
print(shopingCard)

# Remove item from list
print(shopingCard.pop(1))

print(shopingCard[0:3]) # item 0, 1, and 2.

print(shopingCard[::-1]) # reverse shopingCard list

print(shopingCard[::-2]) # reversed list skip by 2







