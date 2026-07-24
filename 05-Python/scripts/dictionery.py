# A q a 1 z
# dictionery = collection of {key:value} pairs
#ordered & changeable no duplicates
capitals = {"USA" : "Washington D.C.", "India" : "New Delhi",
            "China" : "Beijing", "Russia" : "Moscow"}
print(dir(capitals))
#print(help(capitals))
#to print associated value
print(capitals.get("USA"))
print(capitals.get("Japan"))
if capitals.get("Japan"):
    print("The capital exists")
else:
    print("The capital doesn't exist")
if capitals.get("India"):
    print("The capital exists")
else:
    print("The capital doesn't exist")
# to update
capitals.update({"Germany":"Berlin"})
capitals.update({"US":"Detroit"})
#to remove
capitals.pop("China")
#to remove latest key
capitals.popitem()
#to completely remove dictionery
#capitals.clear()
#to only view the keys without the values
keys = capitals.keys()
print(keys)
for key in capitals.keys():
    print(key)
values = capitals.values()
print(values)
for value in capitals.values():
    print(value)
items = capitals.items()
print(items)
for key,value in capitals.items():
    print(f"{key}: {value}")