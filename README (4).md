# AI Agent: Sudoku Solver (Backtracking Search)

Solves a Sudoku puzzle from any given starting state, treating it as a search over the space of partial board assignments. Two versions are implemented:

- **`solve_brute_force`** - always fills the next empty cell in a fixed, left-to-right, top-to-bottom order, trying every legal digit before backtracking.
- **`solve_mrv`** - uses the minimum remaining values (MRV) heuristic, always filling whichever empty cell currently has the *fewest* legal candidate digits. Choosing the most constrained cell first means the search hits contradictions, and therefore backtracks, much sooner.

Both implementations use Python's own call stack for recursion rather than the explicit stack shown in the assignment's pseudocode, the search behavior is identical either way.

## State Space and Complexity

A brute force search that ignored the row, column, and box constraints entirely would face p^(n²) possible leaf states for an n × n board with p permitted digits, for a standard 9×9 board that's 9^81, far too large to search exhaustively. Row, column, and box constraint checking (used by both versions here) already rules out huge portions of that space at every step; the MRV heuristic on top of that prunes even more aggressively by finding contradictions early.

## Optimality

Both versions are guaranteed to find a correct solution if one exists (or correctly report failure if the puzzle is unsolvable), since backtracking exhaustively explores the legal search space with no shortcuts that could skip a valid solution. MRV changes *how fast* the answer is found, not *whether* it's found. Both return the same solution when one exists.

## Usage

```
python3 backtracking_search.py
```

Solves a sample 9×9 puzzle with both versions, verifies each solution is valid, and prints how many recursive calls each approach needed. On the included sample puzzle, brute force takes several thousand calls while the MRV version solves the same puzzle in well under a hundred, a concrete demonstration of how much the heuristic prunes the search space.

### Requirements

- Python 3, no external packages needed

### Notes

- Works on any n × n board where n is a perfect square (9×9, 4×4, 16×16, etc.), since box regions are computed as √n × √n.
