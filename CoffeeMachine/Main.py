from Data import MENU, resources

drink = input("What would you like? (espresso/latte/cappuccino): ").lower()
# print("Please insert coins: ")
# quarters = int(input("How many quarters? ")) * .25
# dimes = int(input("How many dimes? ")) * .1
# nickels = int(input("How many nickels? ")) * .05
# penny = int(input("How many penny? ")) * .01
# total = float("{:.2f}".format(quarters + dimes + nickels + penny))


def check_coins(totals):
    if totals > MENU[drink]["cost"]:
        print(f"Here is {totals - MENU['drink']['cost']} in Change")
        return True
    elif totals == MENU[drink]["cost"]:
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False



def check_resources(user_selection):
    for item in user_selection:
        if resources["item"] >= user_selection[item]:
            print(f"Sorry that's not enough {item}.")
            return False
        else:
            resources[item] -= user_selection[item]
            return True

# def make_coffee(user_selection):
#     coins_check = check_coins(total)
#     resources_check = check_resources(drink)
#
#     if coins_check and resources_check:
#         print(f"Here is your {drink} ☕. Enjoy!")
#     elif not coins_check:
#         print(coins_check)
#     elif not resources_check:
#         print(resources_check)
# make_coffee(drink)

is_ordering = True
profit = 0
while is_ordering:
    if drink == 'report':
        print(f"Water: {resources['water']}\n milk: {resources['milk']}\ncoffee: {resources['coffee']}\nProft: {profit}")
        is_ordering = False
    elif drink == 'off':
        is_ordering = False
    else:
