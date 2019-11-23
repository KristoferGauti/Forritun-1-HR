def alphabet():
   """Returns the alphabetical uppercase letters"""
   ascii_upper_letters = []
   for i in range(65,91): #for x in range(97,123) for the lowercase letters
	   ascii_upper_letters.append(chr(i))

   return ascii_upper_letters

def check_if_a_list_is_full(a_list):
   """a_list is a two dimentional list
   This function changes the two dim list 
   into one dim list and checks if it is full
   [[1,1,1,1],[1,1,1,1]] returns True
   [[1,1,1,1],[1,1,1,2]] returns False"""

   one_dimentional_list = [x for sublist in a_list for x in sublist] 
   if len(set(one_dimentional_list)) == 1:
      return True
   else:
      return False

def open_file(filename):
   """Opens a file and returns it
   File not found returns False"""

   try:
      file_obj = open(filename,"r")
      return file_obj
   except FileNotFoundError:
      print("File {} not found!".format(filename))
      return False

def get_max(the_dict):
   """The dictionary should be like 
   {key : [item1, item2], key2 : [item3, item4, item5]}
   It returns the max key and max length of a list"""

   max_val = 0
   max_name = ""
   for name, country_list in the_dict.items():
      curr_val = len(country_list)
      if curr_val > max_val:
         max_val = curr_val
         max_name = name

   return max_name, max_val

def print_lines(file_obj):
   """Returns a dictionary 
   {name : [country1, country2, country3], 
   name2 : [country1, country2, country3]}"""

   flight_dictionary = {}
   for line in file_obj:
      name, country = line.split()
      if name in flight_dictionary:
         #if line[1] not in flyers_dict[line[0]]: #remove duplicates countries
         flight_dictionary[name] += [country]
      else:
         flight_dictionary[name] = [country] 

   return flight_dictionary


def most_frequent_words(word_list):
   """Returns a dictionary with the top 10 most
   common words and an another dictionary with
   the top 20 most common words"""

   word_counter = {}
   #print(word_list)
   for word in word_list:
      if word in word_counter:
         word_counter[word] += 1
      else:
         word_counter[word] = 1

   popular_words = sorted(word_counter, key = word_counter.get, reverse = True)
   quantity = sorted(word_counter.values(), reverse = True)

   print(popular_words)
   print(quantity)
   # top_ten_keys = popular_words[:10]
   # top_ten_values = quantity[:10]
   # top_twenty_keys = popular_words[:20]
   # top_twenty_values = quantity[:20]

   # top_ten_words = dict(zip(top_ten_keys,top_ten_values))
   # top_twenty_words = dict(zip(top_twenty_keys,top_twenty_values))

   #return top_ten_words, top_twenty_words


a_list = ['1632', 'a', 'a', 'a', 'a', 'a', 'a', 'afterwards', 'against', 'against', 'against', 'all', 'always', 'an', 'ancient', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'and', 'any', 'any']
most_frequent_words(a_list)















