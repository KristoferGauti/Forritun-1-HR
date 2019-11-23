# class Pair():
#    def __init__(self, a = 0, b = 0):
#       self.a = a
#       self.b = b
   
#    def __str__(self):
#       return "Value 1: {}, Value 2: {}".format(self.a, self.b)

#    def __add__(self, other):
#       return Pair(self.a + other.a, self.b + other.b)

# a = Pair(20,30)
# print(a)
# # Value 1: 20, Value 2: 30

# b = Pair(40,50)
# c = a + b
# print(c)
# # Value 1: 60, Value 2: 80


# #Dæmi 2
# class MyString():
#    def __init__(self, my_string = ""):
#       self.mystring = my_string

#    def __sub__(self, other):
#       self.other = other
#       return abs(len(self.mystring) - len(other.mystring))

#    def __gt__(self, other):
#       return len(self.mystring) > len(other.mystring)

#    def __lt__(self, other):
#       return len(self.mystring) < len(other.mystring)

# obj1 = MyString('this is a string')
# obj2 = MyString('this is another one')
# print(obj1 > obj2)
# #False

# print(obj1-obj2)
# #3

# #Dæmi 3 
# class Rectangle():
#    def __init__(self, length = 0, width = 0):
#       if length < 0:
#          self.__length = 0
#       else:
#          self.__length = length

#       if width < 0:
#          self.__width = 0
#       else:
#          self.__width = width

#    def __str__(self):
#       return "Length: {}, Width: {}".format(self.__length, self.__width)

#    def area(self):
#       return self.__length * self.__width

#    def perimeter(self):
#       return 2 * self.__length + 2 * self.__width

#    def __eq__(self, other):
#       return self.area() == other.area()

#    def __repr__(self):
#       return "Rectangle ({}, {})".format(self.__length, self.__width)


# a = Rectangle()
# b = Rectangle(2, 3)
# print(a)
# print(a.area())
# print(a.__repr__())
# print(a == b)

import random
class Dice():
   def __init__(self, value, dices = 1):
      self.__value = value
      self.__dices = dices

   def __str__(self):
      return str(self.__value)

   def __add__(self, other):
      return Dice(self.__value + other.__value, 2)

   def roll(self):
      self.__value = random.randint(1, self.__dices * 6)


def run_dice_experiment():
    dice1 = Dice(6)
    dice2 = Dice(6)
    for _ in range(0,10):
        dice1.roll()
        dice2.roll()
        sum_dice = dice1 + dice2
        print("dice1: {}, dice2: {}, sum dice: {}".format(str(dice1), str(dice2), str(sum_dice)))
        sum_dice.roll()
        print("sum dice: {}".format(str(sum_dice)))

# Main program starts here
seed_number = int(input("Enter a seed: "))
random.seed(seed_number)
run_dice_experiment()




