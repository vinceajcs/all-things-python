# Remove duplicates from a list
def remove_duplicates(list):
    result = []
    for num in list:
        if num not in result:
            result.append(num)

    return result
