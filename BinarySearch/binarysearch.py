def binary_search(a_list, target):
    first = 0
    last = len(a_list) - 1

    while first <= last:

        i = (first + last) // 2

        item_at_mid = a_list[i]

        if item_at_mid == target:
            return i

        if item_at_mid < target:
            first = i + 1

        elif item_at_mid > target:
            last = i - 1

    return -1
