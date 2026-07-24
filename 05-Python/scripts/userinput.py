name = input("What is your name: ")
age = int(input("What's your age: "))
print(f"Hi {name} Happy Birthday ")
age = age + 3
print(f"You are {age}") 
    
       
# Area of rectangle

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
areaR = length * breadth
print(f"The area is {areaR}cm^2")

#Shopping cart problem

item = input("What item do you want: ")
price = float(input("Whtat is the price: "))
amount = int(input("How many do you need: "))
total = price * amount
print(f"You have bought {item} for {total} amount")