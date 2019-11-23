# class Student():
#    def __init__(self, score = 10):
#       self.score = score

#    def add_score(self, score = 10):
#       self.score += score

#    def decrease_score(self):
#       self.score -= 10

#    def __str__(self):
#       return "{}".format(self.score)


# def main():
#    p = Student()
#    p.add_score()
#    p.decrease_score()

#    print(p)



# main()

#Dæmi 2
# class RockGuitar:
#    def __init__(self, guitarist = "", guitar = ""):
#       self.guitarist = guitarist
#       self.guitar = guitar

#    def set_entry(self, guitarist = "", guitar = ""):
#       self.guitarist = guitarist
#       self.guitar = guitar

#    def __str__(self):
#       return "{:<20s}{:<20s}".format(self.guitarist,self.guitar)

# def main():
#    g = RockGuitar()

#    g.set_entry("Keith Richards", "Micawber Fender Telecaster")

#    f = RockGuitar()

#    f.set_entry("Eddie Van Halen","Frankenstrat")

#    h = RockGuitar()

#    h.set_entry("Tony Iommi")

#    print(g)
#    print(f)
#    print(h)

#    def format_solution(first, last):
# 	   return "{:<20s} {:<20s}".format(first, last)
	
#    assert str(g) == format_solution("Keith Richards", "Micawber Fender Telecaster")
#    assert str(f) == format_solution("Eddie Van Halen", "Frankenstrat")
#    assert str(h) == format_solution("Tony Iommi", "")

# main()

#Dæmi 3
# class Sentence:
#    def __init__(self, string):
#       self.string = string.split()

#    def get_first_word(self):
#       return self.string[0]

#    def get_all_words(self):
#       return self.string

#    def replace(self, index, new_word = ""):
#       self.string = [new_word if i == index else word for i, word in enumerate(self.string)]



# def main():
#    sent = Sentence('This is a test')
#    print(sent.get_first_word())
#    print(sent.get_all_words())
#    sent.replace(3, "must")
#    print(sent.get_all_words())

# main()

class Clock:
   def __init__(self, time1 = "00:00:00", time2 = "00:00:00"):
      self.time = time1
      self.other_clock = time2

   def __str__(self):
      hours, minutes, seconds = self.time.split(":")
      return "{} hours, {} minutes and {} seconds".format(hours, minutes, seconds)

   def str_update(self, time):
      self.time = time

   def add_clocks(self, clock):
      hours, minutes, seconds = self.time.split()
      hours2, minutes2, seconds2 = clock.split()
      
      seconds = (int(seconds) + int(seconds2)) % 60
      minutes = (int(minutes) + int(minutes2) + (int(seconds) + int(seconds2)) // 60) % 60
      hours = (int(hours) + int(hours2) + (int(minutes) + int(minutes2)) // 60) % 60

      self.time = "{} {} {}".format(hours,minutes,seconds)


def main():
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


main()

   




      

