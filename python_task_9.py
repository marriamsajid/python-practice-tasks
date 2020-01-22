#Password Validation
import re
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


