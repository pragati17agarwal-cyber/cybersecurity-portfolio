#  A q a 1
def happy_bday():
    print("Happy Birthday...")
    print("You are old")
happy_bday()
happy_bday()
happy_bday()
#can give variable name too
print()
def happy_bday(name):
    print(f"Happy Birthday {name}")
    print("You are old")
happy_bday("Bro")
happy_bday("Steve")
happy_bday("Darl")
#multiple parameters
print()
def happy_bday(name,age):
    print(f"Happy Birthday{name}")
    print(f"You are {age} years old")
happy_bday("Bro",20)
happy_bday("Steve",30)
happy_bday("Darl",40)
#positioning matters
print()
def happy_bday(age, name):
    print(f"Happy Birthday {name}")
    print(f"You are {age} years old")
happy_bday("Bro",20)
happy_bday("Steve",30)
happy_bday("Darl",40)