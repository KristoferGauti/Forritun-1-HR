#Problem 1.1 
"""Write a program that records input from the user. When a line with the 
string Exit appears, the program should stop recording and output every 
line it has recorded."""

import string 
records = []

user_input = input("Input a number: ")
while user_input.isdigit() and user_input != "Exit" or user_input != "exit": 
   records.append(user_input)
   user_input = input("Input a number: ")


for char in records:
   if char.isalpha():
      records.remove(char)
  
print(records)
