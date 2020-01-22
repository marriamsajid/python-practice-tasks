print("Enter the comma separated list of numbers:")
userInput = input()
print("You entered: ", userInput)
print("Output:")
numberList = userInput.split(",")

for i in numberList:
    if ((int(i))%2 != 0):
        print(i, end= ", ")
