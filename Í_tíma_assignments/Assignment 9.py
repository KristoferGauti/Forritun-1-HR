# def function_1():#question 1 
#    a_file = open("text.txt","r")

#    for line in a_file:
#       word = line.strip()
#       words = word.replace(" ","").replace("\n","")
#       print(words,end="")


# #question 2

# def is_float(s):
#    try:
#       s = float(s)
#       return True 
#    except ValueError:
#       return False

# # Do not change the lines below
# print(is_float('3.45'))
# print(is_float('3e4'))
# print(is_float('abc'))
# print(is_float('4'))
# print(is_float('.5'))


#dæmi 3
# file_name = str(input("Enter filename: "))

# def longestword(a_file):     
#    a_file = open(file_name,"r")
#    words = a_file.read().split()
#    x = 0

#    for line in words:
#       if len(line) > x:
#          x = len(line)
#          word = line

#    print("Longest word is '{}' of length {}".format(word,x))


# longestword(file_name)


#Dæmi 4
# Here is the definition of safe_input. It should contain this exception:
# def safe_input(prompt,a_type):
#    while True:
#       try:
#          value = a_type(input(prompt))
#          return value
   
#       except ValueError:
#          print("Error: please enter a value of", a_type)

# # Do not change the lines below
# print(safe_input('Please enter an integer: ', int))
# print(safe_input('Please enter a float: ', float))
# print(safe_input('Please enter a string: ', str))

#Dæmi 5


def open_file(filename):

   a_file = open(filename,"r")

   for line in a_file:
      word = line.strip().split()
      words = " ".join(word)
      
      print(words,end=" ")

filename = str(input("Enter filename: "))
open_file(filename)






   

   


   
   

   