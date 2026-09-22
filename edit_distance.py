"""
Row-by-row black-and-white image comparison using dynamic programming.

Compares two binary images (0 = black, 1 = white) that may have a
different number of columns per row, using an edit-distance style
recurrence to find the cheapest way to align each row of one image
against the corresponding row of the other.
"""


def compare_row(row_x, row_y):
    """
    Returns the minimal mismatch cost between one row of image X and
    the corresponding row of image Y, allowing pixel insertions,
    deletions, and substitutions.
    """
    J = len(row_x)
    K = len(row_y)

    D = [[0] * (K + 1) for _ in range(J + 1)]

    for j in range(J + 1):
        D[j][0] = j
    for k in range(K + 1):
        D[0][k] = k

    for j in range(1, J + 1):
        for k in range(1, K + 1):
            if row_x[j - 1] == row_y[k - 1]:
                match_value = D[j - 1][k - 1]
            else:
                match_value = D[j - 1][k - 1] + 1

            del_value = D[j - 1][k] + 1
            ins_value = D[j][k - 1] + 1

            D[j][k] = min(match_value, del_value, ins_value)

    # minVal is read from the minimum of the entire bottom row, not just
    # the bottom-right corner, so rows of different lengths are compared fairly.
    return min(D[J])


def compare_images(X, Y, thresh):
    """
    X: list of I rows, each a list of 0/1 pixels (initialImage).
    Y: list of I rows, each a list of 0/1 pixels (finalImage).
    thresh: similarity threshold.

    Returns (verdict, total_difference).
    """
    total_difference = 0
    for row_x, row_y in zip(X, Y):
        total_difference += compare_row(row_x, row_y)

    if total_difference > thresh:
        return "The images are different", total_difference
    else:
        return "The images are similar", total_difference


if __name__ == "__main__":
    # Worked example from the report: 3 rows each.
    X = [
        [0, 0, 1, 1, 0],
        [1, 1, 0, 0, 1],
        [0, 0, 1, 1, 1],
    ]
    Y = [
        [0, 0, 1, 1, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 1, 1, 1],
    ]

    for thresh in (3, 1):
        verdict, total_difference = compare_images(X, Y, thresh)
        print(f"thresh={thresh}: totalDifference={total_difference} -> {verdict}")

    # A second example: images with rows of different lengths.
    X2 = [[0, 1, 1, 0, 1, 0]]
    Y2 = [[0, 1, 1, 0]]
    verdict, total_difference = compare_images(X2, Y2, thresh=1)
    print(f"\nDifferent row lengths: totalDifference={total_difference} -> {verdict}")
