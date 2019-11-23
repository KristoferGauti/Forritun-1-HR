"""Coder: Kristofer Gaut"""
"""Tic Tac Toe"""
#Constants
DIM = 3
PLAYER1 = "x"
PLAYER2 = "o"
QUIT = "q"

def make_board():
   """Creates the board"""
   board = []
   for _ in range(DIM):
      sublist = []
      for _ in range(DIM):
         sublist.append(" ")
         
      board.append(sublist)

   return board

def instruction_board(board):
   print("\nTic Tac Toe\n")
   for i in range(1,4):
      print("   ",i,end="")
   print()
   for row_num, place in enumerate(board, start=1):
      print("",row_num,"  " + " | ".join(place))
      if place is not board[-1]:
         print("    " + "--- " * 3)
   print() 
     
     
def print_board(board):
   """prints the board nicely"""
   for place in board:
      print(" " + " | ".join(place))
      if place is not board[-1]:
         print("--- " * 3)
   print()

def player1_coordinates(board):
   """Returns player 1 coordinates"""

   print("Player 1's turn:")
   p1_move = input("Enter row and column seperated with space: ").lower()
   if p1_move == QUIT:
      return None, None

   else:
      alphabet = True
      while alphabet:
         x, y = p1_move.split()
         if x.isdigit() and y.isdigit():
            alphabet = False

         else:
            print("That is not integers!")
            p1_move = input("Enter row and column seperated with space: ")
         
         return int(x) - 1, int(y) - 1


def player2_coordinates(board):
   """Returns player 2 coordinates"""

   print("Player 2´s turn:")
   p2_move = input("Enter row and column seperated with space: ").lower()
   
   if p2_move == QUIT:
      return None, None
   else:
      alphabet = True
      while alphabet:
         x, y = p2_move.split()
         if x.isdigit() and y.isdigit():
            alphabet = False

         else:
            print("These characters are not integers!")
            p2_move = input("Enter row and column seperated with space: ")
         
      return int(x) - 1, int(y) - 1 
   
def check_fullboard(board):
   """Returns true of the board is full"""
   one_dimentional_list = [x for sublist in board for x in sublist]
   if len(set(one_dimentional_list)) == 2 and " " not in set(one_dimentional_list): #{'o','x'} otherwise the len is 3 due to space
      return True
   else:
      return False

def check_win(board):
   """Checks if player 1 or 2 has won 
   vertically, horizontally or crossly"""

   is_winner = False

   vertical_list_first_column = []
   vertical_list_second_column = []
   vertical_list_third_column = []
   column_list = [vertical_list_first_column, vertical_list_second_column, vertical_list_third_column]

   cross_from_left = [board[0][0], board[1][1], board[2][2]]
   cross_from_right = [board[0][2], board[1][1], board[2][0]]
   
   #Check win horizontally 
   for row in board:
      vertical_list_first_column.append(row[0])
      vertical_list_second_column.append(row[1])
      vertical_list_third_column.append(row[2])
      
      if len(set(row)) == 1 and list(set(row))[0] == PLAYER1:
         is_winner = True
         return is_winner, PLAYER1

      elif len(set(row)) == 1 and set(row) == PLAYER2:
         is_winner = True
         return is_winner, PLAYER2

   #Check win vertical
   for col in column_list:
      if len(set(col)) == 1 and list(set(col))[0] == PLAYER1:
         is_winner = True
         return is_winner, PLAYER1

      elif len(set(col)) == 1 and set(col) == PLAYER2:
         is_winner = True
         return is_winner, PLAYER2

   #Check win from left cross
   if len(set(cross_from_left)) == 1 and list(set(cross_from_left))[0] == PLAYER1:
      is_winner = True 
      return is_winner, PLAYER1
   elif len(set(cross_from_left)) == 1 and list(set(cross_from_left))[0] == PLAYER2:
      is_winner = True
      return is_winner, PLAYER2

   #Check win from right cross
   if len(set(cross_from_right)) == 1 and list(set(cross_from_right))[0] == PLAYER1:
      is_winner = True
      return is_winner, PLAYER1
   elif len(set(cross_from_right)) == 1 and list(set(cross_from_right))[0] == PLAYER2:
      is_winner = True
      return is_winner, PLAYER2

   return is_winner, None

   
def main():
   board = make_board()
   instruction_board(board)
   #print_board(board)
   game_is_playing = True
   old_coordinates = []
   
   while game_is_playing:
      player1_turn = True
      player2_turn = False
      
      while player1_turn:
         x1, y1 = player1_coordinates(board)

         if (x1, y1) in old_coordinates:
            print("This spot is already taken!")
            player1_turn = True
         elif (x1, y1) == (None, None):
            player1_turn = False
            game_is_playing = False
         elif x1 < 0 or y1 < 0:
            print("The spot that you have chosen is out of range!")
            player1_turn = True

         else:
            try:
               board[x1][y1] = PLAYER1
               print_board(board)
               old_coordinates.append((x1, y1))
               player1_turn = False
               player2_turn = True

               fullboard = check_fullboard(board)
               if fullboard:
                  print("Tie game!")
                  player1_turn = False
                  player2_turn = False
                  game_is_playing = False

               """Who won?"""
               winner, player = check_win(board)
               if winner == True and player == PLAYER1:
                  print("Player 1 has won!")
                  player1_turn = False
                  player2_turn = False
                  game_is_playing = False

               elif winner == True and player == PLAYER2:
                  print("Player 2 has won!")
                  player1_turn = False
                  player2_turn = False
                  game_is_playing = False

               elif winner == False and player == None:
                  continue
                  

            except IndexError:
               print("The spot that you have chosen is out of range!")
               player1_turn = True

      while player2_turn:
         x2, y2 = player2_coordinates(board)
         if (x2, y2) in old_coordinates:
            print("This spot is already taken!")
         elif (x2, y2) == (None, None):
            player2_turn = False
            game_is_playing = False
         elif x2 < 0 or y2 < 0:
            print("The spot that you have chosen is out of range!")
            player2_turn = True

         else:
            try:
               board[x2][y2] = PLAYER2
               print_board(board)
               old_coordinates.append((x2, y2))
               player2_turn = False
               player1_turn = True 
               
               fullboard = check_fullboard(board)
               if fullboard:
                  print("Tie game!")
                  player1_turn = False
                  player2_turn = False 
                  game_is_playing = False 
               
               """Who won?"""
               winner, player = check_win(board)
               if winner == True and player == PLAYER1:
                  print("Player 1 has won!")
                  print("Player 2 lost!")
                  player1_turn = False
                  player2_turn = False
                  game_is_playing = False

               elif winner == True and player == PLAYER2:
                  print("Player 2 has won!")
                  print("Player 1 lost!")
                  player1_turn = False
                  player2_turn = False
                  game_is_playing = False

               elif winner == False and player == None:
                  continue
               
            except IndexError:
               print("The spot that you have chosen is out of range!")
               player2_turn = True
   
main()