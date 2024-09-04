def is_valid(board,row,col,num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
        
    start_row, start_col = 3*(row // 3), 3*(col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def solve_sudoku(board):
    empty=find_empty(board)
    if not empty:
        return True

    row, col = empty
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] =num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False


def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None


def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- " * 11)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            print(board[i][j], end=" ")
        print()


def get_user_input():
    board = []
    print("Enter the Sudoku puzzle row by row.")
    print("Use 0 for empty cells.")
    for i in range(9):
        while True:
            try:
                row = list(map(int, input(f"Enter row {i + 1} (9 digits, use 0 for blanks): ")))
                if len(row) == 9 and all(0 <= num <= 9 for num in row):
                    board.append(row)
                    break
                else:
                    print("Invalid input. Please enter exactly 9 digits (0-9).")
            except ValueError:
                print("Invalid input, Please enter exactly 9 digits (0-9).")
    return board


if __name__ == "__main__":
    board=get_user_input()

    print("\nUnsolved Sudoku:")
    print_board(board)

    if solve_sudoku(board):
        print("\nSolved Sudoku:")
        print_board(board)
    else:
        print("No solution exists")
