import string

def open_file():
   filename = str(input("Enter filename: "))
   try:
      a_file = open(filename,"r")
      return a_file
   except FileNotFoundError:
      print("Filename {} not found".format(filename))
      return False


def states(filename):
   if filename != False:
      states_list = []

      
      for line in filename:
         line_list = line.split()
         if line_list[1].isalpha():
            line_list[0] = line_list[0] + " " + line_list.pop(1)
         #print(line_list)
         
         states_list.append(line_list)

      return states_list

def year():
   try:
      year = int(input("Enter year: "))
      return year
   except ValueError:
      print("Invalid year!")
      return None

def get_index(chosen_year,states_list):
   for index, year in enumerate(states_list[0]):
      #try statement because the first index is state which is not an integer
      try:
         if chosen_year == int(year): 
            return index
      except ValueError:
         continue

   

def get_population(the_index,states_list):
   population_list = []
   #slice the state_list because we only need the population
   without_first_line = states_list[1:] 
   for population in without_first_line:
      population_list.append(population[the_index])

   print(population_list) 
   print(the_index) 

   

def main():
   a_file = open_file()
   #print(a_file)

   the_list = states(a_file)
   #print(the_list)
   user_input = year()
   the_index = get_index(user_input,the_list)


   get_population(the_index,the_list)

   

main()