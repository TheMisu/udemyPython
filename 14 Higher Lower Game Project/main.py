# importing the needed modules
import art
import game_data
import random
import os


# getting the logo and the game data dict
logo = art.logo
vs_icon = art.vs
data_list = game_data.data



def clear_console():
    """
    Function that clears the console so that the output can be displayed in 
    a nicer way
    """
    # for windows
    if os.name == "nt":
        _ = os.system("cls")

    # for mac and linux (os.name is posix)
    else:
        _ = os.system("clear")


def run_game():
    """
    Function that runs the HigherLower Game in the console
    """
    # init the score variable and generate the first random choice (out of the data dict)
    score = 0
    choice_a = random.choice(data_list)
    followers_a = choice_a["follower_count"]

     
    # while loop that stops when the user makes a wrong choice
    made_mistake = False
    while not made_mistake:
        # generate choice_b in the while loop so that we can constantly generate a new B
        choice_b = random.choice(data_list)
        followers_b = choice_b["follower_count"]

        # print the logo and the score (if score > 0)
        print(logo)
        if score > 0:
            print(f"You're right! Current score: {score}.")

        # print the available choice
        print(f"Choice A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}.")
        print(vs_icon)
        print(f"Choice B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}.")

        # ask the user to choose which they think is more famous
        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()


        # decide whether the user made the correct choice or not
        if user_choice == "a" and followers_a > followers_b:
            score += 1 # increase the score 
            clear_console()
        elif user_choice == "b" and followers_b > followers_a:
            score += 1
            clear_console()
            choice_a = choice_b # store choice_b in choice_a before rerunning the loop
        else:
            print(f"Sorry, that's wrong... Final score: {score}")
            made_mistake = True


# loop that allows the player to play for as long as they want 
play_again = True
while play_again:
    run_game()
    choice = input("Type 'y' to play again or 'n' to exit: ")
    if choice == "n":
        play_again = False
    clear_console()