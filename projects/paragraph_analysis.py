import string

def open_file():
   """Opens a file and returns the opened 
   file if the file exists"""
   try:
      filename = input("Enter filename: ")  

      open_file = open(filename,"r", encoding="utf-8")
      return open_file

   except FileNotFoundError:
      print("Filename {} not found!".format(filename))
      return False

def paragraph_list(filename):
   """Returns a two dimentional list with the 
   paragraphs with stripped punctuation and lowercase letters"""

   paragraph_list = []
   line_list = []

   for line in filename:
      if line != "\n":
         word_list = line.split()
         #Strip punctuation and lowercase all the letters
         for word in word_list:
            line_list.append(word.lower().strip(string.punctuation))

      else:
         paragraph_list.append(line_list)
         line_list = []

   #Append the last paragraph in to the paragraph list
   if line not in paragraph_list:
      paragraph_list.append(line_list)

   return paragraph_list

def dict_words(paragraphs):
   """Returns a dictionary where the key is 
   the number of each paragraph and the value
    is a list that contains each paragraph """

   word_dict = dict()

   for number, paragraph in enumerate(paragraphs, start = 1):
      word_dict[number] = paragraph

   return word_dict

def word_list_sorted(para_list):
   """Returns a list with all the words
    sorted (duplicates included)"""

   word_list = []

   for line in para_list:
      for word in line:
         word_list.append(word)

   return sorted(word_list)

def set_words(sorted_words):
   """Returns the sorted list with 
   no duplicate words"""

   set_word_list = []

   for word in sorted_words:
      if word not in set_word_list:
         set_word_list.append(word)

   return set_word_list

def check_words(para_dict,set_words):
   """Returns a list with tuples. The tuples contains
   the word as its zero index and in what paragraph 
   the word is as its first index """

   word_list_tuple = []

   for word in set_words:
      for key, value in para_dict.items():
         if word in value:
            word_list_tuple.append((word, key))

   return word_list_tuple

def merge_list_and_print_results(word_and_paragraph_number):
   """Merges the values in the word_and_paragraph_number 
   dictionary if the keys are the same 
   and prints the results"""

   merged_value_dict = {}

   for line in word_and_paragraph_number:
      if line[0] in merged_value_dict:
         merged_value_dict[line[0]].append(line[1])
      else:
         merged_value_dict[line[0]] = [line[1]]

   return merged_value_dict

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
   
   top_ten_keys = popular_words[:10]
   top_ten_values = quantity[:10]
   top_twenty_keys = popular_words[:20]
   top_twenty_values = quantity[:20]

   top_ten_words = dict(zip(top_ten_keys,top_ten_values))
   top_twenty_words = dict(zip(top_twenty_keys,top_twenty_values))

   return top_ten_words, top_twenty_words
   
def print_results(the_dict, top_ten, top_twenty):
   """The results"""
   print("\nThe paragraph index: ")
   for key, value in the_dict.items():
      print(key, str(value)[1:-1])
   print()
   
   print("The highest 10 counts:") 
   for key_2, value_2 in top_ten.items():
      print("{}: {}".format(key_2, value_2))
   print()

   print("The highest 20 counts:")
   for key_3, value_3 in top_twenty.items():
      print("{}: {}".format(key_3, value_3))


def main():
   file_object = open_file()

   if file_object == False:
      pass
   else:
      list_of_paragraphs = paragraph_list(file_object) 
      paragraph_dict = dict_words(list_of_paragraphs) 
      sorted_words = word_list_sorted(list_of_paragraphs) 
      word_set = set_words(sorted_words) 
      word_tuple = check_words(paragraph_dict, word_set)
      the_dict = merge_list_and_print_results(word_tuple)
      top_ten_words, top_twenty_words = most_frequent_words(sorted_words)

      print_results(the_dict, top_ten_words, top_twenty_words)

main()