from game_data import data
import random
import art

""" Generating the data needed for the Game """

""" First Choice """
ChoiceA_Random = random.randint(0, (len(data) - 1))
ChoiceA = data[ChoiceA_Random]
# Removing the selected item from the List to avoid chosing it again
data.pop(ChoiceA_Random)

""" Second Choice """
ChoiceB_Random = random.randint(0, (len(data) - 1))
ChoiceB = data[ChoiceB_Random]
data.pop(ChoiceB_Random)

def format_the_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"


# Removing the selected item from the List to avoid chosing it again

print(art.logo)
score = 0


def compare(A_data, B_data):
    global score
    global ChoiceA
    global ChoiceB
    winning = True
    while winning:

        A = A_data["follower_count"]
        print(f"Compare A: {format_the_data(A_data)}")
        print(A)
        print(art.vs)
        B = B_data["follower_count"]
        print(f"Compare B: {format_the_data(B_data)}")
        print(B)
        # Getting the data from the dectionary item to a variables
        # Second Item

        user_selection = input("Who has more followers? Type 'A' or 'B':").lower()
        if user_selection == "a" and A > B:
            print(art.logo)
            score += 1
            print(f"You're right! Current score: {score}")
            ChoiceB_Random = random.randint(0, (len(data) - 1))
            B_data = data[ChoiceB_Random]
            data.pop(ChoiceB_Random)
        elif user_selection == "b" and B > A:
            print(art.logo)
            score += 1
            print(f"You're right! Current score: {score}")
            A_data = B_data
            ChoiceB_Random = random.randint(0, (len(data) - 1))
            B_data = data[ChoiceB_Random]
            data.pop(ChoiceB_Random)
        else:
            print(art.logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            winning = False


compare(ChoiceA, ChoiceB)
