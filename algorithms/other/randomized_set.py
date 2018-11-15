"""Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
"""


class RandomizedSet:
    def __init__(self):
        self.nums, self.lookup = [], {}  # lookup is used to record indices

    def insert(self, val):
        if val not in self.lookup:
            self.nums.append(val)
            self.lookup[val] = len(self.nums) - 1
            return True
        return False

    def remove(self, val):
        """Here we swap val with the current last element. This supports O(1) time, as we can always remove from end of list."""
        if val in self.lookup:
            index = self.lookup[val]
            last = self.nums[-1]

            self.nums[index] = last  # replace val with last
            self.lookup[last] = index  # update last's index
            self.nums.pop()  # remove last element

            del self.lookup[val]
            return True
        return False

    def get_random(self):
        return random.choice(self.nums)
