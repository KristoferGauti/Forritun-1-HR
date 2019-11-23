# Constants to be used in the implementation
DIM = 5
POSITION = 'o'
EMPTY = 'x'
LEFT = 'l'
RIGHT = 'r'
UP = 'u'
DOWN = 'd'
QUIT = 'q'

def get_move():
    ''' Returns a move corresponding to the user input direction '''
    move = input('Move: ')
    
    if move not in [LEFT, RIGHT, UP, DOWN]:
        return QUIT
    else:
        return move

def initialize_grid():
    ''' Returns an initialized grid for the given dimension '''
    grid = []

    for i in range(DIM):
        sublist = []
        for j in range(DIM):
            sublist.append(EMPTY)
        grid.append(sublist)

    grid[0][0] = POSITION  # Current position
    return grid

def pretty_print(grid):
   for row in grid:
      print(" ".join(row))

def make_move(grid, move, x, y):
   """Check what move was made"""
   grid[x][y] = EMPTY

   if move == LEFT:
      if y == 0:
         y = 4
      else:
         y -= 1

   elif move == RIGHT:
      if y == DIM - 1:
         y = 0
      else:
         y += 1

   elif move == DOWN:
      if x == DIM - 1:
         x = 0
      else:
         x += 1

   elif move == UP:
      if x == 0:
         x = DIM
      else:
         x -= 1

   grid[x][y] = POSITION     
   return grid, x, y

def main():
   x = 0 
   y = 0 
   grid = initialize_grid()
   move = ""

   while move != QUIT:
      pretty_print(grid)
      move = get_move()

      grid, x, y = make_move(grid, move, x, y)
 

main()