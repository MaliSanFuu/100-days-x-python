rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

loser = '''                                                       


          _______             _        _______  _______  _______  _ 
|\     /|(  ___  )|\     /|  ( \      (  ___  )(  ____ \(  ____ \( )
( \   / )| (   ) || )   ( |  | (      | (   ) || (    \/| (    \/| |
 \ (_) / | |   | || |   | |  | |      | |   | || (_____ | (__    | |
  \   /  | |   | || |   | |  | |      | |   | |(_____  )|  __)   | |
   ) (   | |   | || |   | |  | |      | |   | |      ) || (      (_)
   | |   | (___) || (___) |  | (____/\| (___) |/\____) || (____/\ _ 
   \_/   (_______)(_______)  (_______/(_______)\_______)(_______/(_)
                                                                    


'''

winner = '''
          _______                     _________ _        _ 
|\     /|(  ___  )|\     /|  |\     /|\__   __/( (    /|( )
( \   / )| (   ) || )   ( |  | )   ( |   ) (   |  \  ( || |
 \ (_) / | |   | || |   | |  | | _ | |   | |   |   \ | || |
  \   /  | |   | || |   | |  | |( )| |   | |   | (\ \) || |
   ) (   | |   | || |   | |  | || || |   | |   | | \   |(_)
   | |   | (___) || (___) |  | () () |___) (___| )  \  | _ 
   \_/   (_______)(_______)  (_______)\_______/|/    )_)(_)                                                                                                                  

'''

draw = '''


__________________ _  _______    _______    ______   _______  _______          
\__   __/\__   __/( )(  ____ \  (  ___  )  (  __  \ (  ____ )(  ___  )|\     /|
   ) (      ) (   |/ | (    \/  | (   ) |  | (  \  )| (    )|| (   ) || )   ( |
   | |      | |      | (_____   | (___) |  | |   ) || (____)|| (___) || | _ | |
   | |      | |      (_____  )  |  ___  |  | |   | ||     __)|  ___  || |( )| |
   | |      | |            ) |  | (   ) |  | |   ) || (\ (   | (   ) || || || |
___) (___   | |      /\____) |  | )   ( |  | (__/  )| ) \ \__| )   ( || () () |
\_______/   )_(      \_______)  |/     \|  (______/ |/   \__/|/     \|(_______)
                                                                               


'''

versus = '''

          _______    
|\     /|(  ____ \   
| )   ( || (    \/   
| |   | || (_____    
( (   ) )(_____  )   
 \ \_/ /       ) |   
  \   /  /\____) | _ 
   \_/   \_______)(_)
                     

'''

#Write your code below this line 👇
import random
import time

weapons = [rock, paper, scissors]

print("Welcome to Rock, Paper and Scissors")
print("\n")

user_input = input("Choose your weapon (R, P or S): ").lower()

if user_input == 's':
    user_input = scissors
elif user_input == 'r':
    user_input = rock
elif user_input == 'p':
    user_input = paper
else:
    print("invalid input")

computer_input = random.choice(weapons)

print("\n")
print(f'Your Weapon of choice: {user_input}')
print(versus)
print(f'The Computer chooses: {computer_input}')
print("\n- - - - - - - - - - - - - - - - - ")

time.sleep(1)

#userinput rock
if user_input == rock:
    if computer_input == scissors:
        print(winner)
    elif computer_input == rock:
        print(draw)
    else:
        print(loser)

#userinput scissors
elif user_input == scissors:
    if computer_input == paper:
        print(winner)
    elif computer_input == scissors:
        print(draw)
    else:
        print(loser)

#userinput paper
elif user_input == paper:
    if computer_input == rock:
        print(winner)
    elif computer_input == paper:
        print(draw)
    else:
        print(loser)