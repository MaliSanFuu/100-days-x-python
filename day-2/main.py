print("Welcome to the tip calculator")

bill = float(input("How much was the bill?\n"))
persons = int(input("How many persons did eat?\n"))
tip = 1 + int(input("How much tip do you wanna give (10%, 12%, or 15%)?\n")) / 100

to_be_payed = (bill / persons) * tip

final_amount = round(to_be_payed, 2)
final_amount = "{:.2f}".format(to_be_payed)

print(f"The bill was {bill}$, you were {persons} persons and everyone has to pay {final_amount}$")  # noqa: E501