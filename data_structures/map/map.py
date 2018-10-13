"""Implement a data structure 'Map' that stores pairs of integers (key, value) and supports the following methods in O(1) runtime: insert, delete, get, get_random_key."""


class Map:
    def __init__(self):
        self.hashmap = {}
        self.keys = []
        self.length = 0

    def insert(key, value):
        index = length
        hashmap[key] = (value, index)
        keys[index] = key
        length += 1

    def get(key):
        return hashmap[key][0]  # return value

    def delete(key):
        # delete from list of keys
        index = hashmap[key][1]
        keys[index], keys[length - 1] = keys[length - 1], keys[index]
        length -= 1

        # delete from dict
        del hashmap[key]

        # update index of swapped key
        hashmap[keys[index]][1] = index

    def get_random_key():
        r = random.randint(0, length - 1)
        # can also just return random.choice(keys)
        return keys[r]
