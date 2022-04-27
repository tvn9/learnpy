# Caculate age

# Get current year 
import datetime
curr_year = datetime.date.today()

# Ask user for birth_year
birth_year = int(input("What year was you born? "))

# Calculate age
age = curr_year.year - birth_year

# Print output result to terminal
print(f"Your are {age} years old.")

print("Ha " * 5)