import random

def main():
    word = input("Please enter a word: ")
    print(scramble(word)) 

def scramble(word):
    char1 = random.randint(1, len(word)-2)
    char2 = random.randint(1, len(word)-2)
    
    while char1 == char2:
        char2 = random.randint(1, len(word)-2)

    newWord = ""

    for i in range(len(word)):
        if i == char1:
            newWord = newWord + word[char2]
        elif i == char2:
              newWord = newWord + word[char1]

        else:

            newWord = newWord + word[i]

    return newWord

main()