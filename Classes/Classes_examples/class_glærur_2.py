class Person:
   def __init__(self,name,age):
      self.name = name
      self.age = age

   def print_age(self):
      print("{} is {} years old man".format(self.name, self.age))

def main():
   john = Person("John",24)

   john.print_age()

   
main()