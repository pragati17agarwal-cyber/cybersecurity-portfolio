# if = print only if IF condition is true
#indentation is a must otherwise will not get response
age = int(input("Enter your age: "))
if age >= 20:
   print("Eligible")
elif age < 0:
    print("Not born yet")
elif age > 200:
    print("Too old")
else:
    print("Not eligible")

response = input("Would you like food(Y/N): ")
if response == "Y":
    print("Yup")
else:
    print("Nope")

name = input("Enter name: ")
if name == "":
    print("Pls enter name")
else:
    print(f"Hi {name}")