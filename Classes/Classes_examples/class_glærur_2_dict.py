class Person:
   def __init__(self, name, age):
      self.name = name 
      self.age = age

   def print_age(self):
      print("{} is {} years old man".format(self.name, self.age))

   
def main():
   john = Person("John", 24)
   mary = Person("Mary", 69)

   print(john.__dict__) #prints {name: John age: 24}
   print(mary.__dict__) #prints {name: Mary age: 69}

main()