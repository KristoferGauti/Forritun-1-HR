def name_and_grade_list(name):
   grade_dict = {}
   for _ in range(1,4):
      grade = float(input("Input a grade number 1: "))
      if name in grade_dict:
         grade_dict[name] += [grade]
      else:
         grade_dict[name] = [grade]

   return grade_dict

def sort_students(student_list):
   student_names = []
   for student_dict in student_list:
      for key, value in student_dict.items():
         student_names.append(key)
      
   return sorted(student_names)

def average(a_list):
   average = sum(a_list) / len(a_list)
   return average

def highest_grade(student_list):
   highest_grade_list = []
   name = ""
   for student in student_list:
      for key, value in student.items():
         avr = average(value)
         highest_grade_list.append(avr)
         
   for s in student_list:
      for k, v in s.items():
         if average(v) == max(highest_grade_list):
            name += k

   return max(highest_grade_list), name


def print_nicely(student_list, names_sorted_list, max_grade, name):
   old_key = []

   for name in names_sorted_list:
      for student_dict in student_list:
         for key, value in student_dict.items():
            if key == name:
               if key in old_key:
                  pass
               else:
                  print("{}: {}".format(key, value))

               
               old_key.append(key)  


   print("Student with highest average grade:\n{} has an average grade of {}".format(name, max_grade)) 


def main():
   
   name = input("Student name: ")
   name_1_grades_dict = name_and_grade_list(name)

   name2 = input("Student name: ")
   name_2_grades_dict = name_and_grade_list(name2)

   name3 = input("Student name: ")
   name_3_grades_dict = name_and_grade_list(name3)

   name4 = input("Student name: ")
   name_4_grades_dict = name_and_grade_list(name4)

   student_list = [name_1_grades_dict, name_2_grades_dict, name_3_grades_dict, name_4_grades_dict]

   names_sorted_list = sort_students(student_list)
   
   max_grade, student_name = highest_grade(student_list)

   print_nicely(student_list, names_sorted_list, max_grade, student_name)

main()