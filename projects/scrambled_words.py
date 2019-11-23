"""Programmer: Kristofer Gauti Þórhallsson"""

import string

def open_file(name):
   """Opens the file"""

   a_file = open(name,"r")
   return a_file
   

def just_letters(filename): 
   """gets every character in every word"""

   letters = "" #string that contains the alphabetical letters

   for line in filename:
      for letter in line:
         letters += letter

   return letters


def scrambled_words(filename):
   """Scrambles the words but not the first and the last letter"""

   for line in filename:
      words = just_letters(line) #Charaters in every line
      #print(words)
      
      #lina = line[0: -1]
      first = words[0] # First letter of words
      last = words[-2] # Last letter of words
      middle = words[1:-2] # Removing first and last characters from words
      new_middle = '' # New middle string, used in next phase
      
      if len(middle) % 2 == 0: #if the middle character's length is an even number
         for index in range(0, len(middle), 2):
            new_middle += middle[index+1] #append the 2nd character to new_middle
            new_middle += middle[index] #and then the 1st character to new_middle

      else: #middle characters length are odd number
         for index in range(1, len(middle), 2):
            new_middle += middle[index] #append the 2nd character to new_middle
            new_middle += middle[index-1] #append the 1st character to new_middle
         new_middle += middle[-1] #append the last character to new_middle, because the length is an odd number


      #If the length of the variable words is bigger or equal to three print(first + new_middle + last)
      #otherwise clean the whitespaces and print the variable words
      print((first + new_middle + last) if len(words) >= 3 else words.strip(), end=" ")

def main():
   name = str(input("Enter name of file: "))
   try:
      filename = open_file(name)
      scrambled_words(filename)

   except:
      print('File', name, 'not found!')
   
main()
