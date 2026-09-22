# In-Place Array Reversal

Reverses a list of integers in place using the two-pointer technique: a `start` pointer at the front and an `end` pointer at the back swap values and move toward each other until they meet.

Originally designed as a prototype for an in-place audio reversal feature on a memory-constrained mobile device, no second buffer is ever allocated.

## Complexity

- **Time:** O(n) — every element is touched by exactly one swap, regardless of the input's contents or order.
- **Space:** O(1) — only a fixed, small set of scalar variables (`start`, `end`, `temp`) are used beyond the input array itself.

## Usage

```
python3 two_pointer_reversal.py
```

The script reverses a small example list, then measures and plots how runtime scales with input size (n = 500, 1,500, and 2,500), saving the chart to `runtime_plot.png`. The near-linear relationship in the plot matches the O(n) time complexity.

### Requirements

- Python 3
- `matplotlib` (`pip install matplotlib`)
