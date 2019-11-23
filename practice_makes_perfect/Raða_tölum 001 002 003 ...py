length = 25

for y in range(1,length+1):
     the_range = int("1"+"0"*y)
     count = 0
     for x in range(0,the_range):
          x = str(x)
          while (len(x)!= y):
               x = "0"+x
          if y == 0:
               None
          elif y == 1:
               None
          elif y == 2:
               if x[0]== x[1]:
                    count+=1
          elif y == 3:
               if x[0]== x[1] or x[1]==x[2]:
                    count+=1
          elif y == 4:
               if x[0]== x[1] or x[1]==x[2] or x[2]==x[3]:
                    count+=1
          elif y == 5:
               if x[0]== x[1] or x[1]==x[2] or x[2]==x[3]or x[3]==x[4]:
                    count+=1
          elif y == 6:
               if x[0]== x[1] or x[1]==x[2] or x[2]==x[3]or x[3]==x[4] or x[4]==x[5]:
                    count+=1
     print(count)