##scope
enemies = 1 

def increase_enemies():
    enemies = 2
    print(f'Enemies inside function {enemies}')

increase_enemies()
print(f'Enemies outside function {enemies}')


# local scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
# print(potion_strength)

#global scope
player_health = 10
def game():
    def drink_potion1():
        potion_strength = 2
        print(player_health)

    drink_potion1()

# there is no block scope in python
enemies1 = ["Skeleton", "Zombie", "Alien"]
game_level = 3

# everything that is in the if block is not seperated from the rest of the code
# only in def functions
if game_level < 5:
    new_enemy = enemies1[0]

print(new_enemy)

#modifying global scope
def increase_enemies1(enemies):
    return enemies + 1

enemies = increase_enemies1(enemies)
print(enemies)

#Global constants!
PI = 3.14159
TWITTER_HANDLE = "luukeenz"

print(TWITTER_HANDLE)
