import re
profile =  "https://auth.geeksforgeeks.org in the portal of http://www.geeksforgeeks.org/user/articles"
listItems = profile.split(" ")
print(listItems)
pattern = r"((http|https)://\w+\.\w+\.\w+\/*w*).*"

for item in listItems:
    if (re.match(pattern, item)) is not None:
        print("Item: ", item)