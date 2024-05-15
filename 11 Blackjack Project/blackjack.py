import random

# init the deck of cards (ace starts as 11pts, J/Q/K are all 10pts each)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# init the user/computer hands and their scores
user_cards = []
user_score = 0
computer_cards = []
computer_score = 0


# function that deals a card to the corresponding player
def deal_cards(player):
    # pick a random card
    dealt_card_index = random.randint(0, len(cards) - 1)

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
    else: # otherwise add it to computer_cards
        computer_cards.append(dealt_card)

deal_cards("user")
deal_cards("user")
deal_cards("user")
deal_cards("user")
print(user_cards)