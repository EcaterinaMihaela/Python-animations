SIZE = 3

# Declaring the global grid
grid = [[' ' for _ in range(SIZE)] for _ in range(SIZE)]

# Initialize grid
def initialize_grid():
    global grid
    grid = [[' ' for _ in range(SIZE)] for _ in range(SIZE)]

# Display grid
def display_grid():
    print("\n")
    for i in range(SIZE):
        for j in range(SIZE):
            print(f" {grid[i][j]} ", end="")
            if j < SIZE - 1:
                print("|", end="")
        print()
        if i < SIZE - 1:
            print("---+" * (SIZE - 1) + "---")
    print("\n")

# Make the move
def make_move(row, col, player):
    if row < 0 or row >= SIZE or col < 0 or col >= SIZE or grid[row][col] != ' ':
        return 0  # Invalid move
    grid[row][col] = player
    return 1  # Valid move

# Check for a winner
def check_win(player):
    # Check rows
    for i in range(SIZE):
        if all(grid[i][j] == player for j in range(SIZE)):
            return 1

    # Check columns
    for j in range(SIZE):
        if all(grid[i][j] == player for i in range(SIZE)):
            return 1

    # Check diagonals
    if all(grid[i][i] == player for i in range(SIZE)):
        return 1

    if all(grid[i][SIZE - 1 - i] == player for i in range(SIZE)):
        return 1

    return 0

# Check for a draw
def check_draw():
    return all(grid[i][j] != ' ' for i in range(SIZE) for j in range(SIZE))

def main():
    row, col = 0, 0
    current_player = 'X'
    game_ended = 0

    initialize_grid()

    while not game_ended:
        display_grid()

        row, col = map(int, input(f"Player {current_player}, enter your move (row and column): ").split())

        if make_move(row, col, current_player):
            if check_win(current_player):
                display_grid()
                print(f"Player {current_player} wins!")
                game_ended = 1
            elif check_draw():
                display_grid()
                print("The game is a draw.")
                game_ended = 1
            else:
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    main()

