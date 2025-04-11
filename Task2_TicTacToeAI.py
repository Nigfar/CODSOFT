# Created by Nigar Fathima - CodSoft Internship Task 2

# Initialize the game board (3x3) with empty spaces
game_board = [" " for _ in range(9)]

# Function to print the current state of the board
def display_board():
    for row in [game_board[i*3:(i+1)*3] for i in range(3)]:
        print("| " + " | ".join(row) + " |")

# Function to check if a player has won
def is_winner(board, player):
    winning_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for positions in winning_positions:
        if all(board[i] == player for i in positions):
            return True
    return False

# Function to check if the game is a draw
def is_draw(board):
    return " " not in board

# Function to get the list of available moves
def get_available_spots(board):
    return [i for i, cell in enumerate(board) if cell == " "]

# The AI uses minimax algorithm to pick the best move
def minimax(board, is_ai_turn):
    if is_winner(board, "O"):
        return 1
    elif is_winner(board, "X"):
        return -1
    elif is_draw(board):
        return 0

    if is_ai_turn:
        best_score = float('-inf')
        for move in get_available_spots(board):
            board[move] = "O"
            score = minimax(board, False)
            board[move] = " "
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for move in get_available_spots(board):
            board[move] = "X"
            score = minimax(board, True)
            board[move] = " "
            best_score = min(best_score, score)
        return best_score

# Function for the AI's turn
def ai_turn():
    best_move = None
    best_score = float('-inf')
    for move in get_available_spots(game_board):
        game_board[move] = "O"
        score = minimax(game_board, False)
        game_board[move] = " "
        if score > best_score:
            best_score = score
            best_move = move
    game_board[best_move] = "O"

# Main function to run the game
def start_game():
    print("Welcome to Tic-Tac-Toe!")
    display_board()

    while True:
        try:
            player_move = int(input("Enter your move (0-8): "))
            if game_board[player_move] != " ":
                print("Cell already taken. Try again.")
                continue
            game_board[player_move] = "X"
        except (ValueError, IndexError):
            print("Invalid input! Please choose a number from 0 to 8.")
            continue

        display_board()

        if is_winner(game_board, "X"):
            print("Congratulations, you win!")
            break
        if is_draw(game_board):
            print("It's a draw!")
            break

        print("AI's Turn...")
        ai_turn()
        display_board()

        if is_winner(game_board, "O"):
            print("AI wins. Better luck next time!")
            break
        if is_draw(game_board):
            print("It's a draw!")
            break

# Run the game
start_game()
