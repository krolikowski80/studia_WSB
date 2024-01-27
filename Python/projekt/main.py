import os


# Funkcja do wyczyszczenia konsoli
def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


# Funkcja do wyświetlenia planszy
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


# Funkcja do sprawdzenia wygranej
def check_win(board, mark):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    return [mark, mark, mark] in win_conditions


# Funkcja do sprawdzenia remisu
def check_draw(board):
    return all(all(cell != " " for cell in row) for row in board)


# Funkcja do wykonania ruchu
def make_move(board, row, col, mark):
    if board[row][col] == " ":
        board[row][col] = mark
        return True
    return False


# Funkcja do zapisania historii do pliku
def save_history(player1, player2, score, filename="tic_tac_toe_history.txt"):
    with open(filename, "a") as file:
        file.write(f"{player1} vs {player2} - Score: {score}\n")


# Funkcja do wczytania historii z pliku
def load_history(player1, player2, filename="tic_tac_toe_history.txt"):
    try:
        with open(filename, "r") as file:
            history = file.readlines()
            score = {"Player1": 0, "Player2": 0}
            for line in history:
                if player1 in line and player2 in line:
                    if "Player1" in line:
                        score["Player1"] += 1
                    elif "Player2" in line:
                        score["Player2"] += 1
            return score
    except FileNotFoundError:
        return {"Player1": 0, "Player2": 0}


# Główna funkcja gry
def tic_tac_toe():
    player1 = input("Enter the name of player 1 (X): ")
    player2 = input("Enter the name of player 2 (O): ")
    current_player = player1
    mark = "X"
    score = load_history(player1, player2)
    print(f"Current score: {player1} {score['Player1']} - {player2} {score['Player2']}")

    while True:
        board = [[" " for _ in range(3)] for _ in range(3)]
        game_over = False

        while not game_over:
            clear_console()
            print(f"{player1} (X) - {player2} (O)")
            print_board(board)
            print(f"Current turn: {current_player} ({mark})")

            try:
                row = int(input("Enter row (1-3): ")) - 1
                col = int(input("Enter column (1-3): ")) - 1
                if row not in range(3) or col not in range(3):
                    print("Invalid move. Try again.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if make_move(board, row, col, mark):
                if check_win(board, mark):
                    clear_console()
                    print_board(board)
                    print(f"{current_player} wins!")
                    if current_player == player1:
                        score["Player1"] += 1
                    else:
                        score["Player2"] += 1
                    game_over = True
                elif check_draw(board):
                    clear_console()
                    print_board(board)
                    print("It's a draw!")
                    game_over = True
                else:
                    current_player = player1 if current_player == player2 else player2
                    mark = "X" if mark == "O" else "O"
            else:
                print("This spot is already taken. Try another one.")

        print(f"Score: {player1} {score['Player1']} - {player2} {score['Player2']}")
        save_history(player1, player2, score)
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break


if __name__ == "__main__":
    tic_tac_toe()
