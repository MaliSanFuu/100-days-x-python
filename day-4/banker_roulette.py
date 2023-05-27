import random

str_input = input("Who's going to buy the meal today? Type in the names: \n")
names = str_input.split(sep=", ")
choice = random.choice(names)

print(names)
print(f"{choice} has to buy the Meal today")
