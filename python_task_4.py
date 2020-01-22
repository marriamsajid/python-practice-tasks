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
print("Testing method from object: ")
print("length: ", stringMod.length)
print("type: ",stringMod.type)
print("case: ", stringMod.case)
print("str: ", stringMod.str)
stringMod.getString()
stringMod.printString()

stringMod.testFunction()