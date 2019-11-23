class Person:
   def __init__(self, name, age, relationship):
      self.__name = name
      self.__age = age
      self.__relationship = relationship

   def get_name(self):
      return self.__name 

   def get_age(self):
      return self.__age

   def get_relationship(self):
      return self.__relationship

   def print_characteristics(self):
      print("{} is {} years old and his relationship status {}".format(self.__name,self.__age, self.__relationship))

def main():
   john = Person("John",69,"it is complicated")

   print(john.get_name()) #prints John 
   print(john.get_age()) #prints 69
   print(john.get_relationship(),"\n") #prints it is complicated
   john.print_characteristics()



main()