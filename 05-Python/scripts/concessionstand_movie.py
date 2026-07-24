# A q a 1 z
#we will use dictionery (key:value) to make concession stand
menu = {"pizza" : 3.00, 
        "burger" : 2.50, 
        "pretzels" : 3.50,
        "popcorn" : 6.00,
        "nachos" : 4.50,
        "fries" : 2.50,
        "chips" : 1.00,
        "soda" : 3.00,
        "lemonade" : 4.25}
cart = []
total = 0
print("---------MENU---------")
for key,value in menu.items():
    print(f"{key:10}: ${value}:.2f")
print("----------------------")

while True:
    food = input("Select an item from menu(q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("------YOUR ORDER-----")
for food in cart:
    total += menu.get(food)
    print(food, end = " ")

print()
print(f"Total of food is: ${total:.2f}")
