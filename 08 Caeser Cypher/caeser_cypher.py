import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# function that both encrypts and decrypts based on what the user wants to do
def caeser(text, shift, direction):
    # fixing a bug that happens if the shift is > 26
    shift %= len(alphabet)

    final_text = ""
    # changing the direction of the shift if needed
    if direction == "decode":
        shift *= -1
 
    for char in text:
        # if the char is a letter, then encode/decode it else just add it to final text
        if char in alphabet:
            # rest of the code stays the same
            letter_index = alphabet.index(char)
            shifted_index = (letter_index + shift) % len(alphabet)
            new_letter = alphabet[shifted_index]
            final_text += new_letter
        else:
            final_text += char

    # print the processed text
    print(f"The {direction}d text is: {final_text}")


# printing the logo
print(art.logo)

# init loop variable
again = "yes"

while again == "yes":
    if again == "yes":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        caeser(text, shift, direction) 

        # asking the user if they want to rerun the program
        again = input("Do you want to run the program again? ").lower()

# Printing goodbye after exiting the program
print("Goodbye!")