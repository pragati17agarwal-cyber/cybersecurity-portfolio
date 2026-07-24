#  A q a 1
# collection = single "variable" used to store multiple values
# List = [] ordered and changeable - Duplicates OK
# Set = {} unordered and immutable, but add/remove OK No duplicates
# Tuple = () ordered and changeable. Duplicates OK Faster
# If want to store multiple values

fruits = ["apple", "banana", "orange", "coconut"]
print(fruits[0])
print(fruits[2])
print(fruits[0:3]) #first 3 ele
print(fruits[::2]) #every second ele
print(fruits[::-1])

#with collections we can iterate with for loop
for x in fruits:
    print (x)
for fruit in fruits:
    print(fruit)

#to check mothds available with collection
print(dir(fruits))
#description of methods to understand

#print(help(fruits))
#length of collection
print(len(fruits))
#to check if a value present in collection - give t/f
print("pineapple" in fruits)
#setting a new value
fruits[0]="pineapple"
print("pineapple" in fruits)
fruits.append("papita")
#fruits.remove("apple")
fruits.insert(0,"litchi") #inserts at given index 
fruits.reverse()
fruits.sort()
fruits.clear()
fruits = ["apple", "banana", "orange", "coconut"]
print(fruits.index("banana"))
print(fruits.count("pineapple"))
fruits = ["apple", "banana", "orange", "coconut", "apple"]
print(fruits.count("apple"))
#sets = immutble & unordered so cnt find index
fruits = {"apple", "banana", "orange", "coconut"}
print(fruits)
#print(dir(fruits))
#print(help(fruits))
print(len(fruits))
print("apple" in fruits)
#print(fruits[0]) #no indexing 
fruits.remove("apple")
print(fruits)
fruits = ("apple", "banana", "orange", "coconut", "coconut") 
print(fruits.index("apple"))
print(fruits.count("coconut"))

      