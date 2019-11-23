class NewClass(object):
   def __init__(self, param_int = 1):
      self.the_int = param_int
      if param_int % 2 == 0:
         self.hvap = "even"
      else:
         self.hvap = "odd"
      
   def process(self, instance):
      sum_int = self.the_int + instance.the_int

      if sum_int < 0:
         return "negative"
      elif sum_int % 2 == 0:
         return "even"
      else:
         return "odd"

   def __str__(self):
      return "Value {} is {}".format(self.the_int, self.hvap)

def main():
   inst1 = NewClass(4)
   inst2 = NewClass(-5)
   inst3 = NewClass()

   print(inst1)
   print(inst1.hvap)
   print(inst1.process(inst2))
   print(inst3.process(inst1))

main()
      
