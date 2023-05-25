bill = 0

size = input("What size do you want S, M or L?").lower()

if size == 's':
    bill += 15
elif size == "m":
    bill += 20
elif size == "l":
    bill += 25

pepperoni = input("Do you want pepperoni? Y or N?").lower()

if pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill+= 3

extra_cheese = input("Extra Cheese? Y or N").lower()

if extra_cheese == "y":
    bill += 1

print(f"Your final bill is {bill}")