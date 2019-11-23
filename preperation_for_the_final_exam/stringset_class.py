class StringSet:
   def __init__(self, str1):
      self.str1 = str1.split()
      self.set_list = []
      

      for item in self.str1:
         if item not in self.set_list:
            self.set_list.append(item)


   def __str__(self):
      the_print = ""
      for item in self.set_list:
         the_print += item + " "
      return "{}".format(the_print)

   def __add__(self, other):
      union_list = []
      for item in other.set_list:
         if item not in union_list:
            union_list.append(item)

      string = ""
      for elem in union_list:
         string += elem + " "

      new_obj = StringSet(string)
      return new_obj 


   
   def size(self):
      return len(self.set_list)

   def at(self):
      pass




def main():
   str1 = 'chocolate ice cream and chocolate candy ice bars are my favorite'
   set1 = StringSet(str1)
   str2 = 'I like to eat broccoli and fish and ice cream and brussel fish sprouts'
   set2 = StringSet(str2)
   print("Set1:", set1)
   print("Set2:", set2)
   print("Set1 size:", set1.size())
   print("Set2 size:", set2.size())
   the_union = set1 + set2
   print("Union:", the_union)
   print("Union size:", the_union.size())

   query = StringSet('chocolate cream fish good rubbish')
   print("Query:", query)
   #  count = 0
   #  for i in range(query.size()):
   #      if the_union.find(query.at(i)):
   #          count += 1
    
   print("Query size:", query.size())
   #  print("Found in union:", count)

main()