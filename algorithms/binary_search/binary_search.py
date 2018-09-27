def binary_search(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2

        if target == data[mid]:
            return mid
        if target < data[mid]:
            high = mid - 1
        elif target > data[mid]:
            low = mid + 1

    return -1


def binary_search_recursive(data, target, low, high):
    if low > high:
        return -1
    else:
        mid = (low + high) // 2

        if target == data[mid]:
            return mid
        elif target < data[mid]:
            return binary_search_recurisve(data, target, low, mid - 1)
        else:
            return binary_search_recursive(data, target, mid + 1, high)
