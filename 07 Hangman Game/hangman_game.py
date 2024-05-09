import random
import hangman_words
import hangman_art

# hangman stages and logo
stages = hangman_art.stages
logo =  hangman_art.logo


# greeting the user with the logo
print(logo)

# lives counter
lives = 6

# list with possible words
word_list = hangman_words.word_list

# randomly chosen word from the list
chosen_word = random.choice(word_list)
print(f"The chosen word is: {chosen_word}") # printing the chosen word for debugging purposes

# init the list of character that will be displayed to the user
display = []
for letter in chosen_word:
    display.append("_")

# variables that make the loop work
guessed_all = False
lost = False

# init a list to keep track of the already gussed letters
already_guessed = []

# loop that makes the game work
while not guessed_all and not lost:
    # user's guessed letter
    guess = input("Guess a letter: ").lower()

    # checking if the user already guessed this letter
    repeat = True
    while repeat:
        repeat = False
        if guess in display or guess in already_guessed:
            guess = input("You have already guessed the letter " + guess + ". Please try another one: ").lower()
            repeat = True
    
    # checking if the user guessed correctly or not 
    # if yes, we change the char in display
    letter_index = 0
    for letter in chosen_word:
        if letter == guess:
            display[letter_index] = letter
        letter_index += 1

    # subtracting a life if the guess was wrong
    if guess not in display:
        lives -= 1
        already_guessed.append(guess)
        letter_index += 1

    # Telling the user what they've guessed so far
    print(stages[lives])
    print("Test" + f" {lives}")
    print(f"{' '.join(display)}")

    # game logic

    # checking if display still has _
    if "_" not in display:
        guessed_all = True

    # checking if the user still has lives
    if lives == 0:
        lost = True

# telling the user whether they won or lost
if lives == 0:
    print(stages[0])
    print("You lost... The word was: " + chosen_word)
else:
    print(stages[lives])
    print("Congratulations! You won! ")

