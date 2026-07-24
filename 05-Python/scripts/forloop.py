#  A q a 1
# # For loop = executes block of code fixed number of times
# you can iterate over a range, seuence, string, etc
for x in range(1,11):
    print(x)
for x in reversed(range(1,11)):
    print(x)
for x in range(1,11,2): #count by 2
    print(x)
credit_card = "2345-6789-0098-7654"
for x in credit_card:
    print(x)
for x in range(2,20):
    if x == 3:
     continue;
    else:
     print(x)
for x in range(2,20):
    if x == 3:
     break;
    else:
     print(x)