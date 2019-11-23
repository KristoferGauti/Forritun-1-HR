import string


def open_file(name):
   """Opens the file"""
   a_file = open(name,"r")
   return a_file
   

def just_letters(filename): 
   """Removes the punctuation from the file"""

   letters = "" #string that contains the alphabetical letters, no punctuations

   for line in filename:
      for letter in line:
         letters += letter
      

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
      lina = line[0: -1]
      first = words[0]
      last = words[-2]
      middle = words[1:-2]
      newMiddle = ''

      if len(middle) == 0:
         newMiddle += middle

      elif len(middle) % 2 == 0:
        for index in range(0, len(middle), 2):
          newMiddle += middle[index+1]
          newMiddle += middle[index]
      else:
        for index in range(1, len(middle), 2):
          newMiddle += middle[index]
          newMiddle += middle[index-1]
        newMiddle += middle[-1]

      if line[-1] in string.punctuation:
         print(first + newMiddle + last + line[-1].strip(), end=' ')
      else:
        print(first + newMiddle + last, end=' ')

   
   
         




def main():
   #Function calls
   name = str(input("Enter name of file: "))
   try:
      filename = open_file(name)

      scrambled_words(filename)
      #switch_char(filename)
   except:
      print('File', name, 'not found!')
   


main()
