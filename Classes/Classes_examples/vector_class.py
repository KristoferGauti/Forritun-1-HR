import math

class Vector():
   def __init__(self, a_list):
      self.__elements = a_list

   def __str__(self):
      return "{}".format(self.__elements)

   def __len__(self):
      return len(self.__elements)

   def scaling(self, scalar):
      for i in range(len(self)):
         self.__elements[i] = self.__elements[i] * scalar

   def length(self):
      square_sum = 0
      for i in range(len(self)):
         square_sum += self.__elements[i]**2

      return math.sqrt(square_sum)
      


def main():
   vec1 = Vector([3,4])
   vec2 = Vector([1,2,3])
   print(vec1)
   #vec1.scaling(3)
   print(vec1)
   print(vec1.length())
   print(vec2.length())


main()
