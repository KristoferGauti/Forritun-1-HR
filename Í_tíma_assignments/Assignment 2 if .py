#Dæmi 1 
num = int(input("Input a number: ")) # Do not change this line

# Fill in the missing code

if num != False:
    print(True) # Do not change this line
else:
    print(False) # Do not change this line   

#dæmi 2
num = int(input("Input a number: ")) # Do not change this line

# Fill in the missing code below

if num < 0:
    print("Negative") # Do not change this line
elif num > 0:
    print("Positive") # Do not change this line
else:
    print("Zero") # Do not change this line

#dæmi 3
num1 = int(input("First number: ")) # Do not change this line
num2 = int(input("Second number: ")) # Do not change this line
num3 = int(input("Third number: ")) # Do not change this line

# Fill in the missing code below


if (num1 >= num2 and num1 >= num3) == True:
    max_int = num1
    
elif (num2 >= num1 and num2 >= num3) == True:
    max_int = num2
    
elif (num3 >= num2 and num3 >= num1) == True:
    max_int = num3


print("The maximum is: ", max_int) # Do not change this line
    
#dæmi 4
grade = float(input("Input a grade: ")) # Do not change this line

# Fill in the missing code below

if grade > 10.0 or grade < 0:
    print("Invalid grade!") # Do not change this line
    
elif 5.0 <= grade <= 10.0:
    print("Passing grade!") # Do not change this line

else:
    print("Failing grade!") # Do not change this line


#dæmi 5 hlaupar algoritmi 
year = int(input("Input a year: ")) # Do not change this line

leapyear = year / 400


if year / 4 == year // 4:
    if year / 100 == year // 100:
        if year / 400 == year // 400:
            leapyear = True
        else:
            leapyear = False
    else:
        leapyear = True
else:
    leapyear = False
print(leapyear)

#Dæmi 6 dice game 
d1 = int(input("Input first dice: ")) # Do not change this line
d2 = int(input("Input second dice: ")) # Do not change this line
summa = d1+d2

# Fill in the missing code below
if 1 <= d1 <=6 and 1 <= d2 <= 6:
    if summa == 7 or summa == 11:
        print("Winner")
    elif summa == 2 or summa == 3 or summa == 12:
        print("Loser")
    else:
        print(summa)

else:
    print("Invalid input")

#Dæmi 7 ticket price
age = int(input("Input age: ")) # Do not change this line
ticket = float(30)

if age >= 65:
    ticket *= 0.5
    print(ticket)
elif age <= 5:
    ticket = 0.0
    print(ticket)
else:
    ticket = 30.0
    print(ticket)

    
    

                
        


    

