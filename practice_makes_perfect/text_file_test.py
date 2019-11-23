def example_1():
   data_file = open("input.txt","r")

   for line in data_file:
      print(line,end="") #have the end empty so it does not print in double space format
   print()

   a_str = "this., "

   b_str = a_str.strip("., ") #The strip method removes the characters that are passed in its arguments
   print(b_str)

def clean_word(word):
   return word.strip().lower()

#string = clean_word("SAN FRAnsIsCo")
#print(string)

def get_vowels_in_word(word):
   """Returns vowels in a string word - include repeats"""

   vowels = "aeiou"
   vowels_in_word = ""
   for char in word:
      if char in vowels:
         vowels_in_word += char

   return vowels_in_word

#word = "create"
#print(get_vowels_in_word(word))

def example_2():
   """Prints all the words in a file and puts them in to a list"""

   data_file = open("input.txt","r")
   for word in data_file:
      wordsplit = word.split() #split on a space
      print(wordsplit)
      


