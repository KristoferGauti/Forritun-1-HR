class IntList:
   def __init__(self, length):
      self.length = length
      self.int_list = []

   def __str__(self):
      return "{}".format(self.int_list)

   def __len__(self):
      return len(self.int_list)

   def __add__(self, other):
      min_number = min(len(self.int_list), len(other.int_list))
      new_list = []

      for i in range(min_number):
         new_list.append(self.int_list[i] + other.int_list[i])

      return new_list

   def add(self, num):
      if len(self.int_list) >= self.length:
         pass
      else:
         self.int_list.append(num)

   def full(self):
      if len(self.int_list) == self.length:
         return True
      else:
         return False


# Main program starts here
list1 = IntList(5) 	# Constructs an IntList that can hold 5 integers
list2 = IntList(12) 	# Constructs an IntList that can hold 12 integers

for i in range(10):
    list1.add(i)
    list2.add(i)

print(list1)
print(list2)

print("Length of list1 is: {}".format(len(list1)))
print("Length of list2 is: {}".format(len(list2)))

if list1.full():
    print("list1 is full")
if list2.full():
    print("list2 is full")

list3 = list1 + list2
print(list3)

list4 = list2 + list1
print(list4)