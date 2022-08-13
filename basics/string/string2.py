first = None
last = None

formated = None

first = "Chris"
last = "Nguyen"
formated = first + " " + last

print(formated)

print(f"Hello {first} {last}")

print("Hello {} {}".format(first, last)) # This is python 2 syntax

# Slice string
myString = "0123456789"

print(myString[1:8])

print(myString[::1])

print(myString[::-1]) # reverse string

print(myString[::-5])

print(myString[::-2])