N = 8

def print_solution(board):
    for row in board:
        print(" ".join("Q" if col else "_" for col in row))
    print("\n")

def is_safe(board, row, col):
    # Check column
    for i in range(row):
        if board[i][col]:
            return False
    
    # Check upper diagonal (left)
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    
    # Check upper diagonal (right)
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j]:
            return False
    
    return True

def solve_n_queens(board, row=0):
    if row == N:
        print_solution(board)
        return True
    
    found = False
    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            found = solve_n_queens(board, row + 1) or found
            board[row][col] = 0  # Backtrack
    
    return found

def solve():
    board = [[0] * N for _ in range(N)]
    if not solve_n_queens(board):
        print("No solution exists")

if __name__ == "__main__":
    solve()
"""
OUTPUT
----------------------------
Q _ _ _ _ _ _ _
_ _ _ _ Q _ _ _
_ _ _ _ _ _ _ Q
_ _ _ _ _ Q _ _
_ _ Q _ _ _ _ _
_ _ _ _ _ _ Q _
_ Q _ _ _ _ _ _
_ _ _ Q _ _ _ _


Q _ _ _ _ _ _ _
_ _ _ _ _ Q _ _
_ _ _ _ _ _ _ Q
_ _ Q _ _ _ _ _
_ _ _ _ _ _ Q _
_ _ _ Q _ _ _ _
_ Q _ _ _ _ _ _
_ _ _ _ Q _ _ _


Q _ _ _ _ _ _ _
_ _ _ _ _ _ Q _
_ _ _ Q _ _ _ _
_ _ _ _ _ Q _ _
_ _ _ _ _ _ _ Q
_ Q _ _ _ _ _ _
_ _ _ _ Q _ _ _
_ _ Q _ _ _ _ _


Q _ _ _ _ _ _ _
_ _ _ _ _ _ Q _
_ _ _ _ Q _ _ _
_ _ _ _ _ _ _ Q
_ Q _ _ _ _ _ _
_ _ _ Q _ _ _ _
_ _ _ _ _ Q _ _
_ _ Q _ _ _ _ _


_ Q _ _ _ _ _ _
_ _ _ Q _ _ _ _
_ _ _ _ _ Q _ _
_ _ _ _ _ _ _ Q
_ _ Q _ _ _ _ _
Q _ _ _ _ _ _ _
_ _ _ _ _ _ Q _
_ _ _ _ Q _ _ _


_ Q _ _ _ _ _ _
_ _ _ _ Q _ _ _
_ _ _ _ _ _ Q _
Q _ _ _ _ _ _ _
_ _ Q _ _ _ _ _
_ _ _ _ _ _ _ Q
_ _ _ _ _ Q _ _
_ _ _ Q _ _ _ _


_ Q _ _ _ _ _ _
_ _ _ _ Q _ _ _
_ _ _ _ _ _ Q _
_ _ _ Q _ _ _ _
Q _ _ _ _ _ _ _
_ _ _ _ _ _ _ Q
_ _ _ _ _ Q _ _
_ _ Q _ _ _ _ _


_ Q _ _ _ _ _ _
_ _ _ _ _ Q _ _
Q _ _ _ _ _ _ _
_ _ _ _ _ _ Q _
_ _ _ Q _ _ _ _
_ _ _ _ _ _ _ Q
_ _ Q _ _ _ _ _
_ _ _ _ Q _ _ _


_ Q _ _ _ _ _ _
_ _ _ _ _ Q _ _
_ _ _ _ _ _ _ Q
_ _ Q _ _ _ _ _
Q _ _ _ _ _ _ _
_ _ _ Q _ _ _ _
_ _ _ _ _ _ Q _
_ _ _ _ Q _ _ _


_ Q _ _ _ _ _ _
_ _ _ _ _ _ Q _
_ _ Q _ _ _ _ _
_ _ _ _ _ Q _ _
_ _ _ _ _ _ _ Q
_ _ _ _ Q _ _ _
Q _ _ _ _ _ _ _
_ _ _ Q _ _ _ _


_ Q _ _ _ _ _ _
_ _ _ _ _ _ Q _
_ _ _ _ Q _ _ _
_ _ _ _ _ _ _ Q
Q _ _ _ _ _ _ _
_ _ _ Q _ _ _ _
_ _ _ _ _ Q _ _
_ _ Q _ _ _ _ _


_ Q _ _ _ _ _ _
_ _ _ _ _ _ _ Q
_ _ _ _ _ Q _ _
Q _ _ _ _ _ _ _
_ _ Q _ _ _ _ _
_ _ _ _ Q _ _ _
_ _ _ _ _ _ Q _
_ _ _ Q _ _ _ _


_ _ Q _ _ _ _ _
Q _ _ _ _ _ _ _
_ _ _ _ _ _ Q _
_ _ _ _ Q _ _ _
_ _ _ _ _ _ _ Q
_ Q _ _ _ _ _ _
_ _ _ Q _ _ _ _
_ _ _ _ _ Q _ _


_ _ Q _ _ _ _ _
_ _ _ _ Q _ _ _
_ Q _ _ _ _ _ _
_ _ _ _ _ _ _ Q
Q _ _ _ _ _ _ _
_ _ _ _ _ _ Q _
_ _ _ Q _ _ _ _
_ _ _ _ _ Q _ _


_ _ Q _ _ _ _ _
_ _ _ _ Q _ _ _
_ Q _ _ _ _ _ _
_ _ _ _ _ _ _ Q
_ _ _ _ _ Q _ _
_ _ _ Q _ _ _ _
_ _ _ _ _ _ Q _
Q _ _ _ _ _ _ _


_ _ Q _ _ _ _ _
_ _ _ _ Q _ _ _
_ _ _ _ _ _ Q _
Q _ _ _ _ _ _ _
_ _ _ Q _ _ _ _
_ Q _ _ _ _ _ _
_ _ _ _ _ _ _ Q
_ _ _ _ _ Q _ _


_ _ Q _ _ _ _ _
_ _ _ _ Q _ _ _
_ _ _ _ _ _ _ Q
_ _ _ Q _ _ _ _
Q _ _ _ _ _ _ _
_ _ _ _ _ _ Q _
_ Q _ _ _ _ _ _
_ _ _ _ _ Q _ _


_ _ Q _ _ _ _ _
_ _ _ _ _ Q _ _
_ Q _ _ _ _ _ _
_ _ _ _ Q _ _ _
_ _ _ _ _ _ _ Q
Q _ _ _ _ _ _ _
_ _ _ _ _ _ Q _
_ _ _ Q _ _ _ _


_ _ Q _ _ _ _ _
_ _ _ _ _ Q _ _
_ Q _ _ _ _ _ _
_ _ _ _ _ _ Q _
Q _ _ _ _ _ _ _
_ _ _ Q _ _ _ _
_ _ _ _ _ _ _ Q
_ _ _ _ Q _ _ _


_ _ Q _ _ _ _ _
_ _ _ _ _ Q _ _
_ Q _ _ _ _ _ _
_ _ _ _ _ _ Q _
_ _ _ _ Q _ _ _
Q _ _ _ _ _ _ _
_ _ _ _ _ _ _ Q
_ _ _ Q _ _ _ _


_ _ Q _ _ _ _ _
_ _ _ _ _ Q _ _
_ _ _ Q _ _ _ _
Q _ _ _ _ _ _ _
_ _ _ _ _ _ _ Q
_ _ _ _ Q _ _ _
_ _ _ _ _ _ Q _
_ Q _ _ _ _ _ _


_ _ Q _ _ _ _ _
_ _ _ _ _ Q _ _
_ _ _ Q _ _ _ _
_ Q _ _ _ _ _ _
_ _ _ _ _ _ _ Q
_ _ _ _ Q _ _ _
_ _ _ _ _ _ Q _
Q _ _ _ _ _ _ _


_ _ Q _ _ _ _ _
_ _ _ _ _ Q _ _
_ _ _ _ _ _ _ Q
Q _ _ _ _ _ _ _
_ _ _ Q _ _ _ _
_ _ _ _ _ _ Q _
_ _ _ _ Q _ _ _
_ Q _ _ _ _ _ _


_ _ Q _ _ _ _ _
_ _ _ _ _ Q _ _
_ _ _ _ _ _ _ Q
Q _ _ _ _ _ _ _
_ _ _ _ Q _ _ _
_ _ _ _ _ _ Q _
_ Q _ _ _ _ _ _
_ _ _ Q _ _ _ _


_ _ Q _ _ _ _ _
_ _ _ _ _ Q _ _
_ _ _ _ _ _ _ Q
_ Q _ _ _ _ _ _
_ _ _ Q _ _ _ _
Q _ _ _ _ _ _ _
_ _ _ _ _ _ Q _
_ _ _ _ Q _ _ _


_ _ Q _ _ _ _ _
_ _ _ _ _ _ Q _
_ Q _ _ _ _ _ _
_ _ _ _ _ _ _ Q
_ _ _ _ Q _ _ _
Q _ _ _ _ _ _ _
_ _ _ Q _ _ _ _
_ _ _ _ _ Q _ _


_ _ Q _ _ _ _ _
_ _ _ _ _ _ Q _
_ Q _ _ _ _ _ _
_ _ _ _ _ _ _ Q
_ _ _ _ _ Q _ _
_ _ _ Q _ _ _ _
Q _ _ _ _ _ _ _
_ _ _ _ Q _ _ _


_ _ Q _ _ _ _ _
_ _ _ _ _ _ _ Q
_ _ _ Q _ _ _ _
_ _ _ _ _ _ Q _
Q _ _ _ _ _ _ _
_ _ _ _ _ Q _ _
_ Q _ _ _ _ _ _
_ _ _ _ Q _ _ _
----------------------------
"""
