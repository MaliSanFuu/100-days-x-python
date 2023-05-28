import random
import os
import ascii_art

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def get_letter():
    user_input = input("\nType in a letter: ").lower()

    if len(user_input) != 1:
        print("Please just input only one letter!")
        get_letter()
    else:
        return user_input

words = ['banana', 'apple', 'cherry', 'geeks', 'scmarch']
word = random.choice(words)
char_list = [x for x in word]
blank_list = []
guessed_list = []
lives = 6

for char in char_list:
    blank_list.append("_")

game_list = [char_list,blank_list]  


print(ascii_art.hangman)
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

print(f'Your word contains {len(game_list[0])} letters.')
print(game_list[1])

while lives > 0:
    user_input = get_letter()

    cls()
    if user_input in guessed_list:
        print("You already guessed that!")

    elif user_input in game_list[0]:
        for i in range(len(game_list[0])):
            if game_list[0][i] == user_input:
                game_list[1][i] = user_input
                guessed_list.append(user_input)
    else:
        print("That's wrong!")
        guessed_list.append(user_input)
        lives -=1

    print(ascii_art.stages[lives])
    print(f'Lives left:  {lives} \n')
    print(game_list[1])

    if "_" in game_list[1]:
        continue
    else:
        break

cls()

if lives > 0:
    print(ascii_art.win)
else:
    print(ascii_art.lose)
    
