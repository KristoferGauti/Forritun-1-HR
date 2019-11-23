class Person:
   def __init__(self, name, age):
      self.__name = name
      self.__age = age

   def print_age(self):
      #self.__name is a private attribute and self.__age aswell
      print("{} is {} years old.".format(self.__name,self.__age)) 

def main():
   john = Person("John", 23)

   try:
      print(john.__name) #This wont work because the field is private
   except:
      print(john._Person__name) #This will print the name attribute

main()
