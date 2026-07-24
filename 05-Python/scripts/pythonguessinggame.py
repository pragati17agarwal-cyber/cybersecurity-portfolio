# A q a 1 z Q
# #python random number guessing game
import random
lowest_num =  1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True
print("PYTHON GUESSING GME")
print(f"Select a number between {lowest_num} and {highest_num}")
while is_running:
  guess = input("Enter your guess: ")

  if guess.isdigit():
   guess = int(guess) #limit it to int number only no cnt go too large like 2000000000000
   guesses += 1
   if guess < lowest_num or guess > highest_num:
    print("Number is out of range")

   elif guess < answer:
     print("Two low, Try again")
  
   elif guess > answer:
     print("Two high, try again")
   else:
     print("CORRECT")
     print(f"Number og guesses: {guesses}")
     is_running = False
  else:
   print("Invalid Guess")
   print(f"Please select a valid number between {lowest_num} and {highest_num}")