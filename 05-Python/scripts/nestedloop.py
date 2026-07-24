#  A q a 1
#nested loop = loop within loop(inner, outer)
# outer loop:
#   inner loop:
for x in range(1, 10):
    print(x) #end is considered to be \n in normal case
for x in range(1, 10):
    print(x, end = "")
for x in range(1, 10):
    print(x, end = " ")
for x in range(3):
    for x in range(1,10):
        print(x, end = "")
    print()

rows = int(input("Enter no of rows: "))
cols = int(input("Enter no of columns: "))
symbol = input("Enter symbol to use: ")
for x in range(rows):
    for x in range(cols):
        print(symbol, end = "")
    print()
