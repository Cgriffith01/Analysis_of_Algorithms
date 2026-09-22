# Divide-and-Conquer Playlist Search (Ternary Search)

Searches a sorted, alphabetically ordered list of song titles for a match. Instead of splitting the search space in half at each step like binary search, this splits it into three roughly equal parts, comparing the target against the first element of the second and third parts to decide which third to search next.

## Complexity

- **Time:** O(log₃ n), which simplifies to O(log n) in Big-O terms since the base of a logarithm doesn't matter, log₃ n and log₂ n differ only by a constant factor.
- In practice, this doesn't outperform binary search: it does more comparison work per step (checking two candidate positions instead of one), which tends to cancel out the benefit of shrinking the list faster per step.

## Usage

```
python3 ternary_search.py
```

Searches a sample 15-song playlist for five test titles, including one that doesn't exist, and prints the result for each.

### Requirements

- Python 3, no external packages needed
