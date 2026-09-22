# Dynamic Programming Image Comparison

Compares two black-and-white images row by row to decide whether they're similar or different, even when the two images have a different number of columns. Each row is treated as a binary string, and an edit-distance style dynamic programming recurrence finds the cheapest way to align one row against the other, allowing for pixel insertions, deletions, and substitutions.

Rather than reading the mismatch cost from a single bottom-right cell of the distance matrix, the algorithm scans the entire bottom row and takes the minimum. That keeps the comparison fair when a row from one image is a different length than the corresponding row from the other, extra trailing pixels aren't penalized unless they're actually needed to explain a real difference.

## Optimality

Unlike the greedy bin packing algorithm, this dynamic programming approach is guaranteed to find the true minimum difference for each row, not just a good approximation. The recurrence has both properties dynamic programming requires: optimal substructure (the cheapest alignment of a prefix is built from the cheapest alignment of a smaller prefix) and overlapping subproblems (the same cell values get reused across multiple later calculations), so filling the matrix once, bottom-up, is guaranteed to reach the exact optimum.

## Complexity

- **Time:** O(J × K) per row, where J and K are the row lengths of the two images. Across all I rows, that's O(I × J × K) total, or O(n³) if the images are roughly square with side length n.
- **Space:** O(J × K), since only one row's distance matrix needs to exist in memory at a time.

## Usage

```
python3 edit_distance.py
```

Runs the worked example from the assignment (two 3-row images) and prints the total difference along with the similar/different verdict at two different thresholds, plus a smaller example showing rows of different lengths being compared.

### Requirements

- Python 3, no external packages needed
