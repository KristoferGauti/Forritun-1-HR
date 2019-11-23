num = int(input("Input an int: ")) # Do not change this line
counter = 1

while counter < num:
    print(counter)
    counter += 1
    

#dæmi 2
num = int(input("Input an int: ")) # Do not change this line =
counter = 0
odd = 1

while counter < num:
    print(odd)
    odd += 2


#dæmi 3

num = int(input("Input an int: ")) # Do not change this line
numbers = []

while num != 10:
    numbers.append(num)
    
        
    num = int(input("Input an int: ")) # Do not change this line

print(sum(numbers))

#dæmi 3
num = 1
n = int(input("Input an int: ")) # Do not change this line

while n >= num:
    if n %num == 0:
        print(num)
    num += 1

#dæmi 4
n = int(input("Input a natural number: ")) # Do not change this line
num = 1
factors = []

while n >= num:
    if n %num == 0:
        factors.append(num)
    num += 1


prime = False #starting bool value = false 

#if the numbers has two factors, the number is a prime number    
if len(factors) == 2: 
    prime = True


# Do not changes the lines below
if prime:
    print("Prime")
else:
    print("Not prime")

#dæmi 5
AB = 144
CAB = AB*AB

print(CAB)
##print(str(CAB)[-2] + str(CAB)[-1])
AB = 1
CAB = str(int(AB**2))
last_digits = int(str(CAB)[-2:])

while len(str(CAB)) != 3:
    AB += 1
    CAB = AB**2

while AB != last_digits:
    AB += 1
    CAB = AB**2
    last_digits = int(str(CAB)[-2:])

print(AB)

#dæmi 7
hole = 1


while hole <= 18:
    print("Par of hole "+str(hole)+":")
    par = int(input())
    print("Score on hole "+str(hole)+":")
    score = int(input())
    
    if par == score+3:
        print("albatross")
    elif par == score+2:
        print("eagle")
    elif par == score+1:
        print("birdie")
    elif par == score:
        print("par")
    elif par == score+1:
        print("bogey")
    elif par == score-2:
        print("double bogey")
    elif par == score-3:
        print("triple bogey")
    elif par > score-3:
        print("bad hole")
    elif par < score+3:
        print("invalid score")
        
    hole += 1


    
   
    


        
        

    



