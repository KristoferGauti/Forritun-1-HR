def open_file(filename):
   try:
      file_object = open(filename,"r")
      return file_object
   except FileNotFoundError:
      return False

def line_list(file_obj):
   department_list = []
   for line in file_obj:
      line_list = line.split()
      line_list = [int(x) for x in line_list]
      department_list.append(line_list)
      
   return department_list
   

def print_average(the_list):
   average_list = []
   for line in the_list:
      average_list.append(round(sum(line) / len(line),1))

   return average_list

def print_formatted(average_list, line_list):
   print("Average sales:\n")
   for department_no, average in enumerate(average_list, start = 1):
      print("Department no. {}: {}".format(department_no, average))
      

def main():
   filename = input("Enter filename: ")
   file_obj = open_file(filename)

   if file_obj == False:
      pass
   else:
      lines = line_list(file_obj)
      average_list = print_average(lines)

      print_formatted(average_list, lines)
                    

main()