class Bug():
   MAP_SIZE = 20
   MIN = 1
   MAX = MAP_SIZE
   EMPTY = "x"
   BUG = "b"

   def __init__(self, pos):
      self.__pos = pos
      self.__rotation = 1
   
   def __str__(self):
      if self.__pos > self.MAX:
         self.__pos = self.MAX
   
      if self.__pos < self.MIN:
         self.__pos = self.MIN

      map_list = []

      for index in range(self.MAP_SIZE + 1):
         if index == self.__pos:
            map_list.append(self.BUG)
         else:
            map_list.append(self.EMPTY)
      
      return "".join(map_list)
   
   def move(self):
      self.__pos += self.__rotation
      return self.__pos
   
   def turn(self):
      self.__rotation *= -1
      return self.__rotation
   
   def __gt__(self, other):
      return self.__pos > other.__pos

   def __add__(self, other):
      return Bug(self.__pos + other.__pos)

print("Bug 1:")
bug1 = Bug(10)  # creates an instance of a bug whose initial position is at 10
print(bug1)

for i in range(1,3):
    bug1.move()
    print(bug1)

bug1.turn()

for i in range(1,5):
    bug1.move()
    print(bug1)

print("Bug 2:")
bug2 = Bug(5)   # creates an instance of a bug whose initial position is at 5
bug2.turn()
bug2.move()
print(bug2)

if bug1 > bug2:
    print("Bug1 has travelled further than bug2")

print("Bug 3:")
# creates an instance of a bug whose initial position is the sum of the position of bug1 and bug2
bug3 = bug1 + bug2  
print(bug3)
bug3.move()
bug3.move()
print(bug3)
if bug3 > bug1:
    print("Bug3 has travelled further than bug1")


print("Bug 1:")
bug1 = Bug(18)  # creates an instance of a bug whose initial position is at 18
print(bug1)

for i in range(1,5):
    bug1.move()
    print(bug1)