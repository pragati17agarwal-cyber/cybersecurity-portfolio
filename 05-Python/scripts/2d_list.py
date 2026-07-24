##  A q a 1
#list of lists = 2d 2d tuples also workout like [()], (()), [{}]
fruits = ["apple", "banana", "pineapple", "orange"]
vegetables = ["peas", "carrot", "radish", "potatoes"]
meats = ["chicken", "fish", "turkey"]
groceries = [fruits, vegetables, meats]
print(fruits)
print(groceries) #return entire row
print(groceries[0])
print(groceries[0][0])
print(groceries[2][2])
 #OR
groceries = [["apple", "banana", "pineapple", "orange"],
              ["peas", "carrot", "radish", "potatoes"], 
              ["chicken", "fish", "turkey"]]
for collection in groceries:
    for food in collection:
        print(food,"")
        print()