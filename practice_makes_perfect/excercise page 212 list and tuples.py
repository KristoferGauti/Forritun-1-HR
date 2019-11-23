#Excercise 2
#Create a list of the squares of all numbers between 1 and 20.
##list_from_one_to_twenty = [n for n in range(1,21)]
##print(list_from_one_to_twenty)

#Excercise 3
#Create a list of 100 integers whose value and index are the same, for example, L[5]=5.
##L = [n for n in range(0,100)]
##print(L)
##print(L[5]) 

#Excercise 14
#Given a list L = [1,2,3,4], we want to convert the list to the string '1234'. We tried
#''.join([i for i in L]),but it doesn’t work.Fix it.

# L = [1,2,3,4]

# for num in L:
#    string = str(num)
#    print("".join(string),end="")

"""we could also implement this with list comprehension"""

#L = [1,2,3,4]
#print("".join([str(n) for n in L]))

#Excercise 18
#Write a program to combine two lists in such a way that duplicate entries are removed 
#only from the second list, and not from the first.
# list_1 = [1,2,3,4,5,6,7,8,9,10]
# list_2 = [2,4,6,8,10,12,14,16,18]

# for i in list_2:
#    if i in list_1:
#       list_2.remove(i)

# concatenation = list_1 + list_2
# print(sorted(concatenation)) #should print out [1,2,3,4,5,6,7,8,9,10,12,14,16,18]

#Extra Excercise, which was not on page 212. Example of enumerate and .format.
# question = int(input("Enter a number from 1 to 6: "))
# a = [1,2,3,4,5,6]
# print("This is our list:",a)

# for index, num in enumerate(a,start=1):
#    if question == num:
#       if question == 1:
#          print("the number {} is at {}st index of the list".format(num,index))
#       elif question == 2:
#          print("the number {} is at {}nd index of the list".format(num,index))
#       elif question == 3:
#          print("the number {} is at {}rd index of the list".format(num,index))
#       else:
#          print("the number {} is at {}th index of the list".format(num,index))

#Prime number excercise 
# def is_prime(n):
#     """Returns True if the given positive number is prime and False otherwise"""
#     if n == 1:
#         return False

#     if n == 2:
#         return True

#     for i in range(2,n):
#         if n%i == 0:
#             return False
            
#     else:
#         return True

# number = int(input("Input a number: "))
# print(is_prime(number))

#Excercise 33
#Write a program that takes a list as an argument, and moves all
#elements divisible by 13 to a new list.

# num_list = [n for n in range(101)]

# list_with_all_num_divisible_by_13 = []

# for num in num_list:
#    if num % 13 == 0:
#       list_with_all_num_divisible_by_13.append(num)

# print(num_list)
# print(list_with_all_num_divisible_by_13)

#Excercise 34
#Given a list [4,8,9,6,5,4,8,7,8] and using the len and sum functions,
#determine the average value of the integers in the list.
# numbers = [4,8,9,6,5,4,8,7,8]

# average = (sum(numbers))/(len(numbers))

# print(average)

#Excercise 35
#Write a function using a for loop that takes a string S as an
#argument and returns S in reversed order. For example, 
#if S=“stressed”, it should return “desserts.”
# def reverse(S):
#    for x in reversed(S):
#       print(x,end="")
      
# S = input("Enter a word: ")
# reverse(S)

#Excercise 37 nested list comprehension
# L = ['Always', 'look', 'on', 'the', 'bright', 'side', 'of', 'life.'] 
# List1 = [[i.upper(), i.lower(), len(i)] for i in L ]
# print(List1)

#Excercise 38
#Using list comprehension create an expression that sums up 
#all the factors of a number that you input. 
#(Hint: If you input 6, it should print 12 (i.e., 1 + 2 + 3 + 6 = 12).)

# num = int(input("Enter a number "))
# divisors = [x for x in range(1,num+1) if num % x == 0] 

# first = divisors[0]
# middle_num_list = divisors[1:-1]
# last = divisors[-1]

# middle = ""

# for index in middle_num_list:
#    middle += "{}+".format(index)

# print(str(first)+"+"+middle+str(last)+"="+str(sum(divisors)))

#Excercise 54
# def transform(list1,list2,r1,r2):
#    extra_list = list1[r1:r2]
#    reverse = extra_list[::-1]
#    list2.extend(reverse)
#    print(list2)


# def main():
#    list1 = [1,2,3,4,5,6,7,8,9]
#    list2 = [100,200]
#    print("Here is our data: ",list1,"and",list2)
#    r1 = int(input("Enter the number x range: list1[x:y] "))
#    r2 = int(input("Enter the number y range: list1[x:y] "))

#    transform(list1, list2, r1,r2)


# main()

#Sublist:
list1 = [1,2,3,4,5,6,7,8,9,10,11,23,45]

sublist = [list1[i:i+3] for i in range(0,len(list1),3)]
print(sublist)

