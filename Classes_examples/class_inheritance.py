class Animal:
   def __init__(self,name):
      self.name = name

   def __str__(self):
      return "Hi my name is {}".format(self.name)

   def make_sound(self):
      print("General animal sound.")

#We declare the Dog class which inherits the Parent class Animal
class Dog(Animal):
   def __init__(self, name, color):
      super().__init__(name) #Here we call the __init__ method from the parent class via super()
      self.color = color

   def __str__(self):
      return "Woof, my name is {} and I am a {} dog".format(self.name, self.color)

   def make_sound(self):
      print("Woof Woof!")


def main():
   animal = Animal("Kristófer")
   doggy = Dog("Ýmir","red")

   animal.make_sound() #This will print out the text from the Animal class (parent class)
   doggy.make_sound() #This will print the make_sound method from the Dog class (child class)

   print(animal)
   print(doggy)

main()

