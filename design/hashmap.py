"""Design a HashMap without using any built-in hash table libraries."""


class MyHashMap:
    def __init__(self):
        self.table = [-1] * 1000001

    def put(self, key, value):
        self.table[key] = value  # assuming value is nonnegative

    def get(self, key):
        return self.table[key]  # returns -1 if key value pair does not exist

    def remove(self, key):
        self.table[key] = -1
