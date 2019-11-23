# import string



# def letters(sentence):
#    alphas = []
   
#    for word in sentence.split():
#       for letter in word:
#          if letter in string.punctuation:
#             continue
#          elif letter not in alphas:
#             alphas.append(letter)
#    return alphas

# # Main starts here
# sentence = input("Input a sentence: ")


# unique_letters = letters(sentence)

# # Call the function here
# print("Unique letters:", unique_letters)


# #Dæmi 2 


# def to_list(string):
#    without_commas = []
#    for word2 in string.split():
#       for word in word2.split(","):
#          without_commas.append(word)
   

#    return without_commas



# # The main program starts here
# the_string = input("Enter the string: ")

# the_list = to_list(the_string)

# print(the_list)

# #Dæmi 3

# def return_value():
#    value_list = []

#    while True:
#       value = str(input("Enter value to be added to list: "))
#       if value == "exit":
#          break 
#       value_list.append(value)
   
#    return value_list

# def loop(letters):
#    letters *= 3
#    for x in letters:
#       print(x,end="\n")


# values = return_value()

# loop(values)

#Dæmi 4

#vector_product = |a| * |b| * cos(a)
import math

a_vector = []
b_vector = []


def two_dim_vec():
   vector1 = []
   vector2 = []

   element1 = int(input("Element no 1: "))
   element2 = int(input("Element no 2: "))

   element3 = int(input("Element no 1: "))
   element4 = int(input("Element no 2: "))

   vector_times_othervector = element1 * element3 + element2 * element4

   vector1.append(element1)
   vector1.append(element2)

   vector2.append(element3)
   vector2.append(element4)

   length1 = math.sqrt((vector1[0])**2 + (vector1[1])**2)
   lenght2 = math.sqrt((vector2[0])**2 + (vector2[1])**2)

   alpha = vector_times_othervector / (length1 * lenght2)

   result = length1 * lenght2 * math.cos(alpha)

   print(result) 


def three_dim_vec():
   element1 = int("Element no 1: ")
   element2 = int("Element no 2: ")
   element3 = int("Element no 3: ")

   element1 = int("Element no 1: ")
   element2 = int("Element no 2: ")
   element3 = int("Element no 3: ")

   result = element1

   print(result)



def main():
   size = int(input("Input vector size: "))

   if size == 2:
      two_dim_vec()
   elif size == 3:
      three_dim_vec()

main()






