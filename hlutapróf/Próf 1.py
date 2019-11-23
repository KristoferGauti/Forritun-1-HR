age = int(input("Enter your age: "))

if 0 <= age <= 34:
    print("Young")
elif 35 <= age <= 50:
    print("Mature")
elif 51 <= age <= 69:
    print("Middle-aged")
elif age > 70:
    print("Old")
else:
    print("Invalid age")


#Dæmi 2
num = 17

for x in range(100,1000):
    if x % num == 0:
        print(x)


#Dæmi 3
first = int(input("First: "))
step = int(input("Step: "))

counter = first
listi = []
listi.append(first)

while counter <= 100:
    counter += step
    listi.append(counter)
    if sum(listi) >= 100:
        break
        

for x in listi:
    print(x, end=" ")

print()

print("Sum of series: ",sum(listi))
    



#Dæmi 4
n = int(input("Number of Integers: "))


if n > 0:
    print("*")

    for x in range(1,n):
        for y in range(1,x+1):
            print("*",end="")
            
        print("*")
            
            



    
    
