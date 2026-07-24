#  A q a 1
foods = []
prices = []
total = 0
while True:
    food = input("Enter your food: ")
    if food.lower() == "q":
        break
    else:
     price = float(input("Enter the cose of: $"))


    foods.append(food)
    prices.append(price)

print("YOUR Cart")
for food in foods:
    print(food," ")
for price in prices:
    total += price
print(f"Total of foods is: {total}")
    