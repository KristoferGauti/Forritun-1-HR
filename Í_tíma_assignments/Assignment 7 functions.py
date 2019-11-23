# find_min function definition goes here
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

def find_min(first,second):
   if first > second:
      minimum = second
      return minimum 
   elif first < second:
      minimum = first
      return minimum
   else:
      return first
   
    
minimum = find_min(first,second)
print("Minimum: ", minimum)


#Dæmi 2
def upper(user_input):
   upper = 0
   lower = 0
   for letter in user_input:
      if letter.isupper() == True:
         upper += 1
      if letter.islower() == True:
         lower += 1
   return upper,lower

user_input = input("Enter a string: ")


upper, lower = upper(user_input)

print("Upper case count: ", upper)
print("Lower case count: ", lower)


#Dæmi 3 
def num_range(num):
   if 1 < num < 555:
      print(num,"is in range")

   elif num <= 1:
      print(num,"is outside the range!")

   else:
      print(num,"is outside the range!") 

num = int(input("Enter a number: "))

num_range(num)


#Dæmi 4
def is_prime(num):
   if (num <= 1) : 
      print(num,"is not a prime")
   elif (num <= 3) : 
      print(num,"is a prime")

   elif (num % 2 == 0 or num % 3 == 0): 
      print(num,"is not a prime")

   else:
      i = 5
      while(i * i <= num) : 
         if (num % i == 0 or num % (i + 2) == 0) : 
            print(num,"is not a prime")
         i = i + 6
      
      print(num,"is a prime")
    
num = int(input("Input an integer greater than 1: "))


is_prime(num)


#Dæmi 5
def is_palindrome(in_str):
   letters = ""
   for letter in in_str.lower():
      if letter.islower() == True:
         letters += letter
   
   if letters == letters[::-1]:
      return True
   else:
      return False


in_str = input("Enter a string: ")

palindrome = is_palindrome(in_str)

if palindrome == True:
   print("\"{}\"is a palindrome".format(in_str))
elif palindrome == False:
   print("\"{}\" is not a palindrome".format(in_str))


#Dæmi 6

def fibo(lenght):
   fibonacci = "" #1 1 2 3 5 8 13 21
   the_sum = 0
   number1 = 1
   number2 = 1
   for x in range(1,lenght+1):
      if x == 1:
         fibonacci += str(number1) + " "  
      elif x == 2:
         fibonacci += str(number2) + " "
      elif x > 2:
         the_sum = number2 + number1
         number1 = number2
         number2 = the_sum
         fibonacci += str(the_sum) + " "
   return fibonacci


n = int(input("Input the length of Fibonacci sequence (n>=1): "))

fibonacc = fibo(n)
print(fibonacc)