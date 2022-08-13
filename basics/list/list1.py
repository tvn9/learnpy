# List data structure example

# Defind a list variable
electrict_trucks = ["Rivian R1T", "Tesla Cybertruck", "Ford F150 Lightning", "Bollinger B2", "Lordstown Electric", "GMC Hummer"]

# Print out the list
print(electrict_trucks)

# Slice the first 3 from list
electrict_trucks = electrict_trucks[0:3]

print(electrict_trucks)

# slice the last 2 
print(electrict_trucks[len(electrict_trucks)-2:])

# skip item 2 and 2
print(electrict_trucks[0::2])