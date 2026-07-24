#conditional expression = one line shortcut for if-else statement (ternary  operator)
#Print or assign one of two values based on condition
# X if condition else Y
 
num = 5
print("Positive" if num>0 else "Negative")
result = "Even" if num%2==0 else "Odd"
print(result)
a = 3 
b = 45
print(f"{a} is greater" if a>b else f"{b} is greater")
age = 30
print("adult" if age>20 else "child" )