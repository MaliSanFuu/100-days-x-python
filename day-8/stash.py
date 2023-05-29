
#functions with parameters
def greet_with_name(name):
    print(f'Hi {name}')
    print(f'How are you {name}')

greet_with_name("Angela")

#functions with more than 1 parameters
def greet_with_name_and_location(name, location):
    print(f'Hello {name}')
    print(f"It's nice in {location}")

#positional arguments
greet_with_name_and_location("Lukas", "Freiburg")

#keyword arguments
greet_with_name_and_location(location="Freiburg", name="Lukas")
