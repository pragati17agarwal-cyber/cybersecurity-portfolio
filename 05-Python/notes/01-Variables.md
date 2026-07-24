New-Item -Path "05-Python\scripts\01_variables.py" -ItemType File

Variables = Container for a value(string, integer, float, boolean)
It behaves as value it contains
can be any


#Ctrl + S = to save
#py filename.py = run file 

name = "Pragati" #string
age = 19 #integer
earning = 300000.67 #float
print(f"My name is {name} and I am {age} years old.")
print(f"My earning is ${earning}")

#boolean 
is_student = False
if is_student:
    print("You are a student") // for is_student being true
else:
    print("You are not a student") // for is_student being false

for_sale = True 
if for_sale:
    print("The item is for sale") // since true 
else:
    print("Not for sale")