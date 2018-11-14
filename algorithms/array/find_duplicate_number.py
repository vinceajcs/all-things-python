"""Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist.
Assume that there is only one duplicate number - find the duplicate one (duplicate can be repeated more than once).

Example 1:
Input: [1,3,4,2,2]
Output: 2

Example 2:
Input: [3,1,3,4,2]
Output: 3

We can treat the array like a LL; this is possible because each integer is between 1 and n.
Thus, we know a duplicate exists if there is a cycle in the LL.
Duplicate is the entry point of the cycle.

Algorithm:
1. Use two pointers, slow and fast, to find cycle
2. Reset slow pointer to the beginning and move both slow and fast to find the duplicate

Time: O(n)
Space: O(1)
"""


def find_duplicate(nums):
	if len(nums) <= 1:
        return -1

    slow, fast = nums[0], nums[nums[0]]

    while slow != fast: # find cycle
        slow = nums[slow]
        fast = nums[nums[fast]]

    slow = 0 # reset slow pointer, start from beginning

    while slow != fast: # find duplicate (entry point of cycle)
        slow = nums[slow]
		fast = nums[fast]

    return slow


"""Using sort."""


def find_duplicate(nums):
	if len(nums) <= 1:
		return -1

	sorted_nums = sorted(nums)

	for i in range(1, len(sorted_nums)):
		if sorted_nums[i] == sorted_nums[i-1]:
			return sorted_nums[i]

	return -1
