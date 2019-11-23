num = int(input("Enter an integer: "))

cumulative_list = [] #culmination of the numbers
even_num_list = [] #list for even numbers
odd_num_list = [] #list for odd numbers


while num > 0:
    cumulative_list.append(num) #appends to the cumulative list
    print("Cumulative total: ",sum(cumulative_list))



    num = int(input("Enter an integer: "))

#this gets all the values in the cumulative_list
for i in cumulative_list:
    if i % 2 == 0: #if i's modulo is zero, than the numbers are even numbers
        even_num_list.append(i) #append all the even numbers to the even_num_list
    

#this gets all the values in the cumulative_list
for x in cumulative_list:
    if x % 2 != 0: #if x's modulo is not zero, than the numbers are odd numbers
        odd_num_list.append(x) #append all the odd numbers to the odd_num_list
        
print("Largest number: ",max(cumulative_list)) #prints the largest number in the cumulative list
print("Count of even numbers: ",len(even_num_list)) #prints the lenght of the even_num_list
print("Count of odd numbers: ",len(odd_num_list)) #print the lenght of the odd_number_list

#print(even_num_list)
#print(odd_num_list)


        

        
    
    

    
    
