# A q a 1 z Q
import random
#print(help(random))
# 6 sided dice
number = random.randint(1,6)
print(number)
low = 1
high = 100
number = random.randint(low, high)
#random floating point variable
number = random.random()
print(number)
options = ("rock", "paper", "scissor")
#choosing from options
option = random.choice(options)
print(option)
cards = ["2", "3", "4", "5","6", "7","8","9","J", "Q", "K", "A"]
#shuffles the seuence
random.shuffle(cards)
print(cards)