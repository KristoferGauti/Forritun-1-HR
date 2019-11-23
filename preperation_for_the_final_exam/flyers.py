def open_file(filename):
   try:
      file_object = open(filename,"r")
      return file_object
   except FileNotFoundError:
      return False

def print_lines(filename):
   line_list = [line.split() for line in filename]


   name_list = []
   country_list = []
   for line in line_list:
      name_list.append(line[0])
      country_list.append(line[1])

   sorted_name_list = sorted(name_list)

   return sorted_name_list, country_list, line_list
   

def remove_duplicates(sorted_names, countries):
   no_dupl_names = []
   for name in sorted_names:
      if name not in no_dupl_names:
         no_dupl_names.append(name)

   return sorted(no_dupl_names)

def been_to_most_countries(line_list):
   name_list = [line[0] for line in line_list]

   maximum_name = max(name_list, key = name_list.count)
   maximum_number = name_list.count(maximum_name)

  



   return maximum_name, maximum_number


def countries_book(lines_list, no_dupl_names, maximum_name, maximum_number):
   #print(lines_list)
   sorted_lines_list = sorted(lines_list)
   
   old_country = []
   for name in no_dupl_names:
      print("{}: ".format(name))
      old_country.clear()
      for line in sorted_lines_list:
         if name == line[0]:
            if line[1] in old_country:
               pass
            else:
               old_country.append(line[1])
               print("\t{}".format(line[1]))

   print("\n\n{} has been to {} countries".format(maximum_name, maximum_number))


def main():
   filename = "text_files/flights.txt" #"flights.txt"
   file_obj = open_file(filename)
   if file_obj == False: #text_files/flights.txt
      pass
   else:
      sorted_names, countries, lines_list = print_lines(file_obj)
      no_dupl_names = remove_duplicates(sorted_names,countries)
      maximum_name, maximum_number = been_to_most_countries(lines_list)
      been_to_most_countries(lines_list)
      
      countries_book(lines_list, no_dupl_names, maximum_name, maximum_number)


main()