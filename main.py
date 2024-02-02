import random

# random_number = random.random()

# print("{:.3f}".format(random_number))


rock_sign = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper_sign = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors_sign = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
Game_list = ["Rock", "Paper", "Scissors"]
Game_sign = [rock_sign, paper_sign, scissors_sign]
pc_choice = random.randint(0, (len(Game_list) - 1))
user_choice = int(input("Make your choice: Enter 1 for Rock, 2 for Paper or 3 for Scissors?\n")) - 1
if user_choice >= 3 or user_choice < 0:
    print("Wrong input YOU LOSE!")
elif user_choice == 2 and pc_choice == 0:
    print("Your Choice is " + Game_list[user_choice] + Game_sign[user_choice] + "\n And Computer Choice is " + Game_list[pc_choice] + Game_sign[pc_choice] + "\n You Lose!")
elif user_choice == 0 and pc_choice == 2:
    print("Your Choice is " + Game_list[user_choice] + Game_sign[user_choice] + "\n And Computer Choice is " + Game_list[pc_choice] + Game_sign[pc_choice] + "\n You WIN!")
elif user_choice > pc_choice:
    print("Your Choice is " + Game_list[user_choice] + Game_sign[user_choice] + "\n And Computer Choice is " + Game_list[pc_choice] + Game_sign[pc_choice] + "\n You WIN!")
elif user_choice < pc_choice:
    print("Your Choice is " + Game_list[user_choice] + Game_sign[user_choice] + "\n And Computer Choice is " + Game_list[pc_choice] + Game_sign[pc_choice] + "\n You LOSE!")
else:
    print(
        "Your Choice is " + Game_list[user_choice] + Game_sign[user_choice] + "\n And Computer Choice is " + Game_list[
            pc_choice] + Game_sign[pc_choice] + "\n It's a DRAW!")
