import random
import art

# init the deck of cards (ace starts as 11pts, J/Q/K are all 10pts each)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# init the user/computer hands and their scores
user_cards = []
user_score = 0
computer_cards = []
computer_score = 0


# function that deals a card to the corresponding player
def deal_cards(player):
    # declaring the variables as global so that we can access them from inside the function
    global user_score
    global computer_score

    # pick a random card
    dealt_card_index = random.randint(0, len(cards) - 1)
    card_score = cards[dealt_card_index]

    # transforming the card if needed
    if dealt_card_index ==  10:
        dealt_card = "J"
    elif dealt_card_index == 11:
        dealt_card = "Q"
    elif dealt_card_index == 12:
        dealt_card = "K"
    else:
        dealt_card = cards[dealt_card_index]
    
    # if the the user requested a card, then add it to user_cards
    if player == "user":
        user_cards.append(dealt_card)
        user_score += card_score    
    else: # otherwise add it to computer_cards
        computer_cards.append(dealt_card)
        computer_score += card_score


# starting the game
input_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
if input_choice == "y":
    play_game = True
    print(art.logo)
else:
    play_game = False
    print("Ok. Bye bye! ")


# cards are never removed from the deck and they are randomly chosen
# so we can (initially) just deal twice to the user/computer instead of alternating between them
deal_cards("user")
deal_cards("user")
deal_cards("computer")
deal_cards("computer")


# run the game if the user chooses to play
while play_game:
    # show the user their cards/the computer's first card
    print(f"\tYour cards: {user_cards}, current score: {user_score}")
    print(f"\tComputer's first card: {computer_cards[0]}")

    # if the user has blackjack
    if user_score == 21 and len(user_cards) == 2:
        print("Win with a Blackjack. 😎")

    # ask if the user wants to hit or pass
    get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")

    # deal another card to the user
    if get_another_card == "y":
        deal_cards("user")
    # print their final hand/score and let them know if they won
    else:
        play_game = False
        print(f"\tYour final hand: {user_cards}, final score: {user_score}")
        print(f"\tComputer's final hand: {computer_cards}, final score: {computer_score}")

        if user_score > computer_score:
            print("You won! :)")

# testing the code
# deal_cards("user")
# deal_cards("user")
# print(user_cards)
# print(user_score)