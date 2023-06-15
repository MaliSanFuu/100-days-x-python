from coffee_data import MENU, resources
from art import logo
import os

PENNY = 0.01
NICKEL = 0.05
DIME = 0.10
QUARTER = 0.25

coffee_machine_resources = resources


def cls():
    """
    Clears the terminal screen.
    """
    os.system('cls' if os.name=='nt' else 'clear')


def insert_money():
    money = 0
    print("Please insert coins: ")
    money += QUARTER * int(input("\tHow many quarters? \t"))
    money += DIME * int(input("\tHow many dimes? \t"))
    money += NICKEL * int(input("\tHow many nickles? \t"))
    money += PENNY * int(input("\tHow many pennies? \t"))
    return money


def print_report():
    for resource in coffee_machine_resources:
        print(f"{resource} : {coffee_machine_resources[resource]}")


# calculation if its enough money or not
def money_calculation(user_money, cost):
    if user_money >= cost:
        return True
    else:
        print("You don't have enough money to buy")
        return False


def check_resources(user_ingredients, coffe_machine_ingredients):
    to_check = ["water", "milk", "coffe"]
    for check in to_check:
        if coffe_machine_ingredients[check] >= user_ingredients[check]:
            return True
        else:
            return False


def subtract_resources(user_ingredients, coffe_machine_ingredients):
    for key in coffe_machine_ingredients:
        if key in user_ingredients:
            coffe_machine_ingredients[key] -= user_ingredients[key]
        else:
            pass
    return coffe_machine_ingredients


def get_coffee_type():
    user_input = input("What would you like? (espresso/latte/cappuccino): \t")

    if user_input == "report":
        print_report()
        coffee_machine()
    elif user_input not in MENU:
        print("That's an invalid type")
        coffee_machine()

    return user_input, MENU[user_input]


def coffee_machine():
    global coffee_machine_resources
    switch = True

    while switch:
        print(logo)
        coffee_name, coffee_type = get_coffee_type()

        if not check_resources(coffee_type["ingredients"], coffee_machine_resources):
            print("Not enough resources, try again with different type")
            coffee_machine()

        print(f"\nOne {coffee_name} costs {coffee_type['cost']}$\n")
        money = insert_money()

        if not money_calculation(money, coffee_type["cost"]):
            print("You broke, try something else")
            coffee_machine()

        coffee_machine_resources = subtract_resources(coffee_type["ingredients"], coffee_machine_resources)
        change = money - coffee_type["cost"]
        print(f"There you go here is your {coffee_name} and the change of {round(change, 2)}$")


if __name__ == '__main__':
    cls()
    coffee_machine()
