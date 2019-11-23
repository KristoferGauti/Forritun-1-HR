class Student(object):
   def __init__(self, first = "", last = "", id = 0): #The init method is our constructor 
      self.first_name_str = first #self is a default instance 
      self.last_name_str = last
      self.id_int = id
      #The __init__ function does not have an explicit return statement, 
      #in fact a return statement is forbidden for this particular method 

   def update(self, first = "", last = "", id = 0):
      if first:
         self.first_name_str = first
      if last:
         self.last_name_str = last
      if id:
         self.id_int = id 

   def __str__(self):
      return "{} {}, ID:{}".format(self.first_name_str, self.last_name_str, self.id_int)

def main():
   joe = Student("Joe", "Bayden", 2) #Prints the whole thing with self.name = "Joe" og svo framvegis 
   print(joe)
   print()
   print(joe.last_name_str) #prints only the method
   print()
   methods = dir(joe)

   for method in methods:
      print(method,end=" ")


main()