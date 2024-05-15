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



def deal_card():
    """
        Randomly picks a card from the deck and returns it.
    """
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(deck)



def count_score(player_hand):
    """
        Counts the score of the player's hand. If the player has an Ace and a score > 21, replace the Ace with 1.
        If the player has Blackjack, return score = 0
    """
    score = sum(player_hand) 

    # if the player has an ace (11) and score > 21, change the ace to 1
    if 11 in player_hand and score > 21:
        player_hand.remove(11)
        player_hand.append(1)
        score -= 10
    
    # if the user has blackjack, set score to 0 (easier to deal with blackjack later)
    if score == 21 and len(player_hand) == 2:
        score = 0

    return score


def decide_winner(user_score, computer_score):
    """
        Decide who won the game based on their scores. Prints a custom message based on the output
        of the if statements.    
    """
    # deal with the individual cases
    if user_score == computer_score:
        print("Draw. Nobody won.")
    elif computer_score == 0:
        print("You lost. The dealer has Blackjack.")
    elif user_score == 0:
        print("You won with a Blackjack 😎")
    # if both the user and the computer are over, the user loses
    elif user_score > 21 and computer_score > 21:
        print("You went over 21. You lost! ")
    elif user_score > 21:
        print("You went over 21. You lost! ")
    elif computer_score > 21:
        print("The dealer went over 21. You won! ")
    elif user_score > computer_score:
        print("You won! ")
    else:
        print("You lost... ")



def run_game():
    """
        Runs the Blackjack game until the user goes over 21 or refuses to hit.
    """
    print(art.logo)

    # init useful variables like player/dealer hands and keep_playing 
    player_hand = []
    dealer_hand = []
    keep_playing = True


    # deal 2 cards to the player and the dealer
    for i in range(2):
        player_hand.append(deal_card())
        dealer_hand.append(deal_card())


    # while loop that keeps the game running
    while keep_playing:
        # check the scores and print the hands/score
        player_score = count_score(player_hand)
        dealer_score = count_score(dealer_hand)

        print(f"\tYour hand: {player_hand}, current score: {player_score}")
        print(f"\tDealer's first card: {dealer_hand[0]}")

        # end the game if any of the players has Blackjack or if player_score > 21
        if player_score == 0 or dealer_score == 0 or player_score > 21:
            keep_playing = False
        # otherwise ask the user if they want to hit or not
        else:
            player_hit = input("Type 'y' if you want to get another card, type 'n' to pass: ")
            if player_hit == "y":
                player_hand.append(deal_card())
            else:
                keep_playing = False
    
    # once the player is done, if the computer has no blackjack and score < 17, it must hit
    while dealer_score != 0 and dealer_score < 17:
        dealer_hand.append(deal_card())
        dealer_score = count_score(dealer_hand)


    # print the final hands/scores and announce the winner
    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_hand}, final score: {dealer_score}")
    decide_winner(player_score, dealer_score)


# start/restart the game
stop_game = False
while not stop_game:
    clear_console()
    run_game()
    print("\n")

    play_again = input("Type 'y' if you want to play another game, type 'n' if you want to quit: ")
    if play_again == "n":
        stop_game = True
        clear_console()
        print("Bye bye!")