#Dæmi 1
a_str = input("Input a string: ")

print(a_str[0],a_str[-1])


#Dæmi 2
a_str = input("Input a string: ")

a_str2 = a_str[3:]
a_str3 = a_str[:3]

print(a_str2 + a_str3) 


#Dæmi 3
 a_str = input("Input a string: ")

target = "o"

for i, ch in enumerate(a_str):
    if ch == target:
        print(i) 


#Dæmi 4
a_str = input("Input a float: ")

a_float = float(a_str)

print("{:12.2f}".format(a_float))

print(a_float)

#Dæmi 5
a_str = input("Input a string: ")

empty = ""

for i in a_str:
    if i.isdigit():
        empty += i

print(empty)
    

#print(a_str.isdigit())

#Dæmi 6 
name = input("Input a name: ")

first, last = name.split()

print(last.capitalize()[0]+"."+" "+first.capitalize()[:-1])


#Dæmi 7 digit to binary
my_int = int(input('Give me an int >= 0: '))

original_int = my_int

if my_int == 0:
    print("The binary of", original_int, "is", "0")

bin_str = ""
while my_int:
    if my_int & 1 == 1:
        bin_str = "1" + bin_str
    else:
        bin_str = "0" + bin_str
    my_int //= 2

    if my_int == 0:
        print("The binary of", original_int, "is", bin_str)
        break



