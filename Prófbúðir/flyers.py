"""text_files/flights.txt"""
def read_file(filename):
   try:
      file_obj = open(filename,"r")
      return file_obj
   except FileNotFoundError:
      print("File {} not found".format(filename))
      return False 

def line_list(file_obj):
   flyers_list = []
   for line in file_obj:
      line_list = line.split()
      flyers_list.append(line_list)
   
   return flyers_list

def make_dict(flyers_list):
   flyers_dict = {}
   for line in flyers_list:
      if line[0] not in flyers_dict:
         flyers_dict[line[0]] = [line[1]]
      else:
         if line[1] not in flyers_dict[line[0]]: #remove duplicates countries
            flyers_dict[line[0]] += [line[1]]

   return flyers_dict

def name_sorted(the_dict):
   name_list = []
   for name in the_dict.keys():
      name_list.append(name)

   return sorted(name_list)

def get_max(the_dict):
   max_val = 0
   max_name = ""
   for name, country_list in the_dict.items():
      curr_val = len(country_list)
      if curr_val > max_val:
         max_val = curr_val
         max_name = name

   return max_name, max_val


def pretty_print(the_dict, sorted_names, max_name, max_val):
   for key, value in the_dict.items():
      for name in sorted_names:
         if key == name:
            print("{}:".format(name))
            for country in value:
               print("\t{}".format(country))
   print("\n\n{} has been to {} countries".format(max_name, max_val))

def main():
   """
   read from file
   make dict
   print names
   print names and countries
   print frequent fliers
   """
   filename = input("Enter a file: ")
   file_obj = read_file(filename)
   if file_obj == False:
      pass
   else:
      flyer_list = line_list(file_obj)
      the_dict = make_dict(flyer_list)

      name_sorted_list = name_sorted(the_dict)
      max_name, max_val = get_max(the_dict)

      pretty_print(the_dict,name_sorted_list, max_name, max_val)


main()
