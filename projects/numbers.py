#Höfundur Kristofer Gauti 


#Dæmi 1
for x in range(10,100):
    first_digit = x//10 #this does the same thing as int(str(x)[0])
    second_digit = x%10 #this does the same thing as int(str(x)[1])

    special_num = (first_digit + second_digit)**2 #the algorithm for special number 
    
    if x == special_num: #if x is special number print it 
        print(special_num)

###Dæmi 2
##
##number_that_has_ten_divisors = 0
##
##while number_that_has_ten_divisors < 99:
##    divisor_int = 1 
##    divisors = [] #a list that has all the divisors
##
##    #this while loop finds all the divisors and append them in to the divisors list
##    while divisor_int <= number_that_has_ten_divisors:
##        if number_that_has_ten_divisors % divisor_int == 0: #if that number that has 10 divisors modulo of divisors int is zero than it is a divisor int  
##            divisors.append(divisor_int) #append the divisor int into our list 
##        divisor_int += 1
##
##    #if the divisors list has 10 divisors numbers, then print them all 
##    if len(divisors) == 10:
##        print(number_that_has_ten_divisors)
##        #print(divisors)
##    number_that_has_ten_divisors += 1
    



for x in range(1,100): #iterates through all 2 digit numbers 
    divisors = 0 # divisors counter
    
    for y in range(1,100): #creates a divisor for the two digit number 
        if x % y == 0: #if the two digit number modulo by the divisor number is equal to zero 
            divisors += 1 #then the divisor counter starts to count
            
    if divisors == 10: 
        print(x) #print the 2 digit number/numbers



    
    
