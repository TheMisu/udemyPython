import random
import art
import os


# defining a function that clears the console every time a new user needs to input data
def clear_console():
    # for windows
    if os.name == "nt":
        _ = os.system("cls")

    # for mac and linux (os.name is posix)
    else:
        _ = os.system("clear")


def run_game():
    """
    Function that runs the Number Guessing Game.
    """
    # generate the number that needs to be guessed
    generated_num = random.randint(1, 100)

    print("I'm thinking of a number between 1 and 100. Can you guess it?")
    # ask the user to set the game difficulty
    game_diff = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if game_diff == "easy":
        attempts_num = 10
    else:
        attempts_num = 5
    
    
    # while loop that keeps the current game running as long as the user hasn't guessed right/ran out of attempts
    guessed = False
    while not guessed and attempts_num > 0:
        print(f"You have {attempts_num} attempts to guess the number.")

        # taking the user's guess
        user_guess = int(input("Make a guess: "))


        # checking whether the user guessed right or not
        if user_guess == generated_num:
            print(f"You got it! The answer was {generated_num}.")
            guessed = True
        # otherwise subtract a life and rerun the while loop
        else:
            attempts_num -= 1
            
            if attempts_num != 0:
                # let the user know if their guess was too low/high
                if user_guess > generated_num:
                    print("Too high.\nGuess again.")
                else:
                    print("Too low.\nGuess again.")


    # if the user ran out of guesses, let them know they lost
    if attempts_num <= 0:
        print("You've run out of guesses. You lose...")


# code that allows us to run the game as many times as the user wants to
play_again = True
while play_again:
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    run_game()
    play_again_choice = input("Do you want to play again? Type 'yes' or 'no': ").lower()
    if play_again_choice == "no":
        print("Bye Bye!")
        play_again = False
    else:
        clear_console()
