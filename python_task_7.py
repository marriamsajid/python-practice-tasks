#without,hello,bag,world

print("Enter comma separated words: ")
userInput = input()
listt = userInput.split(",")
listt.sort()
my_string = ','.join(listt)
print(my_string)