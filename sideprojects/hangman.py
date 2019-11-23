import random

# Constants to be used in the implementation
WORD_LIST = [
"lion", "umbrella", "window", "computer", "glass", "juice", "chair", "desktop",
 "laptop", "dog", "cat", "lemon", "cabel", "mirror", "hat"
           ]
MAX_GUESS = 12
CHAR_PLACEHOLDER = '-'


def random_seed():
   seed = int(input("Random seed: "))
   random.seed(seed)

def guess_word(the_word):
   length_word = CHAR_PLACEHOLDER * len(the_word)
   length_word_list = [line for line in length_word]

   print("The word you need to guess has {} characters".format(len(the_word)))
   print("Word to guess: {}".format(" ".join(length_word_list)))
   return length_word, length_word_list

def check_win(counter, char_lines_list, the_word):
   if counter == 12:
      print("You lost! The secret word was {}".format(the_word))
      return False

   if CHAR_PLACEHOLDER not in char_lines_list:
      print("You won!")
      return True


def game_loop(char_lines, the_word, char_lines_list):
   choose = input("Choose a letter: ")
   guess_counter = 0
   old_guesses = []

   while choose.isalpha():
      if choose not in old_guesses:
         old_guesses.append(choose)

         if choose in the_word:
            for index, char in enumerate(the_word):
               if choose == char:
                  if char_lines_list[index] == CHAR_PLACEHOLDER:
                     char_lines_list[index] = choose
                     
            guess_counter += 1
            print("You guessed correctly!")
            print("You are on guess {}/{}".format(guess_counter, MAX_GUESS))
            print("Word to guess: {}".format(" ".join(char_lines_list)))

         else:
            print("The letter is not in the word!")
            guess_counter += 1
            print("You are on guess {}/{}".format(guess_counter, MAX_GUESS))
            print("Word to guess: {}".format(" ".join(char_lines_list)))

      else:
         print("You have already guessed that letter!") 
         print("You are on guess {}/{}".format(guess_counter, MAX_GUESS))
         print("Word to guess: {}".format(" ".join(char_lines_list)))
         guess_counter += 0

      #Check if the user has won 
      win = check_win(guess_counter, char_lines_list, the_word)

      if win == True:
         print("word to guess: {}".format(" ".join(char_lines_list)))
         break
      elif win == False:
         break

      choose = input("Choose a letter: ")


def main():
   random_seed()
   random_word = random.choice(WORD_LIST)
   char_lines, char_lines_list = guess_word(random_word)

   game_loop(char_lines, random_word, char_lines_list)



main()