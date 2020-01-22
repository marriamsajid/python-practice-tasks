#decorator to measure time
import time
import re

def timee(function):
    def getFunctionTime():
        start = time.perf_counter()
        function()
        end = time.perf_counter()
        return start, end
    return getFunctionTime

@timee
def sortList():
    print("Enter comma separated words: ")
    userInput = input()
    listt = userInput.split(",")
    listt.sort()
    my_string = ','.join(listt)
    print(my_string)

start, end  = sortList()
print("Duration of sort list: ", end-start)


@timee
def passwordValidation():
    print("Enter the passwords to check:")
    user_input = input()
    pass_list = user_input.split(",")

    for password in pass_list:
        if (len(password) >= 6 and len(password) <= 12):
            if (re.search("[a-z]", password)):
                if (re.search(("[A-Z]"), password)):
                    if (re.search("[0-9]", password)):
                        if (re.search("[$#@]", password)):
                            print("Valid password: ", password)


start, end = passwordValidation()
print("Duration of password validation: ", end-start)

@timee
def numberInRange():
    for number in range(1000,2001):
        if (number%7 == 0 and number%5 != 0):
            print(number, end=", ")

start, end = numberInRange()
print("\n Duration of numbers in range: ", end-start)