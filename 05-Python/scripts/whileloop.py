#  A q a 1
# WHILE LOOP = executes somecode while some conditions remain true
 #repeat prompt till not enter name
name = input("Enter your name: ")
#if name == "":
 #   print("Did not enter name")
#else:
 #   print(f"Hi {name}")
#stops after asking for once
while name == "":
    print("You did not enter your name: ")
    name = input("Enter your name: ")

print(f"Hi {name}")
age = int(input("Enter your age: "))
while age < 0:
    print("age cant be negative")
    age = int(input("Enter your age: "))

print(f"You are {age} years old")
num = int(input("Ënter a number: "))
while num < 0 or num > 10:
    print("Num not between 1-10")
    num = int(input("Ënter a number: "))
print(f"Num entered: {num}")
