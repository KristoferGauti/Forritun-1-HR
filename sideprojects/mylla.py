EMPTY = ' '
P1 = "X"
P2 = "O"
QUIT = "q"
TIE = "tie"
GRID_SIZE = 3

def generate_board():
    row = [EMPTY for x in range(GRID_SIZE)]
    board = [row[:] for x in range(GRID_SIZE)]
    return board

def print_board(board):
    for row in board:
        print(" " + " | ".join(row))
        if row is not board[-1]:
            print("--- " * 3)

def check_pos(rowTarget, collumnTarget, board, player):
    same = board[:]
    board[rowTarget - 1] = [player if collumnTarget == index and x == EMPTY else x for index, x in enumerate(board[rowTarget - 1], start = 1)]
    if not same == board:
        return board

def get_input(board, player):
    if player == "X":
        print("It's player's 1 turn")
    else:
        print("It's player's 2 turn")

    while True:
        try:
            the_input = input("Enter position (row, collumn): ")
            if the_input == QUIT.lower():
                return the_input
            row, collumn = the_input.split()
            row, collumn = int(row), int(collumn)
            if 0 > row or row > GRID_SIZE:
                continue
            if 0 > collumn or collumn > GRID_SIZE:
                continue
            if check_pos(row, collumn, board, player) == None:
                continue
            return board
        except ValueError:
            continue

def all_same_in_list(aList):
    checker = aList[0]
    if all([checker == x and not checker == EMPTY for x in aList]):
        return "Player 1" if checker == P1 else "Player 2" if checker == P2 else None

def win(board):
    # Winning possibilities:
    winning_moves = []

    full = True
    cross1 = []
    cross2 = []
    
    for index, row in enumerate(board):
        winning_moves.append(row)
        
        collumns = []
        for row in board:
            for collumn in row[index]:
                collumns.append(collumn)
        winning_moves.append(collumns)
        
        for index2, collumn in enumerate(row):

            if index == index2:
                cross1.append(board[index][index2])
            
            if index + index2 == GRID_SIZE - 1:
                cross2.append(board[index][index2])
            
            if collumn == EMPTY:
                full = False

    winning_moves.append(cross1)
    winning_moves.append(cross2)
    if full:
        return TIE
    
    for win in winning_moves:
        if all_same_in_list(win):
            return all_same_in_list(win)
    

def main():
    board = generate_board()
    print_board(board)
    counter = 0
    while not win(board):
        player = P1 if counter % 2 == 0 else P2
        board = get_input(board, player)
        if board == QUIT:
            break
        print_board(board)
        counter += 1
    
    winner = win(board)
    if winner:
        if winner == TIE:
            print("It's a tie")
        else:
            print(winner, "is the winner!")
main()