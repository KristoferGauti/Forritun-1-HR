def make_word_list(a_file):
   word_list = []

   for line in a_file:
      line_list = line.split()
      for word in line_list:
         word.lower()
         word.strip(".,")
         if word != "--":
            word_list.append(word)

   return word_list

def make_unique(word_list):
   unique_list = []

   for word in word_list:
      if word not in unique_list:
         unique_list.append(word)

   return unique_list



def main():
   a_file = open("gettysburg.txt","r")
   speech_list = make_word_list(a_file)

   print()
   print()

   print(speech_list)
   print("Word count: ", len(speech_list))
   print("Unique word count", len(make_unique(speech_list)))

main()
