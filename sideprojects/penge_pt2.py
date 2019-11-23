"""Author: Kristofer Gauti Þórhallsson"""

"""This program can calculate how much money you have spent monthly.
Pass in a text file with all your spendings this month"""


def file_object(filename):
   try:
      file_object = open(filename,"r")
      return file_object
   except FileNotFoundError:
      print("File {} not found!".format(filename))
      return False

def get_values(file_obj):
   """removes the dot from numbers which 
   are seperated with a dot. For instance 1.347"""

   numbers = [line.strip()for line in file_obj]
   
   str_numbers = []
   for num in numbers:
      if "." in num:
         new_num = num.replace(".","")
         str_numbers.append(new_num)
      else:
         str_numbers.append(num)

   return str_numbers

def get_negative_num_list(str_numbers):
   """Returns the negative numbers 
   provided in the text file"""

   int_list = [int(num) for num in str_numbers]

   negative_num_list = []
   for negative_num in int_list:
      if negative_num < 0:
         negative_num_list.append(negative_num)

   return negative_num_list

def calculate_results(neg_nums):
   """Converts all the negative numbers to positive and 
   returns the total amonth you have spent"""

   positive_num_list = [(num * (-1)) for num in neg_nums]

   return sum(positive_num_list) 

def print_nicely(results, neg_nums):
   print()
   print("You paid {} times with your debit card this month".format(len(neg_nums)))
   print("You have spent {}kr this month".format(results))
   print()


def main():
   filename = input("Enter a filename: ")

   a_file = file_object(filename)
   if a_file == False:
      pass
   else:
      str_numbers = get_values(a_file)
      neg_nums = get_negative_num_list(str_numbers)
      results = calculate_results(neg_nums)

      print_nicely(results, neg_nums)

main()