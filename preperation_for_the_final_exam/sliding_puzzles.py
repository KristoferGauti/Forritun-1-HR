"""Example input: 
5 3 13 7 14 10 0 11 1 4 6 8 12 9 2 15""" 
# Constants
DIM = 4 # dimension of the board DIMxDIM
EMPTYSLOT = 0
QUIT = 0

def initialize_board():
    ''' Creates the initial board according to the user input.
    The board is a list of lists.
    The list contains DIM elements (rows), each of which contains DIM elements (columns)'''
    numbers = input().split()
    numbers = [int(number) for number in numbers]
    puzzle_board = []
    index = 0
    for _ in range(DIM):
        row = numbers[index:index + DIM]
        index += DIM
        puzzle_board.append(row)

    return puzzle_board
    

def display(puzzle_board):
    ''' Display the board, printing it one row in each line '''
    print()
    for i in range(DIM):
        for j in range(DIM):
            if puzzle_board[i][j] == EMPTYSLOT:
                print("\t", end="")
            else:
                print(str(puzzle_board[i][j]) + "\t", end="")
        print()
    print()

def find_index(board, number):
   x = 0
   y = 0
   for index1, row in enumerate(board):
      if number in row:
         x += index1
      for index, num in enumerate(row):
         if num == number:
            y += index
   
   return x,y
   
def move(target, x_start_pos, y_start_pos, target_x, target_y, board):
   # print(board)
   # print(x_start_pos,y_start_pos)
   # print(target_x, target_y)
   old_pos = board[target_x][target_y]

   if (target_x, target_y) == (x_start_pos, y_start_pos - 1):
      board[x_start_pos][y_start_pos - 1] = EMPTYSLOT
      board[x_start_pos][y_start_pos] = old_pos

   elif (target_x, target_y) == (x_start_pos, y_start_pos + 1):
      board[x_start_pos][y_start_pos + 1] = EMPTYSLOT
      board[x_start_pos][y_start_pos] = old_pos

   elif (target_x, target_y) == (x_start_pos - 1, y_start_pos):
      board[x_start_pos - 1][y_start_pos] = EMPTYSLOT
      board[x_start_pos][y_start_pos] = old_pos

   elif (target_x, target_y) == (x_start_pos + 1, y_start_pos):
      board[x_start_pos + 1][y_start_pos] = EMPTYSLOT
      board[x_start_pos][y_start_pos] = old_pos
   
      
   display(board)


def game_loop(board):
   target = int(input())
   while target >= 0:
      x_start_pos, y_start_pos = find_index(board, EMPTYSLOT)  
      target_index_x, target_index_y = find_index(board, target)

      move(target, x_start_pos, y_start_pos, target_index_x, target_index_y, board)
   
      
      target = int(input())

      if target == QUIT:
         break
      


def main():
   board = initialize_board()
   display(board)

   game_loop(board)


main()