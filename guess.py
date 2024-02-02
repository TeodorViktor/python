import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

def guess():
  PC_number = random.randint(1, 100)
  attempt = 1
  
  if level == "easy":
    attempt = 10
  else:
    attempt = 5

  print(f"You have {attempt} attempts remaining to guess the number.")
  guess = int(input("Make a guess "))

  while guess != PC_number and attempt != 0:
    if guess == PC_number:
      print(f"You got it! The answer is {guess}")
      attempt = 0
    elif guess > PC_number:
      print("Too high! \n Guess again")
      attempt -= 1
      print(f"You have {attempt} attempts remaining to guess the number.")
      guess = int(input("Make a guess "))
    else:
      print("Too low! \n Guess again")
      attempt -= 1
      print(f"You have {attempt} attempts remaining to guess the number.")
      guess = int(input("Make a guess "))
      
guess()