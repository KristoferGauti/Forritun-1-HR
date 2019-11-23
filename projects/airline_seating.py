def alphabet():
   """Returns the alphabetical uppercase letters"""
   ascii_upper_letters = []
   for i in range(65,91): #for x in range(97,123) for the lowercase letters
	   ascii_upper_letters.append(chr(i))

   return ascii_upper_letters

def plain_seats_map(alphas):
   """Returns a list with the seat rows and columns alphabetically"""

   rows = int(input("Enter number of rows: "))
   no_of_seats = int(input("Enter number of seats in each row: "))

   no_of_seats_list = []
   for seat in range(no_of_seats):
      no_of_seats_list.append(alphas[seat])
   
   seating_list = []
   for row in range(rows):
      seating_list.append(no_of_seats_list)

   print_right_format(seating_list)

   return seating_list

def choose_seats(seats, old_input = [[1,"z"]]):
   """Returns the users input seat. 
   Returns invalid seat if the user has input his 
   seat out of range. The old_input list contains 
   random stuff in the beginning to prevent an error"""

   try:
      taken = True
      while taken:
         row, seat_number = input("Input seat number (row seat): ").upper().split()
         row = int(row) - 1 

         new_row = []
         
         for letter in seats[row]:
            if seat_number == letter:
               new_row.append("X")
            else:
               new_row.append(letter)

         #Checks if the seat is taken
         if [row,seat_number] in old_input: 
            print("That seat is taken!")

         #if user inputs the letter out of range   
         elif seat_number not in seats[row]:
            print("Seat number is invalid!")
      
         else:
            old_input.append([row,seat_number])
            taken = False

      seats[row] = new_row 
      return seats

   except:
      print("Seat number is invalid!")
      choose_seats(seats)
      return False

def print_right_format(the_plane):
   """Returns the plane seats in a beautiful format"""
   try:
      for index, row in enumerate(the_plane, start = 1):
         print("{:>2}".format(index), end = "   ")

         for index, seat in enumerate(row, start = 1):
            if len(row) / 2 == index:
               print(seat, end = "   ")
            else:
               print(seat, end = " ")
         print()

   except:
      print("Seat number is invalid!")
      
def game_loop(seats,user_seat):
   """This is the game loop function"""

   print_right_format(user_seat)
   more_seats = input("More seats (y/n)? ").lower().strip()
   
   if more_seats == "y":
      while more_seats == "y":
         choose_seats(seats)
         print_right_format(user_seat)

         #changes the two dimentional list into one dimentional list
         one_dimentional_list = [x for sublist in seats for x in sublist]
         if len(set(one_dimentional_list)) == 1: #Check if the plane is full
            break

         else:
            more_seats = input("More seats (y/n)? ").lower().strip()
   else:
      pass

def main():
   alphabetical_letters = alphabet()
   seats = plain_seats_map(alphabetical_letters)
   users_seat = choose_seats(seats)

   game_loop(seats,users_seat)

main()