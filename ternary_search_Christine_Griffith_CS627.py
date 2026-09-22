def ternary_search(playlist, song):
    """
    Divide-and-conquer search that splits the list into 3 parts.
    Sorted alphabetically (ascending), a list of strings.
    Returns the index of 'song' in playlist, or -1 if not found.
    """
    return _search(playlist, song, 0)


def _search(sublist, song, offset):
    if len(sublist) == 0:
        return -1

    # Split the current sublist into 3 roughly equal pieces
    size = len(sublist)
    first_end = size // 3
    second_end = 2 * size // 3

    part1 = sublist[0:first_end]
    part2 = sublist[first_end:second_end]
    part3 = sublist[second_end:size]

    # Checking if the song matches the first item of part2 or part3
    # "checkpoints"
    if part2 and song == part2[0]:
        return offset + first_end
    if part3 and song == part3[0]:
        return offset + second_end

    # Decide which third to search next based on alphabetical comparison
    if part2 and song < part2[0]:
        return _search(part1, song, offset)
    elif part3 and song < part3[0]:
        return _search(part2[1:], song, offset + first_end + 1)
    else:
        return _search(part3[1:], song, offset + second_end + 1)


if __name__ == "__main__":
    playlist = [
        "Alone", "Blinding Lights", "Circles", "Dreamer", "Everglow",
        "Fireflies", "Golden Hour", "Havana", "Ivy", "Jealous",
        "Kiwi", "Levitating", "Memories", "November Rain", "Ocean Eyes"
    ]

    test_songs = ["Havana", "Alone", "Ocean Eyes", "Circles", "Fake Song"]

    for song in test_songs:
        result = ternary_search(playlist, song)
        if result != -1:
            print(f'"{song}" found at index {result}')
        else:
            print(f'"{song}" not found in playlist')
