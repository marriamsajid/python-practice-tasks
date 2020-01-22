first_instance = None

def singleton(class_):
    global first_instance
    def SingletonClass(*args, **kwargs):
        global first_instance
        if first_instance is None:
            first_instance = class_(*args, **kwargs)
        return first_instance

    return SingletonClass

@singleton
class StringModification:
    def __init__(self, length, type, case):
        self.length = length
        self.type =type
        self.case = case

    def getString(self):
        print("Please enter a string: ")
        self.str = input()

    def printString(self):
        print(self.str.upper())

    def testFunction(self):
        print("length: ", self.length)
        print("type: ",self.type)
        print("case: ", self.case)
        print("str: ", self.str)
        print("Testing methods from class: ")
        self.getString()
        self.printString()


stringMod = StringModification(100, "string", "lower")
print(stringMod.length)

newSTR = StringModification(200, "str", "upper")
print(newSTR.length)

anotherObj = StringModification(300, "Check", "Check")
print(anotherObj.length)



