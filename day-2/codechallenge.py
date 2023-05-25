#challenge1
def challenge1():
    input_string = input("Put in your numbers: ")

    a = int(input_string[0])
    b = int(input_string[1])

    print(f"{a} + {b} = {a+b}")

#challenge2
def bmi_calculator():
    weight = int(input("Input your weight in kg (e.g. 80): \n"))
    height = float(input("Input your height in m (e.g. 1.79): \n"))

    bmi = round(weight / (height**2))

    if bmi < 18.5:
        print(f"Your BMI is {bmi} and that mean's you are underweight")
    elif bmi < 25:
        print(f"Your BMI is {bmi} and that mean's you are normal weight")
    elif bmi < 30:
        print(f"Your BMI is {bmi} and that mean's you are overweight")
    elif bmi < 35:
        print(f"Your BMI is {bmi} and that mean's you are obese")
    else:
        print(f"Your BMI is {bmi} and that mean's you are clincally obese")

#challenge3
def life_in_weeks():
    num = int(input("What's your current age? \n"))
    years = 90 - num
    months = years * 12
    weeks = years * 52
    days = years * 365 

    print(f"You have {years} years, {months} months, {weeks} weeks and {days} days left to live.")  # noqa: E501

life_in_weeks()