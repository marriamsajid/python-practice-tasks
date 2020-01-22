from abc import ABC, abstractmethod

class Person(ABC):
   def __init__(self):
      print("Person class constructor")

   @abstractmethod
   def getGender(self):
      pass

class Male(Person):

    def __init__(self):
      print("Male class constructor")
      self.gender = "Male"
      Person.__init__(self)

    def getGender(self):
        print("Male class function")
        print(self.gender)

class Female(Person):
    def __init__(self):
      print("Female class constructor")
      self.gender = "Female"
      Person.__init__(self)

    def getGender(self):
        print("Female class function")
        print(self.gender)


boy = Male()
boy.getGender()
girl = Female()
girl.getGender()
person = Person() #Generates Error that this class cannot be instantiated