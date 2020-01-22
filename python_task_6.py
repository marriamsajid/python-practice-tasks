print("Please enter sentence: ")
inputSentence = input()
alphabet = 0; digit = 0

for character in inputSentence:
    if character.isalpha():
        alphabet += 1
    if character.isdigit():
       digit += 1

print("LETTERS ", alphabet)
print("DIGITS ", digit)