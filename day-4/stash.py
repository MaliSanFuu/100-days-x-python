
def random_tutorial():    
    import random

    random_integer = random.randint(1,10)
    random_float = random.random() * 5

    print(random_integer)
    print(random_float)

    love_score = random.randint(1,100)
    print(f"Your love score is {love_score}")

# List as a datastructure:
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america)


states_of_america[1] = 'Pencilvania'






dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

# append to add 1 more thing to the list
#states_of_america.append('Angelaland')

# extend to extend the list with another list
#states_of_america.extend(['test', 'test1'])

fruits = ["test123", "test123"]
vegetables = ["test456", "test456"]


dirty_dozen = [fruits, vegetables]

print(dirty_dozen)