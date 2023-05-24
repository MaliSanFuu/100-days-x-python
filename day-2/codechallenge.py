#challenge1
def challenge1():
    input_string = input("Put in your numbers: ")

    a = int(input_string[0])
    b = int(input_string[1])

    print(f"{a} + {b} = {a+b}")

#challenge2
def bmi_calculator():
    height = float(input("Enter your height in m: \n"))
    weight = int(input("Enter your weight: \n"))

    bmi = weight / height**2

    bmi_as_int = int(bmi)

    print(f"Your bmi is {bmi_as_int}")

#challenge3
def life_in_weeks():
    num = int(input("What's your current age? \n"))
    years = 90 - num
    months = years * 12
    weeks = years * 52
    days = years * 365 

    print(f"You have {years} years, {months} months, {weeks} weeks and {days} days left to live.")  # noqa: E501

life_in_weeks()