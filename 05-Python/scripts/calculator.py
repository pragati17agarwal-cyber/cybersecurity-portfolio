operator = input("Enter an operator: ")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
if operator == "+":
    r= a+b
    print(r)
elif operator == "-":
    r= a-b
    print(r)
elif operator == "*":
    r= a*b
    print(r)
elif operator == "/":
    r=a/b
    print(r)
else:
    print("Invalid operator")
