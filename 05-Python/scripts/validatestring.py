# validate user input exercise # A 1 a
# 1. username is no more than 12 chrs
# 2. username can't contain spaces
# 3. username can't contain digits
username = input("Enter your username: ")
if len(username) > 12:
    print("Username can't be more than 12 characters ")
elif not username.find(" ") == -1: # as .find returns a number 
    print("Username can't contain spaces ")
elif not username.isalpha():
    print("Username can't contain digits")
else:
    print(f"Welcome {username}")


