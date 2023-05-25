print("Welcome to the love calculator!")
    name1 = input("Your name: \n").lower()
    name2 = input("Their name: \n").lower()
    complete_string = name1 + name2

    true_score = 0
    love_score = 0

    true_score += complete_string.count("t")
    true_score += complete_string.count("r")
    true_score += complete_string.count("u")
    true_score += complete_string.count("e")

    love_score += complete_string.count("l")
    love_score += complete_string.count("o")
    love_score += complete_string.count("v")
    love_score += complete_string.count("e")

    final_score = str(true_score) + str(love_score) 
    final_score = int(final_score)

    if final_score < 10 or final_score > 90:
        print(f"Your score is {final_score}, you go together like coke and mentos")
    elif final_score >= 40 and final_score <= 50:
        print(f"Your score is {final_score}, you are alright together")
    else:
        print(f"Your score is {final_score}")