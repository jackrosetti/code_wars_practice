import random

VOWELS = ("a","e","i","o","u")

message = input("What's your message? \n")

newMessage = ""

for letter in message:
    if letter not in VOWELS:
        newMessage += letter
    else:
        newMessage += random.choice(VOWELS)

print(newMessage)