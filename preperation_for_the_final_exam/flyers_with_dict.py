def open_file(filename):
   try:
      file_object = open(filename,"r")
      return file_object
   except FileNotFoundError:
      return False

def get_dict(file_obj):
   line_dict = {}

   for line in file_obj:
      line_list = line.split()
      name = line_list[0]
      country = line_list[1]
      
      if name not in line_dict:
         line_dict[name] = (country),
      else:
         if country not in line_dict[name]:
            line_dict[name] += (country),

   return line_dict


def get_max(file_obj):
   line_list = [line.split() for line in file_obj]
   name_list = [line[0] for line in line_list]
   

   maximum_name = max(name_list, key = name_list.count)
   maximum_number = name_list.count(maximum_name)

   return maximum_name, maximum_number
   
   
def print_formatted(the_dict, name, max_value):
   for key, value in the_dict.items():
      print("{}:".format(key))
      value_list = list(value)

      for country in sorted(value_list):
         print("\t{}".format(country))

   print("\n\n{} has been to {} countries".format(name, max_value))


def main():
   filename = input("Enter filename: ")
   file_obj = open_file(filename)
   open_again = open_file(filename)

   if file_obj == False:
      pass
   else:
      the_dict = get_dict(file_obj)
      name, max_value = get_max(open_again)

      print_formatted(the_dict, name, max_value)


main()