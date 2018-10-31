"""Given a sorted integer array without duplicates, return the summary of its ranges.


Idea: This is similar to the longest consecutive sequence problem.
We can iterate through the array once.

1. At each index, extend streak as long as possible.
2. If no streak is made, add number at index of array to the result.
3. If there is a streak, add the streak and then move index to the end of the streak.

Time: O(n)
Space: O(1)
"""


def summary_ranges(nums):
    result = []
    if not nums:
        return result

    i = 0
    while i < len(nums):
        count = 0

        next_num = nums[i] + 1

        while next_num in nums:
            next_num += 1
            count += 1

        if not count:  # no streak made
            result.append(str(nums[i]))
            i += 1
        else:  # add streak to result
            current_range = '{}->{}'.format(nums[i], nums[i + count])
            # above same as str(nums[i]) + '->' + str(nums[i+count])
            result.append(current_range)
            i += count + 1  # move index to end of streak

    return result
