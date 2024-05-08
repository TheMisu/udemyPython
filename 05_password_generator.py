#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# greeting the user and taking user input
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# init the num of used characters and a helper list
used_letters = 0
used_symbols = 0 
used_numbers = 0
choices = [letters, symbols, numbers]

# total pw len
total_len = nr_letters + nr_numbers + nr_symbols

# generating the pw
pw = ""
for i in range(total_len):
    # choosing what type of char to generate
    random_choice_index = random.randint(0, len(choices) - 1)
    char_list = choices[random_choice_index]

    # choosing a random char from that list
    random_char_index = random.randint(0, len(char_list) - 1)
    random_char = char_list[random_char_index]
    pw = pw + random_char

# printing the randomly generated password
print("Your generated password is: " + pw)