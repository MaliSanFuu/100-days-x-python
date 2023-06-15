import art 
import game_data
import random
import os

score = 0
data = game_data.data
first = random.choice(data)

def cls():
    """
    Clears the terminal screen.
    """
    os.system('cls' if os.name=='nt' else 'clear')

def compare_follower_count(option_one, option_two):
    if option_one["follower_count"] >= option_two["follower_count"]:
        global score
        score += 1
        return True
    else:
        print(f'I am sorry {option_one["name"]} has {option_one["follower_count"]}'
              f' follower and therefore less follower than {option_two["name"]} with'
              f' {option_two["follower_count"]} followers')
        return False

    
def comparison_print(first_option, second_option):
    print(f'Option A: {first_option["name"]}, a {first_option["description"]}, '
          f'from {first_option["country"]}')
    print(art.vs)
    print(f'Option B: {second_option["name"]}, a {second_option["description"]}, '
          f'from {second_option["country"]}')

    
def set_option(options):
    return random.choice(options)

def game():
    game_flag = True
    first = set_option(data)

    while game_flag:
        cls()
        print(art.logo)

        if score > 0:
            print(f'Your score is {score}')

        second = set_option(data)
        comparison_print(first, second)

        user_input = input("Which has more follower? ('A' or 'B')\n").lower()

        if user_input == "a":
            game_flag = compare_follower_count(first,second)
            
        else:
            game_flag = compare_follower_count(second,first)
            first = second  

    
    print(f'Your final score is: {score}')

game()

