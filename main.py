
alphabet = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

# (Above) Stores the english alphabet in a list

def decode(): # The function to decode a ciphered text
    string = input("What is the string you would like to decode? ").upper()
    number = int(input("How many times is it moved? "))
    for char in string:
        if char == " ":
            print(" ", end="")
        elif char in alphabet:
            location = alphabet.index(char)
            ciphered = (location - number) % 26
            new_string = alphabet[ciphered]
            print(new_string, end="")

def encode(): # The function to encode a ciphered text
    string = input("What is the string you would like to encode? ").upper()
    number = int(input("How many times would you like it moved? "))
    for char in string:
        if char == " ":
            print(" ", end="")
        elif char in alphabet:
            location = alphabet.index(char)
            ciphered = (location + number) % 26
            new_string = alphabet[ciphered]
            print(new_string, end="")

option = input("Would you like to translate encode with caser cipher or decode (En/De): ").upper()

# (Above) The User's choice

if option == "DECODE":
    decode()
elif option == "ENCODE":
    encode()

# (Above) Choice handling