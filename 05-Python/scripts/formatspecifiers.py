# format specifiers = {value:flags} format values based on what flags are inserted
#.(number)f = round to that many decimal places (fixed point) a 1
price1 =  3.14159
price2 = -987.65
price3 = 12.34
print(f"Price 1 is: {price1:.2f}")
print(f"Price 2 is: {price2:.1f}")
print(f"Price 3 is: {price3:.3f}")
# :(number) = allocate that many spaces
print(f"Price 1 is: {price1:10}") #each number now has 10 spaces in total till last digit from start
print(f"Price 2 is: {price2:10}")
print(f"Price 3 is: {price3:.010}") #if we 
# :03 = allocate and ero pad that many spaces
# :< = left justify
print(f"Price 1 is: {price1:<10}") 
print(f"Price 2 is: {price2:<10}")
print(f"Price 3 is: {price3:<10}") #10 spaces from strt towards left
# :> = right justify
print(f"Price 1 is: {price1:>10}") 
print(f"Price 2 is: {price2:>10}")
print(f"Price 3 is: {price3:>10}") #10 spaces from left to right
# :^ = centre align
print(f"Price 1 is: {price1:>10}") 
print(f"Price 2 is: {price2:>10}")
print(f"Price 3 is: {price3:>10}") #centrally aligns the numbers
# :+ = use plus sign to indicate positive value or space 
print(f"Price 1 is: {price1:+10}") 
print(f"Price 2 is: {price2:+10}") #negative number with negative sign 
print(f"Price 3 is: {price3: 10}") #positive number with positive sign
# := = place sign to leftmost position
# : = insert a space before postive numbers
# :, = comma separator - separates thousands 
print(f"Price 1 is: {price1:,}") 
print(f"Price 2 is: {price2:,}")
print(f"Price 3 is: {price3:,}")