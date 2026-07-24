import math

num = 9

num += 2
print(num)

num -= 2
print(num)

num *= 2
print(num)

num /= 2
print(num)

num **= 3
print(num)

rem = num % 2
print(rem)

x = 3.56
print(round(x))

y = -4
print(abs(y))

print(pow(4, 3))

f = 7
print(max(x, y, f))
print(min(x, y, f))

print(math.pi)
print(math.e)

x = 35
print(math.sqrt(x))

x = 9.2
print(math.ceil(x))

x = 9.9
print(math.floor(x))

radius = int(input("Enter radius of circle: "))
circumference = 2 * math.pi * radius
area = math.pi * pow(radius,2)
print(f"The circumference is {round(circumference, 2)}")
print(f"The area is {round(area,2)}")