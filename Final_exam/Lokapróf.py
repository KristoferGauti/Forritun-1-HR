#constants
# QUIT = ["q","Q"]
# FIRST_DASH_NUM = 1
# SECOND_DASH_NUM = 5
# THIRD_DASH_NUM = 11
# DASH = "-"
# MAX_LENGTH_IBNS = 13

# def check_length(isbn_input):
#    return len(isbn_input)

# def alphabet():
#    """Returns the alphabetical uppercase letters"""
#    ascii_upper_letters = []
#    for i in range(65,123): #for x in range(97,123) for the lowercase letters
# 	   ascii_upper_letters.append(chr(i))

#    return ascii_upper_letters


# def check_valid_isbn(isbn_input, length, alphabet):
#    if length == MAX_LENGTH_IBNS:
#       second_character = isbn_input[FIRST_DASH_NUM]
#       sixth_character = isbn_input[SECOND_DASH_NUM]
#       twelwth_character = isbn_input[THIRD_DASH_NUM]

#       for char in isbn_input:
#          if char in alphabet:
#             return False

#       if second_character == DASH and sixth_character == DASH and twelwth_character == DASH:
#          return True
#       else:
#          return False
#    else:
#       return False



# def main():
#    isbn_input = input("Enter an ISBN: ")
#    alphabet_characters = alphabet()
#    while isbn_input not in QUIT:
#       length = check_length(isbn_input)
#       valid_isbn = check_valid_isbn(isbn_input, length, alphabet_characters)
#       if valid_isbn:
#          print("Valid format!")
#       else:
#          print("Invalid format!")

#       isbn_input = input("Enter an ISBN: ")


# main()

# #Dæmi 2
# #Constants
# LOTTO_ROW_LENGTH = 5
# LOTTO_MAX_NUMBER = 40

# def open_file(filename):
#    """Opens a file and returns it
#    File not found returns False"""

#    try:
#       file_obj = open(filename,"r")
#       return file_obj
#    except FileNotFoundError:
#       print("File {} not found!".format(filename))
#       return False

# def check_invalid_numbers(numbers):
#    try:
#       int_numbers = [int(x) for x in numbers]
#       return int_numbers
#    except ValueError:
#       print("Winning numbers are invalid!")
#       return None

# def lotto_card_list(file_obj):
#    lotto_card = []
#    for line in file_obj:
#       num_list = line.split()
#       lotto_card.append(num_list)

#    return lotto_card

# def find_indexes(lotto_card, win_num):
#    coordinates = []

#    for win_number in win_num:
#       for row_index, line in enumerate(lotto_card):
#          for pos_index, str_num in enumerate(line):
#             if str_num == str(win_number):
#                coordinates.append((row_index, pos_index))

#    return coordinates


# def check_win(coordinates_list, lotto_card):
#    for coordinate in coordinates_list:
#       x, y = coordinate[0], coordinate[1]
#       lotto_num = lotto_card[x][y]
      
#       lotto_card[x][y] = lotto_num + "*" 

#    return lotto_card

# def max_number(win_num_list):
#    max_number = 0
#    int_win_num_list = [int(x) for x in win_num_list]
#    for num in int_win_num_list:
#       if num > LOTTO_MAX_NUMBER:
#          max_number += int(num)

#    return max_number

# def print_nicely(lotto_card_complete):
#    for row in lotto_card_complete:
#       print(" ".join(row))
                

# def main():
#    filename = input("Enter file name: ") 
#    file_obj = open_file(filename)

#    if file_obj == False:
#       pass
#    else:
#       winning_numbers_list = input("Enter winning numbers: ").split()

#       if len(winning_numbers_list) <= LOTTO_ROW_LENGTH - 1 or len(winning_numbers_list) >= LOTTO_ROW_LENGTH + 1:
#          print("Winning numbers are invalid!")
      
#       else: 
#          int_num_list = check_invalid_numbers(winning_numbers_list)
#          if int_num_list == None:
#             pass
#          else:
#             max_lotto_num = max_number(winning_numbers_list)
#             if max_lotto_num > LOTTO_MAX_NUMBER:
#                print("Winning numbers are invalid!")

#             else:
#                lotto_card = lotto_card_list(file_obj)
#                coordinates_list = find_indexes(lotto_card, int_num_list)
#                finished_lotto_card = check_win(coordinates_list,lotto_card)
            
#                print_nicely(finished_lotto_card)

# main()



#Dæmi 3
class Distribution:
   def __init__(self, a_file = ""):
      self.__filename = a_file
      self.__average = 0  
      self.__distribution = {}
      
      numbers_two_dim = []
      for line in self.__filename:
         num_list = line.split()
         numbers_two_dim.append(num_list)
      
      one_dimentional_list = [int(x) for sublist in numbers_two_dim for x in sublist] 
      for num in one_dimentional_list:
         if num in self.__distribution:
            self.__distribution[num] += 1
         else:
            self.__distribution[num] = 1

      
   def __str__(self):
      results = ""
      for key, value in sorted(self.__distribution.items()):
         results += "{}: {}\n".format(key, value)
      return "{}".format(results)

   def __ge__(self, other):
      return self.__average >= other.__average

   def __add__(self, other):
      #new_dict = {}
      #for value in self.__distribution.values():


      return self.__average + other.__average

   def average(self):
      if self.__distribution == {}:
         self.__average = 0

      else:
         number_list = []
         length = 0
         for key, value in self.__distribution.items():
            number_list.append(key*value)
         self.__average += (sum(number_list)) / (len(number_list))

      return self.__average
    
    # You need to implement several methods here 
        
   def set_distribution(self, distribution):
      self.__distribution = distribution


def open_file(filename):
        ''' Returns a file stream if filename found, otherwise None '''
        try:
            file_stream = open(filename, "r")
            return file_stream
        except FileNotFoundError:
            return None

dist1 = Distribution()
dist1.set_distribution({1:5, 2:3, 3:7, 4:4, 5:6, 6:4}) # 1 appears 5 times, 2 appears 3 times, etc.
print("Dist1: ")
print(dist1)
print(dist1.average())

filename = "distribution.txt" #input("Enter filename: ")
file_stream = open_file(filename)

dist2 = Distribution(file_stream)
print("\nDist2: ")
print(dist2)
print(dist2.average())

if dist1 >= dist2:
    print("Dist1 >= Dist2")
else:
    print("Dist2 > Dist1")

dist3 = dist1 + dist2
print("\nDist3: ")
print(dist3)
print(dist3.average())