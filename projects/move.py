#Höfundur Kristofer Gauti Þórhallsson
MAP_SIZE = 10 

def map(position):
   """This function creates the map"""

   map = ""
   for x in range(1,MAP_SIZE+1):
      if x == position:
         map += "o"
      else:
         map += "x"
   return map


def info():
   """This function contains the information for user's input"""

   print("l - for moving left")
   print("r - for moving right")
   print("Any other letter for quitting")



def game():
   """This function contains the gaming loop"""

   pos = int(input("Input a position between 1 and {}: ".format(MAP_SIZE))) #MAP_SIZE = 10
   the_map = map(pos) #This variable contains the map function, which takes a position argument 
   print(the_map)

   info()

   choice = str(input("Input your choice: "))

   #The gaming loop
   while choice == "r" or choice == "l":

      #This if statement is for moving right
      if choice == "r" and pos != MAP_SIZE: 
         pos += 1
         print(map(pos))

      #This if statement is for moving left   
      elif choice == "l" and pos != 1: 
         pos -= 1
         print(map(pos))

      #This if statement checks if the "o" has gotten out of bounds from right
      elif pos == MAP_SIZE and choice == "r":  
         print(map(MAP_SIZE))

      #This if statement checks if the "o" has gotten out of bounds from left 
      elif pos == 1 and choice == "l": 
         print(map(1))

      choice = str(input("Input your choice: "))

   else:
      print(map(pos))
      
      
game()