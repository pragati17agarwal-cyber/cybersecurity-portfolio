name = "Bro code"
r = len(name)
print(f"The length of string is {r}")
r = name.find(" ") #first occurence of given character here space
print(f"Position of blank is in {r}")
r = name.find("r")
print(f"Position of r is in {r}")
r = name.rfind("o") #reverse finding of occurence
print(f"Position of o in reverse is {r}")
name = name.capitalize() # a #capitalizes the first letter only
print(name)
name = name.upper() # uppercases all letters
print(name)
name = name.lower()
print(name)
r = name.isdigit() #checks if the entire string is only digits combination of alpha and digit is false
print(r)
r = name.isalpha() #checks if entire string is alphabets = space also gives false 
print(r)
phone_number = input("Enter your phone number: ")
r = phone_number.count("-")
print(r)
r = phone_number.count("8")
print(r)
name = name.replace("o","a")
print(name)
phone_number = phone_number.replace("-"," ")
print(phone_number)
#TO GET COMPREHENSICE LIST OF aLL STRING METHODS
print(help(str))