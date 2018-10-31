"""Given a string, sort it in decreasing order based on the frequency of characters.

Time: O(n)
Space: O(1)
"""


def frequency_sort(s):
    if not s:
        return ''

    counter = collections.Counter(s)
    pairs = counter.most_common()

    result = []
    for char, freq in pairs:
        for _ in range(freq):
            result.append(char)

    return ''.join(result)


"""Without using Counter and built-in method most_common()."""


def frequency_sort(s):
    if not s:
        return ''

    counter, result = {}, ''

    for c in s:
        counter[c] = 1 if c not in counter else counter[c] + 1

    sorted_counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)

    for char, freq in sorted_counter:
        result += char * freq

    return result
