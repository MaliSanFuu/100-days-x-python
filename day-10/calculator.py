import os 

def cls():
    """
    Clears the terminal screen.
    """
    os.system('cls' if os.name=='nt' else 'clear')

#add
def add(n1,n2):
    return n1+n2

#substract
def substract(n1,n2):
    return n1-n2

#divide
def divide(n1,n2):
    return n1/n2

#multiply
def multiply(n1,n2):
    return n1*n2

operations = {
    "+": add,
    "-": substract,
    "/": divide,
    "*": multiply
}

# operation_function = operations["*"]
# print(operation_function(2,6))

def calculation():
    print("New calculation started \n")
    num1 = float(input("What's the first number?: \t"))

    print("Which operation do you want to do: \n")
    for symbol in operations:
        print(symbol)
    print("\n")
    operation_symbol = input("Pick an operation from the lines above: \t")
    print("\n")
    num2 = float(input("What's the second number?: \t"))

    calculation_function = operations[operation_symbol]
    result = calculation_function(num1, num2)

    print(f'{num1} {operation_symbol} {num2} = {result}')

    continue_flag = True

    while continue_flag:
        going_on = input("Do you want to go on? (Y or N) \t").lower()
        if going_on == "y":
            cls()
            print(result)
            operation_symbol = input("Pick another operation: \t")
            num3 = int(input("What's the next number?: \t"))
            calculation_function = operations[operation_symbol]
            stash = result
            result = calculation_function(result, num3)
            print(f'{stash} {operation_symbol} {num3} = {result}')
        elif going_on == "new":
            continue_flag = False
            cls()
            calculation()
        else:
            continue_flag = False

calculation()