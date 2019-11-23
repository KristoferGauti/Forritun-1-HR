# #Dæmi 1

# def common_letters(first,last):
#    common_list = []
#    unique_common = []

#    for char in first:
#       if char in last:
#          common_list.append(char)
   
#    for characters in common_list:
#       if characters not in unique_common:
#          unique_common.append(characters)

#    print(sorted(unique_common))

# def common_set(first,last):
#    set1 = set(first)
#    set2 = set(last)
   
#    print(sorted(list(set1 & set2)))


# def main():
#    first, last = input("Enter a name: ").lower().split()

#    common_letters(first,last)
#    common_set(first,last)


# main()

# #Dæmi 2

# def menu():
#    return "1. Intersection\n2. Union\n3. Difference\n4. Quit"

# def game_loop(num1,num2):
#    while True:
#       union = num1 | num2
#       intersection = set()
#       choice = menu()
#       print(choice)
#       set_operation = input("Set operation: ")

#       if set_operation == "1":
#          for element in num1:
#             if element in num2:
#                intersection.add(element)
         
#          print(intersection)

#       elif set_operation == "2":
#          print(union)

#       elif set_operation == "3":
#          print(num1-num2)

#       else:
#          break

      
# def main():
#    str_list1 = input("Input a list of integers separated with a comma: ").split(",")
#    str_list2 = input("Input a list of integers separated with a comma: ").split(",")

#    num_set1 = set([int(i) for i in str_list1])
#    num_set2 = set([int(i) for i in str_list2])

#    print(num_set1)
#    print(num_set2)


#    game_loop(num_set1,num_set2)

# main()

#Dæmi 3
import string
from operator import itemgetter

def file_object():
   filename = "bigrams.txt"

   file_obj = open(filename,"r")

   return file_obj

def lowercase_letters(filename):
   """Same as this list comprehension [x.lower().split() for x in filename]"""
   lowercase = []
   for line in filename:
      lowercase.append(line.lower().strip().split())

   #remove punctuation
   new_list = []
   for index_line, line in enumerate(lowercase):
      for index_word, word in enumerate(line):
         new_list.append(lowercase[index_line][index_word].strip(string.punctuation))

   return new_list
            
def tuple_word(word_list):
   tuples = tuple()
   for index in range(1, len(word_list)):
      bigram = (word_list[index - 1]), (word_list[index])
      tuples += (bigram),

   return tuples

def 

def main():
   file_obj = file_object()
   no_punctuation_word_list = lowercase_letters(file_obj)
   a_tuple = tuple_word(no_punctuation_word_list)



main()