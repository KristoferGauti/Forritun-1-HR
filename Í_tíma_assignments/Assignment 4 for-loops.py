#Dæmi 1
num = int(input("Input an int: "))  # Don not change this line

for x in range(1,num):
    print(x)

#Dæmi 2
num = int(input("Input an int: "))
odd_num = 0

for x in range(1,num+1,1):
    print(odd_num+1)
    odd_num += 2

#Dæmi 3
summa = 0
grain = 1
for x in range(64):
    summa += grain
    grain*=2
    
print(summa)

#Dæmi 4
m = int(input("Input the first integer: ")) # Do not change this line
n = int(input("Input the second integer: ")) # Do not change this line

for i in range(1,m+1):
    if m % i == 0 and n % i == 0:
        dividor = i

print(dividor)

#Dæmi 5
num = int(input("Input an int: ")) # Do not change this line

summa = 0
for x in range(1,num+1):
    for i in range(1,x+1):
        summa += i
        
    print(summa)
    summa = 0

    
#dæmi 6

top_num = int(input("Upper number for the range: ")) # Do not change this line

n = 1

for n in range(1,top_num):
    if n == 3 or n == 5:
        continue
    perfect_number= 2**n*((2**(n+1))-1)#formula
    if perfect_number > top_num:
        break

    print(perfect_number)
    

