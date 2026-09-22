"""
Backtracking Sudoku solver, in two versions:

- solve_brute_force: always fills the next empty cell in a fixed,
  left-to-right, top-to-bottom scan order.
- solve_mrv: uses the minimum remaining values (MRV) heuristic,
  always filling whichever empty cell currently has the fewest legal
  candidate digits, which tends to hit contradictions (and therefore
  backtrack) much sooner.

Both use Python's call stack for recursion in place of the explicit
stack shown in the pseudocode, the search behavior is the same either way.

Boards are n x n grids of ints, 0 for an empty cell, using square
box regions (box_size = sqrt(n)), so this works for a standard 9x9
board or any other perfect-square size such as 4x4.
"""

import copy
import math


def is_legal(board, row, col, value, box_size):
    """Whether placing `value` at (row, col) breaks no row/column/box rule."""
    n = len(board)

    if value in board[row]:
        return False
    if any(board[r][col] == value for r in range(n)):
        return False

    box_row = (row // box_size) * box_size
    box_col = (col // box_size) * box_size
    for r in range(box_row, box_row + box_size):
        for c in range(box_col, box_col + box_size):
            if board[r][c] == value:
                return False

    return True


def legal_values(board, row, col, box_size):
    n = len(board)
    return {v for v in range(1, n + 1) if is_legal(board, row, col, v, box_size)}


def find_first_empty_cell(board):
    """Fixed scan order: left to right, top to bottom."""
    n = len(board)
    for r in range(n):
        for c in range(n):
            if board[r][c] == 0:
                return r, c
    return None


def select_mrv_cell(board, box_size):
    """
    Returns (row, col, candidates) for the empty cell with the fewest
    legal candidates, or None if the board has no empty cells left.
    """
    n = len(board)
    best = None
    best_candidates = None

    for r in range(n):
        for c in range(n):
            if board[r][c] == 0:
                candidates = legal_values(board, r, c, box_size)
                if best is None or len(candidates) < len(best_candidates):
                    best = (r, c)
                    best_candidates = candidates
                    if len(candidates) == 0:
                        # dead end found, no need to keep scanning
                        return r, c, candidates

    if best is None:
        return None
    return best[0], best[1], best_candidates


def solve_brute_force(board, stats=None):
    """Backtracking with no cell-ordering heuristic. Solves `board` in place."""
    if stats is not None:
        stats["calls"] += 1

    box_size = int(round(math.sqrt(len(board))))
    empty = find_first_empty_cell(board)
    if empty is None:
        return True  # solved

    row, col = empty
    for v in range(1, len(board) + 1):
        if is_legal(board, row, col, v, box_size):
            board[row][col] = v
            if solve_brute_force(board, stats):
                return True
            board[row][col] = 0

    return False


def solve_mrv(board, stats=None):
    """Backtracking guided by the MRV heuristic. Solves `board` in place."""
    if stats is not None:
        stats["calls"] += 1

    box_size = int(round(math.sqrt(len(board))))
    cell = select_mrv_cell(board, box_size)
    if cell is None:
        return True  # solved

    row, col, candidates = cell
    if not candidates:
        return False  # dead end, backtrack

    for v in candidates:
        board[row][col] = v
        if solve_mrv(board, stats):
            return True
        board[row][col] = 0

    return False


def print_board(board):
    box_size = int(round(math.sqrt(len(board))))
    for r, row in enumerate(board):
        line = ""
        for c, val in enumerate(row):
            line += (str(val) if val != 0 else ".") + " "
            if (c + 1) % box_size == 0 and c != len(row) - 1:
                line += "| "
        print(line)
        if (r + 1) % box_size == 0 and r != len(board) - 1:
            print("-" * (len(line)))


def is_valid_solution(board):
    n = len(board)
    box_size = int(round(math.sqrt(n)))
    full = set(range(1, n + 1))

    for row in board:
        if set(row) != full:
            return False
    for c in range(n):
        if {board[r][c] for r in range(n)} != full:
            return False
    for br in range(0, n, box_size):
        for bc in range(0, n, box_size):
            box = {
                board[r][c]
                for r in range(br, br + box_size)
                for c in range(bc, bc + box_size)
            }
            if box != full:
                return False
    return True


if __name__ == "__main__":
    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

    print("Starting puzzle:")
    print_board(puzzle)

    board_bf = copy.deepcopy(puzzle)
    stats_bf = {"calls": 0}
    solve_brute_force(board_bf, stats_bf)

    board_mrv = copy.deepcopy(puzzle)
    stats_mrv = {"calls": 0}
    solve_mrv(board_mrv, stats_mrv)

    print("\nSolved (brute force):")
    print_board(board_bf)
    print(f"Valid solution: {is_valid_solution(board_bf)}")
    print(f"Recursive calls: {stats_bf['calls']}")

    print("\nSolved (MRV heuristic):")
    print_board(board_mrv)
    print(f"Valid solution: {is_valid_solution(board_mrv)}")
    print(f"Recursive calls: {stats_mrv['calls']}")

    print(f"\nBoth solutions match: {board_bf == board_mrv}")
