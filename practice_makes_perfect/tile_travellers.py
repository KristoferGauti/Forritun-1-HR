import random

# Constants
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'

def move(direction, col, row):
    ''' Returns updated col, row given the direction '''
    if direction == NORTH:
        row += 1
    elif direction == SOUTH:
        row -= 1
    elif direction == EAST:
        col += 1
    elif direction == WEST:
        col -= 1
    return(col, row)    

def is_victory(col, row):
    ''' Return true is player is in the victory cell '''
    return col == 3 and row == 1 # (3,1)

def print_directions(directions_str):
    print("You can travel: ", end='')
    first = True
    for ch in directions_str:
        if not first:
            print(" or ", end='')
        if ch == NORTH:
            print("(N)orth", end='')
        elif ch == EAST:
            print("(E)ast", end='')
        elif ch == SOUTH:
            print("(S)outh", end='')
        elif ch == WEST:
            print("(W)est", end='')
        first = False
    print(".")
        
def find_directions(col, row):
    ''' Returns valid directions as a string given the supplied location '''
    if col == 1 and row == 1:   # (1,1)
        valid_directions = NORTH
    elif col == 1 and row == 2: # (1,2)
        valid_directions = NORTH+EAST+SOUTH
    elif col == 1 and row == 3: # (1,3)
        valid_directions = EAST+SOUTH
    elif col == 2 and row == 1: # (2,1)
        valid_directions = NORTH
    elif col == 2 and row == 2: # (2,2)
        valid_directions = SOUTH+WEST
    elif col == 2 and row == 3: # (2,3)
        valid_directions = EAST+WEST
    elif col == 3 and row == 2: # (3,2)
        valid_directions = NORTH+SOUTH
    elif col == 3 and row == 3: # (3,3)
        valid_directions = SOUTH+WEST
    return valid_directions

def coin(col, row, coinCounter):
    coin = False
    coinCounter[1] = []   #take this line out if game should not be able to pick up same coin 2 times
    if row == 2 and col == 1:
        if 1 not in coinCounter[1]:
            coin = True
            coinCounter[1].append(1)
    elif row == 2 and col == 2:
        if 2 not in coinCounter[1]:
            coin = True
            coinCounter[1].append(2)
    elif row == 2 and col == 3:
        if 3 not in coinCounter[1]:
            coin = True
            coinCounter[1].append(3)
    elif row == 3 and col == 2:
        if 4 not in coinCounter[1]:
            coin = True
            coinCounter[1].append(4)
    if coin:
        print("Pull a lever (y/n): ",end="")
        lever = random.choice(["y", "n"])
        print(lever)
        #lever = input("Pull a lever (y/n): ").lower()
        if lever == "y":
            coinCounter[0] += 1
            print("You received 1 coin, your total is now {}.".format(coinCounter[0]))
        else:
            coinCounter[1].pop()
    
    return coinCounter

def play_one_move(col, row, valid_directions, coinCounter, movesToWin):
    ''' Plays one move of the game
        Return if victory has been obtained and updated col,row '''
    victory = False
    #Computer input:
    print("Direction: ",end="")
    direction = random.choice([NORTH,EAST,SOUTH,WEST])
    print(direction)

    #Player input:
    #direction = input("Direction: ")
    #direction = direction.lower()
    movesToWin += 1
    if not direction in valid_directions:
        print("Not a valid direction!")
    else:
        col, row = move(direction, col, row)
        coinCounter = coin(col, row, coinCounter)
        victory = is_victory(col, row)
    return victory, col, row, coinCounter, movesToWin

def game_loop(choice):
    if choice.lower() == "y":
        return True

# The main program starts here
play = game_loop("y")

while play:
    SEED = int(input("Input seed: "))
    random.seed(SEED)
    victory = False
    row = 1
    col = 1
    coinCounter = [0, []]
    movesToWin = 0

    valid_directions = NORTH
    print_directions(valid_directions)

    while not victory:
        victory, col, row, coinCounter, movesToWin = play_one_move(col, row, valid_directions, coinCounter, movesToWin)
        if victory:
            print("Victory! Total coins {}. Moves {}.".format(coinCounter[0], movesToWin))
        else:
            valid_directions = find_directions(col, row)
            print_directions(valid_directions)
    play = game_loop(input("Play again (y/n): "))