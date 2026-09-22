# Greedy Bin Packing (Best Fit Decreasing)

Packs a set of files onto as few disks as possible, using the Best Fit Decreasing strategy: files are placed largest first (since large files are hardest to fit later), and each file goes on whichever disk will have the smallest amount of leftover space afterward.

Files are sorted by size using an explicit merge sort implementation rather than a built-in sort, guaranteeing O(n log n) sorting time in the worst case (a quicksort implementation's O(n²) worst case would have undermined the overall time complexity bound).

## Optimality

This is a greedy approximation, not an exact solver. The underlying problem, bin packing, is NP-hard, so no known polynomial-time algorithm guarantees the true minimum number of disks or the true minimum wasted space in every case. Best Fit Decreasing tends to perform close to optimal in practice, but a greedy choice made early on can occasionally block a better global arrangement later, since a placement, once made, is never revisited or swapped.

## Complexity

- **Time:** O(n log n + n × m), where n is the number of files and m is the number of disks. Sorting takes O(n log n); scanning every disk for every file takes O(n × m).
- A brute force approach that tried every possible file-to-disk assignment would cost O(mⁿ × n), exponential in n, which is impractical beyond a small number of files.

## Usage

```
python3 best_fit_decreasing.py
```

Runs the worked example from the assignment: two 100 MB disks and files of 51, 50, 49, and 50 MB, which Best Fit Decreasing packs with zero wasted space.

### Requirements

- Python 3, no external packages needed
