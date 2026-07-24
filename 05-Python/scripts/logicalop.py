#logical = evaluate multiple conditions like
#OR = either of the condition must be true
# aND = bth condition must be true
# NOT = inverts condition (not false, not true) 

temp = 25
is_raining = False
if temp > 35 or temp < 0 or is_raining:
    print("The event  is cancelled")
else:
    print("The event is ongoing")
    
temp = 35
is_sunny = True
if temp >= 28 and is_sunny:
    print("It is hot outside")
elif temp <= 0 and is_sunny:
    print("It is cold outside")
elif 30 > temp > 0 and is_sunny:
    print("It is warm inside")
elif temp == 40 and not is_sunny:
    print("It is extremely hot")