# class WholeNumber:
#    def __init__(self, num = 0):
#       try:
#          int(num)
#          if num < 0:
#             self.__num = None 
#          else:
#             self.__num = num
#       except ValueError:
#          self.__num = None

         

#    def __str__(self):
#       return "{}".format(self.__num)

#    def __add__(self, other):
#       if self.__num == None or other.__num == None:
#          return None 
#       else:
#          return WholeNumber(self.__num + other.__num)

#    def __mul__(self, other):
#       if self.__num == None or other.__num == None:
#          return None 
#       else:
#          return WholeNumber(self.__num * other.__num)

#    def __sub__(self, other):
#       if self.__num == None or other.__num == None:
#          return None 
#       else:
#          return WholeNumber(self.__num - other.__num)

# num1 = WholeNumber(1)
# print(num1)

# num1 = WholeNumber(3)
# num2 = WholeNumber(4)
# num3 = num1 + num2
# print(num3)

# num2 = WholeNumber(2)
# num3 = num1 * num2
# print(num3)

# num3 = num1 - num3
# print(num3)

# #Dæmi 2
# class Student:
#    def __init__(self, identity, grades):
#       self.__identity = identity
#       self.__grades = grades

#    def __str__(self):
#       return "Student ID: {}\nGrades: {}".format(self.__identity, self.__grades)

#    def __gt__(self, other):
#       return self.average() > other.average()

#    def average(self):
#       average = (sum(self.__grades)) / len(self.__grades)
#       return average

# student1 = Student(1, [3.0, 4.6, 3.4, 5.4])
# student2 = Student(2, [9.5, 9.0, 8.9, 9.8])

# print(student1)

# if student1 < student2:
#     print("student1 < student2")


#Dæmi 3
class Account:
   def __init__(self, money):
      self.money = money

   def __str__(self):
      return "Balance: {:.2f}".format(self.money)      

class SavingsAccount(Account):
   def __init__(self, money):
      Account.__init__(self, money)

   def update_balance(self):
      self.money = self.money * 1.05 + self.money * 0.1
   

class DebitAccount(Account):
   def __init__(self, money):
      Account.__init__(self, money)

   def update_balance(self):
      self.money = self.money * 1.02

s1 = SavingsAccount(300)
s1.update_balance()
print( str(s1)) == "Balance: 345.00"
d1 = DebitAccount(400)
d1.update_balance()
print( str(d1)) == "Balance: 408.00"

# class Employee:
#    def __init__(self, name, salary):
#       self.name = name
#       self.salary = salary

#    def get_name(self):
#       return self.name

# class HourlyEmployee(Employee):
#    def __init__(self, name, salary):
#       Employee.__init__(self,name,salary)

#    def weekly_pay(self, hours):
#       if hours > 40:
#          pay = self.salary * 40 
#          hours -= 40

#          pay += 1.5 * self.salary * hours
#          return pay


# class SalariedEmployee(Employee):
#    def __init__(self, name, salary):
#       Employee.__init__(self, name, salary)

#    def weekly_pay(self, hours):
#       pay = self.salary / 52
#       return pay


# class Manager(SalariedEmployee):
#    def __init__(self, name, salary, weekly_bonus):
#       Employee.__init__(self, name, salary)
#       self.bonus = weekly_bonus

#    def weekly_pay(self, hours):
#       pay = SalariedEmployee.weekly_pay(self, hours)
#       pay += self.bonus
#       return pay




# def print_salaries(staff):
#     for employee in staff:
#         name = employee.get_name()
#         hours = int(input("Hours worked by " + name + ": "))
#         pay = employee.weekly_pay(hours)
#         print("{}: {:.2f}".format(name, pay))

# # The main program starts here
# staff = []
# staff.append(HourlyEmployee("Harry Morgan", 30.0))  # 30.0 is the hourly wage
# staff.append(SalariedEmployee("Sally Lin", 52000.0)) # 52000 is the annual salary
# staff.append(Manager("Mary Smith", 104000.0, 50.0))  # 104000 is the annual salary, 50.0 is the weekly bonus
# print_salaries(staff)
