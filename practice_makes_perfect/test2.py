import string
from random import randint


def open_file(name):
   """Opens the file"""
   a_file = open(name,"r")
   return a_file
   

def just_letters(filename): 
   """Removes the punctuation from the file"""

   letters = "" #string that contains the alphabetical letters, no punctuations

   for line in filename:
      for letter in line:
         if letter not in string.punctuation:    #if letter does not have a punctuation: letters += letter
            letters += letter
         else:
            letters += " "

   return letters

def not_first_not_last_char(filename):
   """Returns the all the characters in each word,
    but not the first and the last character"""
   characters = ""
   
   for line in filename:
      no_firstandlast_letters = line[1:-2] # -2 because of the \n character
      if len(line) == 3:
         characters += ""
      else:
         characters += no_firstandlast_letters + " "
      
   
   return characters
   
                           #!!!!#
def switch_char(filename): #!!!Þetta hérna fall virkar ekki alveg að brengla stafina á milli firsta og síðasta stafinn í orðinu
   """Switching the characters starting from right to left"""
   switch_char = ""
   char = not_first_not_last_char(filename)   
   print(char)
   
   
   for x in range(0, len(char),2):
      if char[x + 1].strip() == "": #if the last character is a space, then append the character + a space 
         switch_char += char[x] + " "
      else:
         switch_char += char[x + 1] + char[x] #concatinate the second letter with the first letter
      
      
   
   print(switch_char)

   
   return switch_char


def scrambled_words(filename):
   for line in filename:
      words = just_letters(line) #Charaters in every line
      #print(words)
      brengla = list()
      
      for index, letters in enumerate(line):

         if 0 < index < len(words)-2:
            brengla.append(letters)

            
      for index, letters in enumerate(line):
         if index == 0:
            print(letters,end="")

         if 0 < index < len(words)-2:
            randomIndex = randint(0, len(brengla)-1)
            print(brengla[randomIndex],end="") #setja hvern staf fyrir sig
            brengla.pop(randomIndex)

         if index == len(words)-2: # -2 because we dont want to include the \n character
            print(letters,end=" ")
            #print(len(char))
            

def main():
   #Function calls
   name = str(input("Enter name of file: "))
   try:
      filename = open_file(name)

      scrambled_words(filename)
      #switch_char(filename)
   except:
      print('File', name, 'not found!')
   



f = open("test.txt")

switch_char(f)

main()
