def open_file():
   """Opens the file and catches the error if the user 
   has input anything else than the filename"""

   filename = str(input("Enter filename: "))
   try:
      a_file = open(filename,"r")
      return a_file
   except FileNotFoundError:
      print("Filename {} not found!".format(filename))
      return False

def states(filename):
   """creates a list with all the states. if the state has two
   words then we pop the second word and assign the zero index with the concatenation of the 
   first word and the second word"""

   if filename != False:
      states_list = []

      for line in filename:
         line_list = line.split()
         if line_list[1].isalpha():
            line_list[0] = line_list[0] + " " + line_list.pop(1)
         
         states_list.append(line_list)

      return states_list
   
def get_year_index(first, states_list):
   """Returns the index (or position) of the 
   year that the user has input to determine the 
   population later on"""
   first_line_list = first.split()
   while True:
      chosen_year = str(input("Enter year: "))
      try:
         for index, year in enumerate(first_line_list):
            if chosen_year == year:
               return index

         print("Invalid year!")
               
      except ValueError:
         continue  

def get_population(index, states_list):
   """Gets the population of inputted year"""
   population_list = []
   
   for population in states_list:
      population_list.append(population[index])

   return population_list
   
   
def united_states(the_list):
   """Returns a list with all the states in the text file"""
   united_states_list = []
   for line in the_list:
      united_states_list.append(line[0])
      
   return united_states_list[1:] #slice the first index because it is "State"
   
def get_min_max_int_population_list(states, pop):
   """Returns the population's minimum and maximum value
   It also returns the integer population list"""
   int_pop_list = []

   for num in pop:
      int_pop = int(num)
      int_pop_list.append(int_pop)
   
   min_pop = min(int_pop_list)
   max_pop = max(int_pop_list)
   
   return min_pop, max_pop, int_pop_list 

def get_min_state_index(states, pop):
   """Gets the minimum population value index"""
   min_num, max_num, int_pop_list = get_min_max_int_population_list(states,pop)
   min_list = []
   max_list = []

   for min_index, population in enumerate(int_pop_list): 
      if population == min_num:
         min_list.append(min_index)

   for max_index, population in enumerate(int_pop_list):
      if population == max_num:
         max_list.append(max_index)

   return min_list[0], max_list[0], min_num, max_num

def min_max_states_tuples(states_list, index_min, index_max, min_pop, max_pop):
   """index - 1 because the population list did not have the 
   first line included and also because the states list did have
   "states" as its first index"""

   min_tuple = (min_pop,states_list[index_min - 1])
   max_tuple = (max_pop,states_list[index_max - 1])

   print("Minimum:",min_tuple)
   print("Maximum:",max_tuple)

def main():
   a_file = open_file()

   if a_file == False:
      return None
   else:
      #Read the first line of the file
      first_line = a_file.readline()
      #The original list
      the_list = states(a_file) 
      #The list with just the states
      united_states_list = united_states(the_list) 
      #The index of the year
      index = get_year_index(first_line, the_list)
      #The population
      population = get_population(index, the_list)

      minimum_index, maximum_index, min_pop, max_pop = get_min_state_index(united_states_list, population)
      min_max_states_tuples(united_states_list, minimum_index, maximum_index, min_pop, max_pop)

main()