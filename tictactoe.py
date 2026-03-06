def print_board(board):
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def check_winner(b):
    # All 8 winning combinations (rows, columns, diagonals)
    win_coords = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for (x, y, z) in win_coords:
        if b[x] == b[y] == b[z] != " ":
            return b[x].upper()
    return None

def play_game():
    board = [" "] * 9
    current_player = "X"
    game_still_going = True
    
    while game_still_going:
        print_board(board)
        try:
            move = int(input(f"Player {current_player}, enter position (0-8): "))
            if board[move] != " ":
                print("Spot taken! Try again.")
                continue
            board[move] = current_player
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 0 and 8.")
            continue

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Game Over! Player {winner} wins!")
            game_still_going = False

        #   Checks for draw inside the loop
        elif " " not in board:
            print_board(board)
            print("It's a draw!")
            game_still_going = False
        
        else:
            current_player = "O" if current_player == "X" else "X"
            print(f"Player {current_player}'s turn")
play_game()