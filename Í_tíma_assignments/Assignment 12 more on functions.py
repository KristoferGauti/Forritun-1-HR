# def music_func(music,group,singer):
#    print("The best type of music is",music)
#    print("The best music group is",group)
#    print("The best lead vocalist is",singer)

# def main():
#     music, group, singer = input("Input music, group, singer: ").split(',')
#     music_func(music, group, singer)
#     music_func(music = "Classic Rock",group = "The Beatles",singer = "Freddie Mercury")

# main()


#Dæmi 2
# def sort_list(the_list):
#    the_list.sort()


# def get_list():
#    a = input("")
#    num_list = []
#    while a.isdigit():
#       num_list.append(int(a))
#       a = input("")
   
#    return num_list


# # Do not modify this part
# def main():
#     a_list = get_list()
#     print(a_list)
#     print(sort_list(a_list))
#     print(a_list)
    
# main()

#Dæmi 3
# import string
# def open_file(filename):
#    try:
#       file_object = open(filename,"r")
#       return file_object
#    except FileNotFoundError:
#       return False

# def unique_words_list(filename):
#    word_list_withpunc = []
#    punctuation = '!"#$%&\'()*+,./:;<=>?@[\\]^_`{|}~'
   

#    for line in filename:
#       word_list_withpunc += line.split()

#    nopunctuation_words = ["".join(n for n in s if n not in punctuation)for s in word_list_withpunc]
   
#    unique_words = list(set(nopunctuation_words))

#    print(sorted(unique_words))
         

# def main():
#    filename = input("Enter filename: ")
#    file_name = open_file(filename)
#    if file_name == False:
#       pass
#    else:
#       unique_words_list(file_name)
      
# main()

#Dæmi 4

# def merge_lists(list1,list2):
#    list3 = list1 + list2
#    for word in list3:
#       if list3.count(word) >= 2:
#          list3.remove(word)

#    return sorted(list3)


# # Main program starts here - DO NOT change it
# list1 = input("Enter elements of list separated by commas: ").split(',')
# list2 = input("Enter elements of list separated by commas: ").split(',')
# print(merge_lists(list1, list2))

def check_eight(list1):
   for i in range(len(list1) - 1):
      if list1[i] == "8" and list1[i] == list1[i+1]:
         return True
      else:
         return False

def check_digit(elements_list):
   for word in element_list:
      for digit in word:
         if digit.isdigit():
            return True
   return False

def main():
   elements_list = input("Enter elements of list separated by commas:").split(",")
   
   if check_digit(elements_list):
      eight = check_eight(elements_list)
      print(eight)
   else:
      print("Error - please enter only integers.")

main()