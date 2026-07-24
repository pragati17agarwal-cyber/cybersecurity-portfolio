weight = float(input("Enter the weight: "))
unit = input("What is the unit(K/L): ")
if unit == "K":
    weight = weight * 2.205
    unit = "Lbs"
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs"
else:
    print(f"The {unit} not valid")

print(f"The converted weight is : {weight}{unit}")


temp = float(input("Enter the temperature: "))
unit = input("Is temperature in celsius/fahrenheit(C/F): ")
if unit == "C":
    temp = round((9 * temp)/5 + 32, 2)
    unit = "F"
    print(f"The converted temp is {temp}{unit}")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 2)
    unit = "C"
    print(f"The converted temp is {temp}{unit}")
else:
    print(f"The temp unit is inbvalid")