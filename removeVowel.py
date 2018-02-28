VOWELS = ("a","e","i","o","u")

message = input("What's your message?")

newMessage = ""

for letter in message:
    if letter not in VOWELS:
        newMessage += letter

print(newMessage)