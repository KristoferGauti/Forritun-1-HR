#Dæmi 1
# def values():
#    data_dict = {}


#    while True:
#       name = input("Name: ")
#       number = input("Number: ")
#       more_data = input("More data (y/n)? ")
#       data_dict.update({name : number})
#       if more_data == "n":
#          break


#    return data_dict

# def print_dictionary(dictionary):
#    print(sorted(dictionary.items()))

# def main():
#    value = values()
#    print_dictionary(value)


# main()

#Dæmi 2
# import string 

# def get_word_list(a_file):
#    word_list = []
#    for line in a_file:
#       line_split = line.split()
#       word_list.extend(line_split)

#    return word_list
      
# def remove_punc(a_list):
#    remove_punc_list = []
#    for word in a_list:
#       if word[-1] in string.punctuation:
#          word = word[:-1]
#          remove_punc_list.append(word)
#       else:
#          remove_punc_list.append(word)

#    return remove_punc_list

# def word_count_dict(the_list):
#    word_count_dict = {}
#    word_list = []

#    for word in the_list:
#       if word in word_count_dict:
#          word_count_dict[word] += 1
#       else:
#          word_count_dict[word] = 1
      
      
#    for word in word_count_dict.items():
#       word_list.append(word)
      
#    print(word_list)

#    #print(sorted(word_count_dict.items()))
   

# def main():
#    filename = input("Name of file: ")
#    # Get a file stream
#    fstream = open(filename)

#    # Get a list of words from the stream
#    word_list = get_word_list(fstream) 
#    ## print(word_list)
#    fstream.close()
#    #remove punctuation 
#    no_punc_list = remove_punc(word_list)
   
#    # Transform the list to a dictionary of word-count pairs
#    word_count_dict = word_list_to_counts(no_punc_list) 
#    #word_list_to_counts(word_list)

#    # Finally, makes a list of tuples from the dictionary
#    ##word_count_tuples = dict_to_tuple(word_count_dict)
#    ##print(sorted(word_count_tuples))
    
# main()

#Alvöru dæmi 2 
# import string

# def get_word_list(filename):
#     list_object = []

#     for lines in filename:
#         for word in lines.lower().split():
#             if word[-1] in string.punctuation:
#                 word = word[:-1]
#             list_object.append(word)

#     return list_object

# def word_list_to_counts(list_object):
#     word_count_dict = {}

#     for word in list_object:
#         if word in word_count_dict:
#             word_count_dict[word] += 1
#         else:
#             word_count_dict[word] = 1
#     return word_count_dict

# def dict_to_tuple(dict_object):
#     value_key_list = []
#     for key, val in dict_object.items():
#         value_key_list.append((key, val))
#     return value_key_list

# def main():
#     filename = input("Name of file: ")
#     # Get a file stream
#     fstream = open(filename)
#     # Get a list of words from the stream
#     word_list = get_word_list(fstream)
#     fstream.close()
#     # Transform the list to a dictionary of word-count pairs
#     word_count_dict = word_list_to_counts(word_list) 
#     # Finally, makes a list of tuples from the dictionary
#     word_count_tuples = dict_to_tuple(word_count_dict)
#     print(sorted(word_count_tuples))

# main()

# #Dæmi 3

# def menu_selection():
#    choose = input("add(a), remove(r), find(f): ")
#    return choose

# def execute_selection(choice,a_dict):
#    dictionary = a_dict
#    if choice == "a":
#       key = input("Key: ")
#       value = input("value: ")
#       dictionary.update({key: value})
#    elif choice == "r":

   
#    print(dictionary)
      


# # Do not change this main function
# def main():
#     more = True
#     a_dict = {}
    
#     while more:      
#         choice = menu_selection()
#         execute_selection(choice, a_dict)
#         again = input("More (y/n)? ")
#         more = again.lower() == 'y'
    
#     #dictlist = dict_to_tuples(a_dict)
#     #print(sorted(dictlist))

# main()

#Dæmi 3 klárað
def menu_selection():
   print("Menu:")
   choice = input("add(a), remove(r), find(f): ")
   return choice

def execute_selection(choice, a_dict):
   if choice == "a":
      key = input("Key: ")
      value = input("Value: ")
      if key not in a_dict:
         a_dict.update({key : value})
      else:
         print("Error. Key already exists.")
   elif choice == "r":
      key = input("key to remove: ")
      if key in a_dict:
         a_dict.pop(key, None)
      else:
         print("Key not found.")
   
   elif choice == "f":
      key = input("Key to locate: ")
      if key in a_dict:
         print("Value: ",a_dict.get(key))
      else:
         print("Key not found.")
      

def dict_to_tuples(dict_object):
   value_key_list = []
   for key, val in dict_object.items():
      value_key_list.append((key, val))
   return value_key_list

# Do not change this main function
def main():
   more = True
   dictionary = {}
   
   while more:      
      choice = menu_selection()
      execute_selection(choice, dictionary)
      again = input("More (y/n)? ")
      more = again.lower() == 'y'
   
   dictlist = dict_to_tuples(dictionary)
   print(sorted(dictlist))

main()

   


