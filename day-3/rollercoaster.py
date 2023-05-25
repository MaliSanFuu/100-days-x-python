def rollercoaster():
    print("Welcome to the rollercoaster!")

    height = int(input("Whats is your height in cm?\n"))
    bill = 0

    if height >= 120:
        age = int(input("What's your age?"))
        print(f"Oh you're {age} years old.")

        if age > 18:
            bill = 12
        elif age >= 12 and age <= 18:
            bill = 7
        elif age < 12:
            bill = 5

        if input("Do you want a photo (y or n)?") == "Y".lower():
            bill += 3

        print(f"You have to pay {bill}$")

    else:
        print("Sorry you're not tall enough!")


