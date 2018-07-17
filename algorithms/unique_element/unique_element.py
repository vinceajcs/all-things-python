def unique_naive(list):
    """Return True if there are no duplicates in the list."""
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] == list[j]:
                return False
    return True


def unique_sorted(list):
    """Running time of O(nlogn), assuming sorting time is O(nlogn)."""
    sorted_list = sorted(list)
    for i in range(1, len(sorted_list)):
        if sorted_list[i - 1] == sorted_list[i]:
            return False
    return True


uniques = [8, 10, 5, 7, 72, 88, 100]
duplicates = [1, 3, 3, 5, 2]

print(unique_sorted(uniques))
print(unique_sorted(duplicates))
