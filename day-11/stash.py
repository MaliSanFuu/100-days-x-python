player = {
    "cards":[10,11]
}

computer = {
    "cards":[10,11]
}

def check_blackjack(dict):
    if sum(dict["cards"]) == 21:
        print("you win!")
    elif sum(dict["cards"]) > 21:
        print("you lose!")

check_blackjack(player)
check_blackjack(computer)

player["cards"].append(11)

print(player["cards"])