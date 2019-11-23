class Person:
   def __init__(self, name, age):
      self.__name = name 
      self.__age = age

   def get_name(self):
      return self.__name

   def get_age(self):
      return self.__age

   def set_age(self,new_age):
      if new_age > 0:
         self.__age = new_age

   def print_age(self):
      print("{} is {} years old man".format(self.__name, self.__age))

def main():
   john = Person("John",69)

   print(john.get_age()) #prints 69

   john.set_age(27) #Gives John a new age. Now he is 27 years old

   print(john.get_age()) #prints 27

main()

   