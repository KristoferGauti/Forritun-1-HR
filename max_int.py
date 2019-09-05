
num_int = int(input("Input a number: "))    # Do not change this line
listi = []

while num_int >= 0:
    listi.append(num_int)
    num_int = int(input("Input a number: ")) 

max_int = max(listi)


print("The maximum is", max_int)    # Do not change this line
