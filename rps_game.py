import random
total_game_time = 0
high_score = 0
print("LET'S PLAY ROCK PAPER SCISSORS\n")
user_game_choice = 'no'
while user_game_choice[0] == 'n' or user_game_choice[0] == 'N':
    # getting user input
    total_game_time = 1 + total_game_time
    user_choice = input("ENTER ROCK//PAPER//SCISSORS ")
    # game parameters
    # 1: rock 2: paper 3: scissors
    if user_choice[0] == 'r' or user_choice[0] == 'R':
        result = random.randrange(1, 4)
        ch = 1
        if ch == result:
            print("ROCK")
            print("TIE")
        elif result == 2:
            print("PAPER")
            print("YOU LOSE")
        elif result == 3:
            print("SCISSORS")
            print("YOU WON")
            high_score = high_score + 1
    elif user_choice[0] == 'p' or user_choice[0] == 'P':
        result = random.randrange(1, 4)
        ch = 2
        if ch == result:
            print("PAPER")
            print("TIE")
        elif result == 1:
            print("ROCK")
            print("YOU WON")
            high_score = high_score + 1
        elif result == 3:
            print("SCISSORS")
            print("YOU LOSE")
    elif user_choice[0] == 's' or user_choice[0] == 'S':
        result = random.randrange(1, 4)
        ch = 3
        if ch == result:
            print("SCISSORS")
            print("TIE")
        elif result == 1:
            print("ROCK")
            print("YOU LOSE")
        elif result == 2:
            print("PAPER")
            print("YOU WON")
            high_score = high_score + 1
    user_game_choice = input("DO YOU WANT TO EXIT THE GAME YES/NO ")
print("TOTAL PLAYS: ", total_game_time)
print("YOUR SCORE: ", high_score)
