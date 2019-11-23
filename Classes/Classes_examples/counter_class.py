class Counter:
   num_instances = 0 #num_instances is a class variable

   def __init__(self, value = 0):
      Counter.num_instances += 1 
      self.value = value #self.value is an instance variable (tilvikarbreyta)

   def __str__(self):
      return "Counter value: {}".format(self.value)

   def increment(self, value = 1):
      self.value += value

   def decrement(self, value = 1):
      self.value -= 1

#Interface for class is the set of methods that it defines
      

def main():
   counter1 = Counter() #Calling the constructor (smiður)
   print(Counter.num_instances)
   counter1.increment() #Counter1 is self in the call to increment
   counter1.increment(2) 
   counter1.decrement()

   print(counter1)

   counter2 = Counter()
   print(Counter.num_instances)
   for i in range(1,5):
      counter2.increment()
   print(counter2)


main()
