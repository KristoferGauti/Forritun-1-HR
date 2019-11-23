class Person:
   def __init__(self, some_name):
      self.name = some_name
      
   def __str__(self):
      return "Name: {}".format(self.name)

   def print_name_uppercase(self):
      print(self.name.upper())


def main():
   person_a = Person("John")
   person_b = Person("Alice")

   print(person_a.name)
   print(person_b.name)

   person_a.print_name_uppercase()
   person_b.print_name_uppercase()

main()

