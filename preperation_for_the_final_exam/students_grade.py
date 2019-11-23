def create_a_student():
   name = input("Student name: ")

   grade = []
   for i in range(1,4):
      grade += [float(input("Input grade number {}: ".format(i)))]

   return name, grade

def sort_names(student_list):
   student_sorted_list = sorted(student_list, key=lambda x: x[0], reverse=False)
   return student_sorted_list

def average(a_list):
   return sum(a_list) / len(a_list)

def highest_grade(student_list):
   avr_list = []
   name = ""
   for student in student_list:
      avr_list.append(average(student[1]))

   maximum = max(avr_list)

   for s in student_list:
      if average(s[1]) == maximum:
         name = s[0]
         break

   return name, maximum


def print_nicely(sort_name_list, name, max_grade):
   print("Student list:")
   for student in sort_name_list:
      print("{}: {}".format(student[0],student[1]))

   print("Student with highest average grade:")
   print("{} has an average grade of {:.2f}".format(name, max_grade))


def main():
   student_list = []
   for _ in range(4):
      student_list.append(create_a_student())

   
   sort_student_list = sort_names(student_list)
   name, max_grade = highest_grade(student_list)

   print_nicely(sort_student_list, name, max_grade)


main()