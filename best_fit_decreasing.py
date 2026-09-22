"""
Best Fit Decreasing bin packing.

Packs a set of files onto as few disks as possible, choosing for each
file the disk that leaves the smallest amount of leftover space.
Files are placed largest first, since large files are the hardest to
place later.

This is a greedy approximation algorithm, not an exact solver: bin
packing is NP-hard, so this does not guarantee the true minimum number
of disks or the true minimum wasted space in every case.
"""


def merge_sort_indices_by_size_desc(sizes):
    """
    Returns a list of indices into `sizes`, ordered from the largest
    size to the smallest. Uses merge sort so the ordering step is
    guaranteed O(n log n), unlike quicksort's O(n^2) worst case.
    """
    indices = list(range(len(sizes)))

    def merge_sort(idx_list):
        if len(idx_list) <= 1:
            return idx_list
        mid = len(idx_list) // 2
        left = merge_sort(idx_list[:mid])
        right = merge_sort(idx_list[mid:])
        return merge(left, right)

    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if sizes[left[i]] >= sizes[right[j]]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    return merge_sort(indices)


def best_fit_decreasing(sizes, capacities):
    """
    sizes: list of file sizes (MB).
    capacities: list of disk capacities (MB).

    Returns a list `assignment` the same length as `sizes`, where
    assignment[i] is the index of the disk file i was placed on, or
    -1 if the file is larger than every disk's capacity.
    """
    remaining = list(capacities)
    assignment = [0] * len(sizes)

    sorted_indices = merge_sort_indices_by_size_desc(sizes)

    for i in sorted_indices:
        best_disk = -1
        best_leftover = float("inf")

        for j in range(len(capacities)):
            if remaining[j] >= sizes[i]:
                leftover = remaining[j] - sizes[i]
                if leftover < best_leftover:
                    best_disk = j
                    best_leftover = leftover

        if best_disk != -1:
            assignment[i] = best_disk
            remaining[best_disk] -= sizes[i]
        else:
            assignment[i] = -1

    return assignment, remaining


if __name__ == "__main__":
    # Worked example: two 100 MB disks, files of 51, 50, 49, and 50 MB.
    sizes = [51, 50, 49, 50]
    capacities = [100, 100]

    assignment, remaining = best_fit_decreasing(sizes, capacities)

    print("Files:", sizes)
    print("Disk capacities:", capacities)
    print()

    for i, disk in enumerate(assignment):
        if disk == -1:
            print(f"File {i} (size {sizes[i]} MB): does not fit on any disk")
        else:
            print(f"File {i} (size {sizes[i]} MB): placed on disk {disk}")

    print()
    for j, space_left in enumerate(remaining):
        print(f"Disk {j}: {space_left} MB free")

    disks_used = len({d for d in assignment if d != -1})
    print(f"\nDisks used: {disks_used} of {len(capacities)}")
