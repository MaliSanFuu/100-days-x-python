import os
import random
import art

player = {
    "cards":[],
    "score":0
}
dealer = {
    "cards":[],
    "score":0
}

def cls():
    """
    Clears the terminal screen.
    """
    os.system('cls' if os.name=='nt' else 'clear')

def deal_card():
    playing_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(playing_cards)

def change_aces(list):
    for i in range(len(list)):
        if list[i] == 11:
            list[i] = 1
    return list

def check_score(list):
    if sum(list) > 21:
        if 11 in list:
            list = change_aces(list)
            check_score(list)
        else:
            return "over"
    elif sum(list) == 21:
        return "blackjack"
    
def players_game():
    end = False
    while not end:
        if check_score(player["cards"]) == "over":
            print(f"Unfortunately you've drawn {sum(player['cards'])} and therefore overdrawn. Dealer wins!")
            end = True
        elif check_score(player["cards"]) == "blackjack":
            print(f"You've drawn {player['cards']} and hit a blackjack")
            end = True
        else:
            print(f'\tThe player has drawn {player["cards"]} \tScore: {sum(player["cards"])}')
            print(f'\tThe computer has drawn {dealer["cards"][0]}')
            user_input = input("Do you want to draw another card? (Y or N)\t").lower()

            if user_input == "y":
                player["cards"].append(deal_card())
            else:
                player["score"] = sum(player["cards"])
                end = True
                return 

def dealers_game():
    while sum(dealer["cards"]) < 17:
        dealer["cards"].append(deal_card())
    dealer["score"] = sum(dealer["cards"])
    return

if __name__ == "__main__":
    cls()
    print(art.logo)

    #first two player and computer cards
    player["cards"].append(deal_card())
    player["cards"].append(deal_card())
    dealer["cards"].append(deal_card())
    dealer["cards"].append(deal_card())

    print(f'dealer score {sum(dealer["cards"])}')

    print("First Round!")     
    players_game()
    dealers_game()
    print(f'\tThe player has drawn {player["cards"]} \tScore: {sum(player["cards"])}')
    print(f'\tThe computer has drawn {dealer["cards"]} \tScore: {sum(dealer["cards"])}')

    if check_score(dealer["cards"]) == "over":
            print(f"The Deaker overdraws with {dealer['cards']}. You win!")

    elif check_score(dealer["cards"]) == "blackjack":
        print(f"The dealer draws {player['cards']} and hits a blackjack")
    
    else:
        if player["score"] == dealer["score"]:
            cls()
            print(art.draw)
        elif dealer["score"] > player["score"]:
            cls()
            print(art.loser)
        elif player["score"] > dealer["score"]:
            cls()
            print(art.winner)
        

