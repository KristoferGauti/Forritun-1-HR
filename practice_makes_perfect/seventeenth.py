"""Write a class Student() such that it has an attribute 'score' (that is initialized with 10) and three methods:

add_score(): adds 10 to the score
decrease_score(): decreases score by 10
__str__(): returns the current score (should return a string)"""

class Student():
        def __init__(self,value = 10):
                self.value = value
        def __str__(self, value = 0):
                return str(self.value)
        def add_score(self, value = 0):
                self.value += 10
        def decrease_score(self, value = 0):
                self.value -= 10
p = Student()

print(p)


p.add_score()
print(p)

p.decrease_score()
print(p)

"""
Write a class called RockGuitar() that has attributes: 'guitarist' and 'guitar'. It has a constructor with three
 parameters, self, guitarist and guitar. The default value of guitarist and guitar should be empty string.

 

The class should have __str__ method to return a string for output using this format: "{:<20s} {:<20s}". 
Lastly, it has the following method to set guitarist and guitar:

set_entry(guitarist, guitar): both 'guitarist' and 'guitar' are strings.  'guitar" has the default value as the empty string. 
"""

class RockGuitar():
        def __init__(self, guitarist = "", guitar = ""):
                self.guitarist = guitarist
                self.guitar = guitar
        
        def __str__(self):
                return "{:<20s} {:<20s}".format(self.guitarist,self.guitar)
        
        def set_entry(self, guitarist,guitar = ""):
                self.guitarist = guitarist
                self.guitar = guitar

g1 = RockGuitar()
g1.set_entry("Jimmy Page", "Gibson Les Paul Standard")
g2 = RockGuitar()
g2.set_entry("Angus Young", "Jaydee SG")
g3 = RockGuitar("Mark Knoppfler")
print(g1)
print(g2)
print(g3)

"""Design a class called Sentence that has a constructor that takes a string, representing the sentence, as input.
  The class should have the following methods:

get_first_word(): returns the first word as a string
get_all_words(): returns all words in a list.
replace(index, new_word): Changes a word at a particular index to "new_word".  
For example, if sentence is "I'm going back", then replace(2, "home") results in "I'm going home". 
 If the index is not valid, the method does not do anything. """

class Sentence():
        
        def __init__(self,sentence = ""):
                self.sentence = sentence
                self.sentence_list = self.sentence.split()

        def get_first_word(self):
                return self.sentence_list[0]
        def get_all_words(self):
                return self.sentence_list
        def replace(self,index,new_word):
                if index <= len(self.sentence_list):
                        self.sentence_list[index] = new_word
                        return self.sentence_list
sent = Sentence('This is a test')
print(sent.get_first_word())
print(sent.get_all_words())
sent.replace(3, "must")
print(sent.get_all_words())


"""
Implement a class called Clock with the following attributes:

Constructor with three parameters: hours, minutes, seconds with default values 0.
Three instance variables: hours, minutes, seconds.
A method called str_update(). It takes as an argument a string of the form hh:mm:ss and updates
the three instances variables.
A __str__() method for responding to the print() method. It should write out: "{} hours, {} minutes and {} seconds"
A method called add_clocks(). It takes another clock object as a parameter, adds the two clocks and returns a new 
clock instance.  In this method, you need to add the respective values of the two clocks together and remember the
 resulting hours, minutes and seconds. Remember that the sum of seconds cannot exceed 60, in which case there is
  a carry over to the minutes values. Same for minutes, it cannot exceed 60 and carries over to hours. For hours,
   the summed values cannot exceed
24. If hours is exceeded, we DO NOT ignore it and start from zero.  Use the divmod() built-in Python function in your
 implementation.

 """

class Clock():
        def __init__(self, hours = 0, minutes = 0, seconds = 0):
                self.hours = hours
                self.minutes = minutes
                self. seconds =seconds

        def str_update(self,a_string):
                a_list = a_string.split(":")
                self.hours = int(a_list[0])
                self.minutes = int(a_list[1])
                self.seconds = int(a_list[2])
        def add_clocks(self, other):
                # divmod(xx, 60) = (xx//60, xx%60) = minutes, seconds
                self.hours +=other.hours
                self.minutes += other.minutes
                self.seconds += other.seconds

                seconds_tuple = divmod(self.seconds,60)
                self.seconds = seconds_tuple[1]
                self.minutes += seconds_tuple[0]
                minutes_tuple = divmod(self.minutes,60)
                self.minutes = minutes_tuple[1]
                self.hours += minutes_tuple[0]
                self.hours = self.hours %24
                return "{} hours, {} minutes and {} seconds".format(self.hours,self.minutes,self.seconds)
        def __str__(self):
                return "{} hours, {} minutes and {} seconds".format(self.hours,self.minutes,self.seconds)


clock1 = Clock()
clock2 = Clock()
print(clock1)
print(clock2)
clock1.str_update("03:21:34")
clock2.str_update("05:45:52")
print(clock1)
print(clock2)
clock3 = clock1.add_clocks(clock2)
print(clock3)

#print(divmod(70,60))
