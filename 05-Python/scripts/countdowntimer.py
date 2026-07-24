
#  A q a 1
import time
my_time = int(input("Enter time: "))
for x in range(1, my_time):
    print(x)
    time.sleep(1)
print("TIME UP")

for x in reversed(range(1, my_time)):
    print(x)
    time.sleep(1)
print("TIME UP")

#another method to reverse - need to add a step
for x in range(my_time, 1,-1):
    print(x)
    time.sleep(1)
print("TIME UP")

#want to display in form of time in seconds
for x in range(my_time, 1,-1):
    sec = x % 60
    min = int(x / 60) % 60
    hour = int(x / 3600)
    print(f"00:{min:02}:{sec:02}")
    time.sleep(1)
print("TIME UP")