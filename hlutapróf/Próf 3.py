# import string
# #text_files/abbrev.txt
# def file_open(filename):
#    try:
#       file_object = open(filename)
#       return file_object
#    except FileNotFoundError:
#       return False

# def get_lines(file_obj):
#    """Gets the lines in the file and 
#    puts the lines in a dictionary"""

#    line_list = [line.strip().split(":") for line in file_obj]

#    return dict(line_list)

# def translate(the_dict, message):
#    message_list = message.split()
#    sentence_word_list = []

#    for abbrev in message_list:
#       for key, value in the_dict.items():
#          if abbrev == key:
#             sentence_word_list.append(value)


#       if abbrev not in the_dict.keys():
#          sentence_word_list.append(abbrev)
      
      

#    return sentence_word_list
      
# def print_message(word_list, message):
#    if message[-1] == "!":
#       last_word = word_list.pop() + "!"
#       word_list.append(last_word)

#       for word_1 in word_list:
#          print(word_1, end=" ")
#       print()
   
#    elif message[-1] == "?":
#       last_word = word_list.pop() + "?"
#       word_list.append(last_word)

#       for word_1 in word_list:
#          print(word_1, end=" ")
#       print()

#    elif message[-1] == ")":
#       last_word = word_list.pop() + ")"
#       word_list.append(last_word)

#       for word_1 in word_list:
#          print(word_1, end=" ")
#       print()
         
#    else:
#       for word in word_list:
#          print(word, end=" ")
#       print()



# def main():
#    filename = input("Enter name of mapping file: ")

#    file_obj = file_open(filename)

#    if file_obj == False:
#       pass
#    else:
#       line_dict = get_lines(file_obj)
#       message = input("Enter a message: ")
#       while message.lower() != "q":
#          if message[-1] in string.punctuation:
#             word_list = translate(line_dict,message[:-1])
#          else:
#             word_list = translate(line_dict, message)

#          print_message(word_list, message)
#          word_list = []
#          message = input("Enter a message: ")


# main()

# #Dæmi 2 
# class Bug():
#    table = []
#    for _ in range(0,20):
#       table.append("x")

#    def __init__(self, position, the_bug = "b", direction = True):
#       self.position = position - 1
#       self.the_bug = the_bug
#       self.direction = direction


#    def __str__(self):
#       Bug.table[self.position] = self.the_bug
#       return "".join("{}".format(bug) for bug in Bug.table)

#    def move(self):
#       if self.direction == True:
#          self.position += 1
#          Bug.table[self.position] = self.the_bug
#          Bug.table[self.position-1] = "x"
#       else:
#          self.position -= 1
#          Bug.table[self.position] = self.the_bug
#          Bug.table[self.position+1] = "x"
         
         

#    def turn(self):
#       self.direction = False


# print("Bug 1:")
# bug1 = Bug(10)  # creates an instance of a bug whose initial position is at 10
# print(bug1)

# for i in range(1,3):
#    bug1.move()
#    print(bug1)

# bug1.turn()

# for i in range(1,5):
#     bug1.move()
#     print(bug1)

# print("Bug 2:")
# bug2 = Bug(5)   # creates an instance of a bug whose initial position is at 5
# bug2.turn()
# bug2.move()
# print(bug2)

#kóðinn hans Ýmirs
class Bug:
   """ Takes in position, can print, move, change direction, see if a bug has gone further than another bug,
   add position of two bugs to make a new bug with that position, lastly there is a function that keeps bugs
   inside the map """
   def __init__(self, position = 1):
      self.__position = position
      self.__map_size = 20
      self.__rotation = 1
      self.fix_pos()
   
   def __str__(self):
      return "".join(['b' if self.__position == x + 1 else 'x' for x in range(self.__map_size)])

   def move(self):
      self.__position += self.__rotation
      self.fix_pos()
   
   def turn(self):
      self.__rotation *= -1

   def __gt__(self, other):
      return self.__position > other.__position

   def __add__(self, other):
      new_bug_pos = self.__position + other.__position
      new_bug = Bug(new_bug_pos)
      new_bug.fix_pos()
      return new_bug

   def fix_pos(self):
      if self.__position > 20:
         self.__position = 20
      if self.__position < 0:
         self.__position = 1


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





