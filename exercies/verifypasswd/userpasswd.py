user_name = input("Login name: ")
password = input("Password: ")

l = len(password)
passwd = password.replace(password, ("*" * l))

print(f"Your user {user_name} and password ({passwd}) is {l} chracters long.")