
# def list_to_tuple(a_list):
#    for index in range(0,len(a_list)):
#       try:
#          a_list[index] = int(a_list[index])
#       except ValueError:
#          print("Error. Please enter only integers")
#          return tuple()

#    return tuple(a_list)
   


# # Main program starts here - DO NOT change it
# a_list = input("Enter elements of list separated by commas: ").strip().split(',')
# a_tuple = list_to_tuple(a_list)
# print(a_tuple)

# #Dæmi 2
# def get_list():
#    a_list = input("Enter elements of list separated by commas: ").strip().split(',')
#    int_list = []

#    for number in a_list:
#       int_num = int(number)
#       int_list.append(int_num)
      

#    b_list = [num for num in int_list if num % 2 == 0]


#    return b_list

# def even_sum(a_list):
#    even_sum = sum(a_list)
#    return even_sum

# # Main program starts here - DO NOT change it
# a_list = get_list()
# print(even_sum(a_list))

#Dæmi 3 

# def get_emails():
#    email_list = []
#    email = str(input("Email address: "))
#    while email != "q":
#       email_list.append(email)
#       email = str(input("Email address: "))

#    return email_list

# def get_names_and_domains(list_of_emails):
#    tup = [tuple(email.split("@")) for email in list_of_emails]
#    return tup


# # Main program starts here - DO NOT change it
# email_list = get_emails()
# print(email_list)
# names_and_domains = get_names_and_domains(email_list)
# print(names_and_domains)
