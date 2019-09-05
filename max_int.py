
num_int = int(input("Input a number: "))    # Do not change this line
listi = []

while num_int >= 0:
    listi.append(num_int)
    num_int = int(input("Input a number: ")) 

max_int = max(listi)


print("The maximum is", max_int)    # Do not change this line

#dæmi 2
n = int(input("Enter the length of the sequence: ")) # Do not change this line
listi = []

n_sum = 0

for x in range(1,n+1):
    if x <= 3:
        n_sum = x
        listi.append(x)
    else:
        next_num = (listi[x-2] + listi[x-3] + listi[x-4])
        listi.append(next_num)

for x in listi:
    print(x,end=" ")
    
        
    
            
    
    
    

