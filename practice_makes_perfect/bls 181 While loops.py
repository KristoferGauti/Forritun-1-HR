#Dæmi 1
num = 17

for x in range(100,1000):
    if x % num == 0:
        print(x)

#Dæmi 4
grade = int(input("Input a grade"))

if grade <= 40:
    print("You got a D on the final test")
elif 40 < grade <= 60:
    print("You got a C on the final test")
elif 60 < grade <= 80:
    print("You got a B on the final test")
elif 80 < grade <= 100:
    print("you got an A on the final test")

#Dæmi 6
num1 = int(input("input number 1"))
num2 = int(input("input number 2"))
num3 = int(input("input number 3"))


if (num1 >= num2 and num1 >= num3) == True:
    big = num1
elif (num2 >= num1 and num2 >= num3) == True:
    big = num2
elif (num3 >= num2 and num3 >= num1) == True:
    big = num3 

print("The largest number is",big)

#Dæmi 18a
listi = []
x = int(input("Enter an integer"))

for i in range(1,x+1):
    listi.append(i)
    print(str(listi)," + ".join(listi))

x = int(input("Input an Integer: "))

sum_num = 0

for x in range(1,x+1):
    
    for y in range(1,x):
        print(y,end=" + ")
        sum_num += y
        
    sum_num += x
    print(x,end=" = ")
    print(sum_num)


#Dæmi 20
num = input("Input an integer: ")

while True:
    if num.isdigit() == True:
        print("The integer is",num)
        break
    else:
        print("did not work")
        num = input("Input an integer: ")



    
    



        
        
        
        



