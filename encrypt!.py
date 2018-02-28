letters = {"A":"E", "B":"U","C":"Z","D":"F","E":"I","F":"Y", "G": "P", "H":"Q", "I":"S", "J":"N", "V":"Z"}

def main():
    message = input("Enter a message \n").upper()
    encrypted = ""

    for letter in message:
        if letter in letters:
            encrypted += letters[letter]
        else:
            encrypted += letter

    print(encrypted)

main()