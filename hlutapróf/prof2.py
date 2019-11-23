# def last_two_removed(num_list):
#    float_list = []

#    for num in num_list:
#       float_list.append(float(num))

#    sort_float_list = sorted(float_list)
#    sort_float_list_two_lowest_removed = sort_float_list[2:]

#    return sort_float_list_two_lowest_removed


# def get_score(num_list):
#    if len(num_list) < 2:
#       print("At least two scores needed!")
#    else:
#       sum_list = []
#       the_list = last_two_removed(num_list)

#       for num in the_list:
#          sum_list.append(float(num))

#       print("Sum of scores (two lowest removed): ",sum(sum_list))
   



# def main():
#    num_list = str(input("Enter scores separated by space: ")).split()

#    get_score(num_list)

# main()

# def open_file(a_file):
#    try:
#       filename = open(a_file, "r")
#       return filename
#    except FileNotFoundError:
#       print("File",a_file,"not found!")
#       return False

# def word_list_punctuation_list(file_object):
#    punctuation = []
#    words = []

#    for line in file_object:
#       word_strip = line.strip()
#       word_list = word_strip.split()

#       for char in line:
#          if char == ",":
#             punctuation.append(char)
#          elif char == ".":
#             punctuation.append(char)
#          elif char == "!":
#             punctuation.append(char)
#          elif char == "?":
#             punctuation.append(char)

#       for word in word_list:
#          words.append(word)

#    print(len(words)+len(punctuation))
   

# def main():
#    a_file = str(input("Enter filename: "))
#    file_object = open_file(a_file)

#    if file_object == False:
#       pass
#    else:
#       word_list_punctuation_list(file_object)
   
# main()

# Les inn heiltölur inn í tvo lista (bil á milli staka í inntaki), breytir listunum í röðuð mengi og prentar mengin út.  Ekki þarf að villutékka inntakið. 
# Býr til raðað sniðmengi mengjanna tveggja og prentar það út.
# Býr til raðað sammengi mengjanna tveggja og prentar það út. 

def sets(set1, set2):
   string_set1 = set1.split()
   string_set2 = set2.split()

   set_list1 = []
   set_list2 = []

   for string_1 in string_set1: 
      set_list1.append(int(string_1))

   for string_2 in string_set2:
      set_list2.append(int(string_2))


   sort1 = sorted(set_list1)
   sort2 = sorted(set_list2)

   final_set1 = set(sort1)
   final_set2 = set(sort2)


   return list(final_set1), list(final_set2)
   

def intersection(set1,set2):
   intersec = []
   for num in set1:
      if num in set2:
         intersec.append(num)

   return intersec


def main():
   set1 = input("Enter elements of a list separated by space: ")
   set2 = input("Enter elements of a list separated by space: ")

   
   sets(set1,set2)
   set1_list, set2_list = sets(set1,set2)

   inter = intersection(set1_list,set2_list)

   print("Set 1: ",sorted(list(set1_list)))
   print("Set 2: ",sorted(list(set2_list)))
   print("Intersection: ",sorted(inter))
   print("Union:",sorted(list(set(set1_list + set2_list))))


main()