m_str = input("Input m: ")
c = 300000000

new_variable = float(m_str)
e = new_variable*(c**2)

print("e =",e)

#**********************************************************************************

in_str = input("Input s: ")
in_int = int(in_str)

print("in_int = ",in_int)

in_float = float(in_str)
print("in_float = ",in_float)

#*******************************************************************************

import math

x1_str = input("Input x1: ")  # do not change this line
y1_str = input("Input y1: ")  # do not change this line
x2_str = input("Input x2: ")  # do not change this line
y2_str = input("Input y2: ")  # do not change this line
# convert strings to ints
#  d =

x = int(x1_str)
y = int(y1_str)
x1 = int(x2_str)
y1 = int(y2_str)

d = math.sqrt((x-x1)**2 + (y-y1)**2)

print("d =",d)  # do not change this line

#*****************************************************************************************

weight_str = input("Weight (kg): ") # do not change this line
height_str = input("Height (cm): ") # do not change this line

weight_int = float(weight_str) 
height_int = float(height_str) / 100

bmi = (weight_int / height_int**2)

print("BMI is: ", bmi) # do not change this line

#******************************************************
x_str = input("Input x: ")
# remember to convert to an int
# first_three =
# last_two =
# middle_two =

x_int = int(x_str)
first_three = x_int//1000
last_two = x_int%100
middle_two = x_int%10000//100

print("original input:", x_str)
print("first_three:", first_three)
print("last_two:", last_two)
print("middle_two:", middle_two)

#*****************************************************************

secs_str = input("Input seconds: ") # do not change this line
# hours =
# minutes =
# seconds =

secs_int = int(secs_str)


hours = secs_int // (60*60)
hours_afgangur = secs_int%3600

minutes = hours_afgangur // 60
minutes_afgangur = hours_afgangur%60

seconds = minutes_afgangur


print(hours,":",minutes,":",seconds) # do not change this line
