#!/usr/bin/python3
import sys

def is_valid(board, row, col, n):
    """ validate the board"""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(n, row, board, solutions):
    """solve nqueens"""
    if row == n:
        solutions.append(board[:])
        return

    for col in range(n):
        if is_valid(board, row, col, n):
            board[row] = col
            solve_nqueens(n, row + 1, board, solutions)
            board[row] = -1

def print_solution(board):
    """ Print Solution"""
    solution = []
    for row in range(len(board)):
        solution.append([row, board[row]])
    print(solution)

def nqueens(n):
    """ number of solutions"""
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    solutions = []
    board = [-1] * n
    solve_nqueens(n, 0, board, solutions)

    for solution in solutions:
        print_solution(solution)

def main():
    """Main"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    nqueens(n)

if __name__ == "__main__":
    main()
