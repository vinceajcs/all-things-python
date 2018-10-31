"""Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Time: O(2**n)
Space: O(1)
"""


def restore_ip(s):
    result = []
    dfs(s, 0, '', result)
    return result


def dfs(s, index, path, result):
    if index == 4:
        if not s:
            result.append(path[:-1])
        return  # backtracking

    for i in range(1, 4):
        # the digits we choose should not be more than the length of s
        if i <= len(s):
            # choose one digit
            if i == 1:
                dfs(s[i:], index + 1, path + s[:i] + ".", result)
            # choose two digits, the first one should not be "0"
            elif i == 2 and s[0] != "0":
                dfs(s[i:], index + 1, path + s[:i] + ".", result)
            # choose three digits, the first one should not be "0", and should less than 256
            elif i == 3 and s[0] != "0" and int(s[:3]) <= 255:
                dfs(s[i:], index + 1, path + s[:i] + ".", result)
