# Algorithms

A small collection of classic algorithm implementations, each demonstrated with a runnable example.

## Files

- **reverse_array.py** - reverses a list of integers in place using the two-pointer technique, and benchmarks how runtime scales with input size.
- **ternary_search.py** - a divide-and-conquer search over a sorted list of song titles, splitting the search space into three parts per step instead of two.

## reverse_array.py

Reverses a list in place by swapping elements from the outside in, moving a `start` pointer forward and an `end` pointer backward until they meet in the middle.

- **Time complexity:** O(n)
- **Space complexity:** O(1), no extra array is allocated

Running the script:

1. Reverses a small example list (`[1, 2, 3, 4, 5]`) and prints it before and after.
2. Times how long a reversal takes for lists of size 500, 1,500, and 2,500.
3. Plots runtime against input size and saves the chart to `runtime_plot.png`.

### Requirements

- Python 3
- `matplotlib` (`pip install matplotlib`)

### Usage

```
python3 reverse_array.py
```

## ternary_search.py

Searches a sorted, alphabetically ordered list of song titles for a match. At each step, the current sublist is split into three roughly equal parts, and the target is compared against the first element of the second and third parts to figure out which third to search next.

- **Time complexity:** O(log₃ n), which is still O(log n) overall, though ternary search does more comparisons per step than binary search, so it isn't actually faster in practice
- **Space complexity:** O(log n) for the recursion, plus some overhead from slicing sublists at each call

Running the script searches a sample playlist of 15 songs for five test titles (including one that doesn't exist) and prints the result for each.

### Requirements

- Python 3, no external packages needed

### Usage

```
python3 ternary_search.py
```
