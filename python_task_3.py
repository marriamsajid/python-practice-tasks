numberDictionary = {}

def generateDictionary(number):
    for digit in range(1,number+1):
        numberDictionary[digit] = digit*digit
    return numberDictionary

print(generateDictionary(8))